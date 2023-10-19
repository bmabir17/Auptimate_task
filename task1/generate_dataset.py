import pandas as pd
import numpy as np

# Number of records
n = 1000

# Generate random investor IDs, syndicate IDs, transaction amounts, and transaction dates
np.random.seed(0)
investor_ids = np.random.randint(1, 101, n)  # 100 unique investors
syndicate_ids = np.random.randint(1, 21, n)  # 20 unique syndicates
transaction_amounts = np.random.uniform(1000, 50000, n)  # Transaction amount between 1000 and 50000
transaction_dates = pd.date_range(start='1/1/2020', periods=n).to_pydatetime().tolist()  # Dates from 01-01-2020
np.random.shuffle(transaction_dates)  # Shuffle the dates

# Create a DataFrame
df = pd.DataFrame({
    'investor_id': investor_ids,
    'syndicate_id': syndicate_ids,
    'transaction_amount': transaction_amounts,
    'transaction_date': transaction_dates
})

# Write the DataFrame to a CSV file
df.to_csv('task1/dummy_data.csv', index=False)
print("Dummy data generated and saved to 'dummy_data.csv'.")
