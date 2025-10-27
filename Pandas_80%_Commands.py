🧩 1. Data Input / Output (I/O)

You’ll load and save data constantly.

import pandas as pd

# Read data
df = pd.read_csv("data.csv")
df = pd.read_excel("data.xlsx")

# Save data
df.to_csv("output.csv", index=False)
df.to_excel("output.xlsx", index=False)


🧱 2. Data Creation

# From dict or list
df = pd.DataFrame({'name': ['Alice', 'Bob'], 'age': [25, 30]})
s = pd.Series([1, 2, 3], name="numbers")


🔍 3. Exploring Data

df.head()          # first 5 rows
df.info()          # column types + nulls
df.describe()      # summary stats
df.shape           # (rows, columns)
df.columns         # list of columns
df.dtypes          # data types


🎯 4. Selecting & Filtering

df['age']                  # one column
df[['name', 'age']]        # multiple columns
df.loc[df['age'] > 25]     # conditional filter
df.iloc[0:5]               # positional selection



🧹 5. Data Cleaning / Transformation

df.rename(columns={'age': 'Age'}, inplace=True)
df.drop(columns=['unneeded_col'], inplace=True)
df.dropna(inplace=True)           # remove missing
df.fillna(0, inplace=True)        # fill missing
df.replace('?', None, inplace=True)
df.astype({'Age': int})
df.duplicated().sum()             # count duplicates
df.drop_duplicates(inplace=True)



🔢 6. Sorting & Indexing

df.sort_values(by='Age', ascending=False, inplace=True)
df.reset_index(drop=True, inplace=True)
df.set_index('name', inplace=True)



📊 7. Aggregation & Grouping

df.groupby('category')['sales'].mean()
df.groupby(['region', 'category']).sum()



🔄 8. Merging & Combining

pd.concat([df1, df2])                         # stack vertically
pd.merge(df1, df2, on='id', how='left')       # join like SQL



🔁 9. Reshaping / Pivoting

df.pivot_table(values='sales', index='region', columns='year', aggfunc='sum')
df.melt(id_vars='region', var_name='year', value_name='sales')



⏰ 10. Date & Time

df['date'] = pd.to_datetime(df['date'])
df['year'] = df['date'].dt.year
df['month'] = df['date'].dt.month



📈 11. Basic Statistics

df['sales'].mean()
df['sales'].sum()
df['sales'].median()
df['sales'].value_counts()
df.corr()



🎨 12. Visualization (Quick Looks)

df['sales'].plot(kind='hist')
df.plot(x='month', y='sales', kind='line')




⚙️ 13. Utility Helpers

pd.to_numeric(df['col'], errors='coerce')
pd.set_option('display.max_rows', 100)
