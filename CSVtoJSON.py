import csv, json
csvFilePath = "C:\\Users\dvoruga\Desktop\promo_sears_offers.csv"
jsonFilePath = "C:\\Users\dvoruga\Desktop\happy.json"

# Read CSV and add the data to the dictionary
data={}
with open(csvFilePath) as csvFile:
    csvReader = csv.DictReader(csvFile)
    for csvRow in csvReader:
        hmid = csvRow["hmid"]
        data[hmid] = csvRow

print(data)



#write data to JSON file


