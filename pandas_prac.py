import pandas as pd 
# df = pd.read_csv("customers-100.csv") # reading the file 
# print(df)

# creating our own dataframe 
data = {
  "name":["aashiya","ashraf","arham"],
  "age":[19,18,4],
  "height":[5.11,6.3,5.3]
}
df = pd.DataFrame(data)
print(df)
df.to_csv("created.csv")


# preveiwing the data using methods 

print("the first two rows are displayed as")
print(df.head(2)) # for seeing the last two colums name we use tail method 

# getting the information of the datafarme we created 

df.info() # gives information about the respective dataframe like columns , null values , data type as well as the memory 







