import pandas as pd 
import matplotlib.pyplot as plt

data=pd.read_csv("laptop_price.csv",encoding='latin-1')

display1=pd.DataFrame(data)

print(display1)
print(type(display1))
print(display1.info())


display1.plot(kind='pie',
         x='Company',
         y='Price_euros',
         color='red')

plt.title("Laptop Price Graph")
plt.show()