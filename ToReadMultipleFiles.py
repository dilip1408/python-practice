import pandas as pd

#print(glob.glob("C:/Users/dvoruga/Desktop/uploadS3/*.csv"))

ksn_group_id_data = "C:/Users/dvoruga/Desktop/uploadS3/ksn_group_id_data1.csv"
points_data = "C:/Users/dvoruga/Desktop/uploadS3/Pat5.csv"

list1 = [ksn_group_id_data, points_data]

#print(list1[0])
counter = 0
for file in list1:
    fileToRead = pd.read_csv(file)
    x = fileToRead[:4]
    if(counter == 0):
        ksnfile = x
        print("reading first file")
        print(ksnfile)
        print(counter)
        counter = counter+1
    else:
        pointsfile = x
        print("y value is:::::::::::::::")
        print(pointsfile)
        print(counter)


