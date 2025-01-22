# Workflow: `btc.py` -> `merge_csv.py` -> `plot.py` :shipit:

### `btc.py`
- Checks the Bitcoin price approximately once every second.
- Logs the price with the current datetime to a `.csv` file.

### `merge_csv.py`
- Merges all data from the `all_data` folder into a single CSV file.
- Saves the merged file in the `merged_data` folder.
