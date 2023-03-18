import pandas as pd

# create a sample DataFrame
df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})

# drop the last row
df = df.drop(df.index[-1])

# print the resulting DataFrame
print(df)
