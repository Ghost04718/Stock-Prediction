import pandas as pd
import os

# Step 1: Load the primary CSV file
data = pd.read_csv('senti_fin/000001_senti_factor.csv')
# Step 2: Filter the rows based on 'date'
dates_to_extract = pd.to_datetime(data['date']).dt.strftime('%Y%m%d').astype(int)

input_folder = "data02"
for filename in os.listdir(input_folder):
    if filename.endswith('.csv'):
        code = filename.split(".")[0]
        # Load the CSV file
        data = pd.read_csv(os.path.join(input_folder, filename))
        df = pd.read_csv(os.path.join(f'senti_fin/{code}_senti_factor.csv'))
        
        # Convert 'date' in df to the same format as 'dates_to_extract'
        # Filter the rows in df based on 'date' matching 'date' in dates_to_extract
        df['date'] = pd.to_datetime(df['date']).dt.strftime('%Y%m%d').astype(int)
        df_filtered = df[df['date'].isin(dates_to_extract)]
        
        # Filter the primary data based on 'trade_date' matching 'trade_date' in dates_to_extract
        data_filtered = data[data['trade_date'].isin(dates_to_extract)]
        
        # Merge the filtered dataframes on 'trade_date' and 'date'
        merged_df = pd.merge(df_filtered, data_filtered, left_on='date', right_on='trade_date', suffixes=('', '_primary'))
        
        # Save the merged dataframe to a new CSV file
        merged_df.to_csv(f'data03/{filename}', index=False)

        print(f"Merged data saved to {filename}.")