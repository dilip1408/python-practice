import zipfile36 as zipfile
import wget
import os
import pandas as pd
# pd.set_option('display.max_columns', 22)

#
# print('Beginning file download with wget module')
# url = 'http://api.worldbank.org/v2/en/indicator/NY.GDP.MKTP.CD?downloadformat=csv'
# wget.download(url, 'C:/Users/dvoruga/Downloads/gdp_data.zip')
#
# with zipfile.ZipFile('C:/Users/dvoruga/Downloads/gdp_data.zip', "r") as z:
#     z.extractall("")
# pd.set_option('precision',199)
gdp = pd.read_csv('C:/Users/dvoruga/Downloads/API_NY.GDP.MKTP.CD_DS2_en_csv_v2_713242/API_NY.GDP.MKTP.CD_DS2_en_csv_v2_713242.csv', skiprows=4)
print(type(gdp))
gdp.drop(['Country Code','Indicator Name','Indicator Code','Unnamed: 64'], axis=1, inplace=True)
# Set the Index on Country Name - previously was numeric.
gdp_transpose = gdp.set_index('Country Name')
# Transpose the index and columns
gdp_transpose = gdp_transpose.transpose()
# Reset the index, sets, 'index' as a column
gdp_transpose = gdp_transpose.reset_index()
# Rename the 'index' column to year
gdp_transpose = gdp_transpose.rename(columns={'index':'Year'})
# Set the DataFrame Index to newly named 'Year'
gdp_transpose = gdp_transpose.set_index('Year')

print(gdp_transpose.head())

gdp_pct_diff = gdp_transpose
gdp_pct_diff = gdp_pct_diff.pct_change()
print(gdp_pct_diff.head())
gdp_pct_diff_transpose = gdp_pct_diff.transpose().reset_index()
melted_gdp = pd.melt(gdp,id_vars=['Country Name'],value_vars=gdp.columns[1:],var_name='Year',value_name='GDP')
melted_gdp_pct_diff  = pd.melt(gdp_pct_diff_transpose,id_vars='Country Name',value_vars=gdp_pct_diff_transpose.columns[1:],var_name='Year',value_name='GDP')

df = melted_gdp.merge(melted_gdp_pct_diff, left_index=True, right_index=True)

# Drop 2 columns
df = df.drop(['Country Name_y','Year_y',], axis=1)
# Rename 4 columns
df = df.rename(columns={'Country Name_x':'Country Name',
                        'Year_x':'Year',
                        'GDP_x':'GDP',
                        'GDP_y':'GDP_pct_change'})
# Cast Year to a numeric dtype
df['Year'] = pd.to_numeric(df['Year'])
# Drop NAs
df = df.dropna()

gdp_quartile = df
gdp_quartile['Quartile'] = gdp_quartile.groupby(['Year'])['GDP'].transform(
                     lambda x: pd.qcut(x, 4, labels=range(1,5)))


pct_change = gdp_quartile
# Group by Year and Quartile, focus the mean calculation on GDP_pct_change
pct_change = pd.DataFrame(pct_change.groupby(['Year','Quartile'])['GDP_pct_change'].mean())
# Rename the calculated column to Average GDP Pct Change
pct_change = pct_change.rename(columns={'GDP_pct_change':'Average GDP Pct Change'}).reset_index()

import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection

# Initialize figure and size of the plot
plt.figure(figsize=(14,8))

# Seaborn line plot
ax = sns.lineplot(x='Year',y='Average GDP Pct Change',
                  data=pct_change,
                  hue='Quartile',
                  palette='Accent')

# Create a dashed line at zero for comparison
ax.annotate("",
            xy=(1961, 0), xycoords='data',
            xytext=(2019, 0), textcoords='data',
            arrowprops=dict(arrowstyle="-",
                            ls='dashed',
                            edgecolor = "red",
                            connectionstyle="arc3, rad=0"),
           )


# Set xtick labels and rotate the x-axis labels
plt.setp(ax.get_xticklabels(), rotation=90)
# Set the title
plt.title('Average GDP Percent Change per Year - Quartiles')

plt.tight_layout()
# Grab the figure
fig = ax.get_figure()
# Save the figure
fig.savefig('Avg GDP pct change')