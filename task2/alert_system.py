import heapq
from collections import deque
import random
import time
import csv

class SlidingWindow:
    def __init__(self, window_size=3600):
        self.window_size = window_size
        self.transactions = deque()

    def add(self, transaction):
        self.transactions.append((transaction, time.time()))

        # Remove transactions outside the window
        while time.time() - self.transactions[0][1] > self.window_size:
            self.transactions.popleft()

    def count(self):
        return len(self.transactions)

    def average(self):
        return sum(t[0].amount for t in self.transactions) / len(self.transactions)


class PriorityQueue:
    def __init__(self):
        self.queue = []

    def add(self, transaction):
        # Use a negative amount to get a max-heap
        heapq.heappush(self.queue, (-transaction.amount, transaction))

    def get_all(self):
        return [(t[1], -t[0]) for t in sorted(self.queue)]

class Transaction:
    def __init__(self, amount):
        self.amount = amount

class AlertSystem:
    def __init__(self, threshold, spike_rate):
        self.threshold = threshold
        self.spike_rate = spike_rate
        self.transactions = SlidingWindow()
        self.alerts = PriorityQueue()

    def process_transaction(self, transaction):
        if transaction.amount > self.threshold:
            self.alerts.add(transaction)
        avg = 0
        if self.transactions.count() > 0:
            avg = self.transactions.average()
        self.transactions.add(transaction)
        # print(f"transactions.count: {self.transactions.count()}")
        # print(f"transactions.spike_rate*avg: {self.spike_rate * self.transactions.average()}")
        if self.transactions.count() > self.spike_rate * avg:
            self.alerts.add(transaction)
            print("Spike Alert: Detected a sudden spike in transactions")

    def get_alerts(self):
        return self.alerts.get_all()


# Create an instance of AlertSystem
alert_system = AlertSystem(threshold=10000, spike_rate=10)

# Read transactions from a CSV file and process them
with open('task2/transactions.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader)  # Skip the header row
    for row in reader:
        amount = float(row[0])  # Assuming the amount is in the first column
        alert_system.process_transaction(Transaction(amount))

# Generate normal transactions
for _ in range(100):
    alert_system.process_transaction(Transaction(random.uniform(1, 5000)))

# Generate a spike in transactions
for _ in range(2000):
    alert_system.process_transaction(Transaction(random.uniform(1, 5000)))

# Get alerts
alerts = alert_system.get_alerts()
for alert in alerts:
    print(f"Alert: Transaction of amount {alert[1]} triggered an alert")
