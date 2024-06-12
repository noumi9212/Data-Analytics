import pandas as pd
import csv

path = "E:\\Drive\\Mega@Simulation365\\Data Analytics\\Labs\\Python Dev\\pandas\\exercise\\exercise\\Titanic-Dataset.csv"
df = pd.read_csv(path)

print(df.head(891)) #dataset has 891 rows and 12 cols
print(df.info()) #cols 5, 10 and 11 have null values
print(df.describe()) #7 cols are numerical, age having null values to be replaced by mean/median 
print(df.isnull().sum()) #Age, Cabin and Embarked have null values

#find duplicated duplicates
duplicatedRows = df[df.duplicated()]
print(duplicatedRows) #no duplicates found

#Handle outliers 
Q1 = df['Age'].quantile(0.25)
Q3 = df['Age'].quantile(0.75)
IQR = Q3 - Q1
threshhold = 1.5
lower_bound = Q1 - threshhold * IQR
upper_bound = Q3 + threshhold * IQR
print("Lower Bound:", lower_bound, "Upper Bound:", upper_bound)
outliers = df[(df['Age'] < lower_bound) | (df['Age'] > upper_bound)]
print('Outliers Printing')
print(outliers) #data has outliers

#calculate median
median_age = df['Age'].median()
mean_age = df['Age'].mean()
print(median_age)
print(mean_age)

#replace outliers using median
df.loc[(df['Age'] < lower_bound) | (df['Age'] > upper_bound), 'Age'] = median_age
#fill nan for age using median
df['Age'] = df['Age'].fillna(df['Age'].median())

#conver floats to int
df['Age'] = pd.to_numeric(df['Age']).astype(int)


#fill nan for Cabin using mode
df['Cabin'] = df['Cabin'].fillna(df['Cabin'].mode()[0])
#fill nan for Embarked using mode
df['Embarked'] = df['Embarked'].fillna(df['Embarked'].mode()[0])
print(df.info())
print(df.isnull().sum())
#export clean data to new file
clean_file_path = "E:\\Drive\\Mega@Simulation365\\Data Analytics\\Labs\\Python Dev\\pandas\\exercise\\exercise\\Clean-Titanic-Dataset.csv"
with open(clean_file_path,mode='w',newline='') as file:
    writer = csv.writer(file)
    writer.writerow(df)
    writer.writerows(df.to_numpy())


print("Submitted by: Nouman Karim")













