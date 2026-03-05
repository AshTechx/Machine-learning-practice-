# import pandas as pd 
# df = pd.read_csv("sales_data.csv")
# print(df)
# print("the first five rows of the dataset is ",df.head())
# print("the last five rows of the datasets is ",df.tail())
# print("the no of rows and columns ",df.shape)
# print("the names of all columns",df.columns)
# print(df.info())
# print(df.describe())
# name = df[["CustomerName","Product"]]
# print(name)
# filtered_1 = df[(df["Quantity"]>2 ) & (df["Price"]>500)]
# print(filtered_1)

# filtered_2 = df[(df["Product"] =="Smartphone") | (df["Product"]=="Tablet")]
# print(filtered_2)

# creating our own dataframe 
import pandas as pd 
data = {"Day" :["Monday","Tuesday","Wednesday","Thursday","Friday"],
        "WorkoutType":["running","yoga","rest","cycling","strength training",],
        "Duration time":[30,45,34,50,50],
        "Calories burned":[300,450,200,500,460]
        }

df = pd.DataFrame(data)
print(df)
df.to_csv("workout.csv",index=False)
print(df.head())
print(df.tail())
print(df.info())
print(df.describe())
name = df [["WorkoutType"]]
print(name)
name_2 = df[["WorkoutType","Calories burned"]]
print(name_2)
filtered_rows = df[(df["Duration time"])>30]
print(filtered_rows)
filtered_rows_2 = df[(df["WorkoutType"]==" cycling" ) |(df["WorkoutType"]=="running")]
print(filtered_rows_2)
