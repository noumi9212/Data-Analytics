#from recursive import factorial
#num = int(input("Enter number to find factorial: "))
#factorial(num)

import pandas as pd

# Creating a sample DataFrame
data = {'Column1': ['1.9', '2', '3', '4.5']}
df = pd.DataFrame(data)

# Using to_numeric() method
df = pd.DataFrame(data)
df['Column1'] = pd.to_numeric(df['Column1']).astype(int)
print(df)
print(df['Column1'].dtype)