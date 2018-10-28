# Read json file to pandas Dataframe

Reading a json file is very easy.

```
file_activeingredient = open('opencanada/activeingredient.json', 'r')

# Load the first sheet of the JSON file into a data frame
activeingredients = pd.read_json(file_activeingredient, orient='records')

# View the first ten rows
# print(activeingredients.head(10))
```

More info [here](https://pythonspot.com/json-encoding-and-decoding-with-python/) and [here](https://chrisalbon.com/python/data_wrangling/load_json_file_into_pandas/).
