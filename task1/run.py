import pandas as pd

# Function to load data from a CSV file
def load_data(file_path):
    try:
        df = pd.read_csv(file_path)
        print("Data loaded successfully.")
        return df
    except Exception as e:
        print(f"Error occurred: {e}")
        return None

# Function to validate data
def validate_data(df):
    required_columns = ['investor_id', 'syndicate_id', 'transaction_amount', 'transaction_date']
    
    # Check if required columns exist
    if not set(required_columns).issubset(df.columns):
        print("Error: Some required columns are missing.")
        return False

    # Check for missing values
    if df[required_columns].isnull().sum().any():
        print("Error: There are missing values in the data.")
        return False

    # Data is valid
    return True

# Function to find top investors
def top_investors(df):
    # Group by investor_id and syndicate_id to find unique investments
    unique_investments = df.groupby(['investor_id','syndicate_id']).size().reset_index().rename(columns={0:'count'})
    # print(unique_investments)
    
    # Count the number of unique syndicates each investor invested in
    syndicate_counts = unique_investments['investor_id'].value_counts().reset_index(name='unique_syndicates').rename(columns={'index':'investor_id'})

    # Calculate the total amount each investor has invested
    total_investment = df.groupby('investor_id')['transaction_amount'].sum().reset_index().rename(columns={'transaction_amount':'total_investment'})

    # Merge the two dataframes on investor_id
    merged_df = pd.merge(syndicate_counts, total_investment, on='investor_id')

    # Sort by syndicate_count and select top 5
    top_investors = merged_df.sort_values(by='unique_syndicates', ascending=False).head(5)

    return top_investors

# Load and validate data
file_path = 'task1/dummy_data.csv'  # replace with your file path
df = load_data(file_path)
if df is not None and validate_data(df):
    # Find top investors
    top_5_investors = top_investors(df)
    print(top_5_investors)
else:
    print("Could not find top investors due to validation errors.")
