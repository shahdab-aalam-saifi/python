import pandas as pd

names=["GANESH","MANISH","NILESH","NITIN"]
ages=[49,25,40,44]

my_dict={"names":names,"age":ages}

#print(my_dict.keys())

df=pd.DataFrame(my_dict)
#print(df)
df.to_csv("emp.csv")
df1=pd.read_csv("emp.csv")


