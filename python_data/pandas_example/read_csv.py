import pandas as pd

df=pd.read_csv('C:\\Users\dell1\Desktop\pandas_example\students.csv')
print(df)
#print(df['Total'].max())
df.fillna(0,inplace=True)
print(df['Name'])

students_data={"Rollno":[100,200,300,400,500,600],"Name":["Ganesh","Manish",
"Nilesh","Siddhi","Kunal","Mrunal"],"Marks1":[80,70,67,77,88,90],"Marks2":
	[55,66,77,88,99,67],"Marks3":[65,76,87,98,66,77]}

print(students_data)

df=pd.DataFrame(students_data)
print(df)

print(df.shape)
rows,columns=df.shape
print("Rows ",rows)
print("Columns ",columns)
print(df.head(2))
print(df.tail(1))
print(df[2:5])
print(df.columns)
print(df[['Name','Marks1','Marks2','Marks3']])
