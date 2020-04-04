import glob
import pandas as pd
data_list = glob.glob("C:/Users/dvoruga/Desktop/uploadS3/Testdata*.xlsx")

print(data_list)


for f in glob.glob("C:/Users/dvoruga/Desktop/uploadS3/Testdata*.xlsx"):
    df = pd.read_excel(f)



