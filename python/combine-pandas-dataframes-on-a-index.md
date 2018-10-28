# Combine or merge two pandas Dataframes using a index

Reading a json file is very easy.

```
merged_df = df_1.merge(df_2,left_on='id', right_on='df1_id', how='outer')
```

More info [here](https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.merge.html).
