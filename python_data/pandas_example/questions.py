import pandas as pd
import time
df=pd.read_csv('C:\\Users\dell1\Desktop\pandas_example\questions.csv')
#print(df)
#print(df[['Q.No','Question']])
#print(df[['Q.No','Question']])

df1=df.head(2)
#print(df1)
df.set_index('Q.No',inplace=True)
df1=df.head(1)
print(df1['Question'])
print(df1[['op1','op2','op3','op4']])
'''for n in range(1,5):
		print(df['Question'])
		time.sleep(4)
'''		
