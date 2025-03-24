import pandas as pd

# Example DataFrames
df1 = pd.DataFrame({'A': [1, 2, 3],
                    'B': [4, 5, 6],
                    'C': [7, 8, 9]})

df2 = pd.DataFrame({'A': [1, 2, 3],
                    'D': [10, 11, 12]})

combined_df = pd.merge(df1, df2, on='A', how='outer')

print(combined_df)
