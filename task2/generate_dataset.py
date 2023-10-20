import csv
import random

# Define the number of transactions and range of amounts
#To Throw no Alert
# num_transactions = 5
# min_amount = 1
# max_amount = 9000

#To Throw Alert
num_transactions = 1000
min_amount = 1
max_amount = 15000

# Generate random transactions
transactions = [random.uniform(min_amount, max_amount) for _ in range(num_transactions)]

# Write transactions to a CSV file
with open('task2/transactions.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Amount'])  # Write header
    for transaction in transactions:
        writer.writerow([transaction])
