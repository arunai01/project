import pandas as pd 


# data={
#     "name":["Arun","Rathi","Saravanan"],
#     "Location":["Keeranur","Seethappatti","Peravurani"]

# }
# df=pd.DataFrame(data)

# print(df)

data=pd.read_csv("laptop_price.csv",encoding='latin-1')

df=pd.DataFrame(data)


#print(df)

print(df.head())
print(df.tail())

print(df.head(10).to_string())
print(df.tail(10).to_string())
