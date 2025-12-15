"""
consumer.py
----------------
This file contains the logic for a Consumer that continuously reads messages
from the queue and processes them.

The Consumer runs forever, just like a streaming system.
"""

import time
from queue import Queue
from collections import defaultdict


class Consumer:
    def __init__(self, q):
        """
        PARAMETERS:
        - q : the shared queue (simulated topic)

        TODO:
        - Store the queue.
        - Initialize any state variables you may want later,
          e.g. a running total for stateful computations.
        """
        self.q = q
        # now i want to add aggregation so
        self.running_total = 0.0
        self.count = 0
        self.amount_per_user = defaultdict(float)
        self.count_per_user = defaultdict(int)

    def start(self):
        """
        Main loop of the consumer.

        TODO:
        - Continuously call q.get() to receive events.
        - Print the event received.
        - Pass it to the process() function. # process() is a placeholder for now 
        """
        while True:
            event = self.q.get()
            print(f"Received event: {event}")
            self.process(event)

    def process(self, event):
        """
        TODO:
        - Simulate some processing time using time.sleep().
        - Transform fields (e.g., convert amount to float).
        - Implement optional filtering conditions.
        - Update any state (example: running total).
        """
        # time.sleep(0.5)
        # if 'amount' in event:
        #     event['amount'] = float(event['amount'])
        #     # optional filttering my amount>
        #     if event['amount'] > 400:
        #         print(f"High value transaction detected: {event}")
        #     # update running total
        #     event['running_total'] = event['amount']
        time.sleep(0.5)

        if "amount" not in event:
            return

        # Convert amount
        try:
            amount = float(event["amount"])
        except ValueError:
            print(f"Invalid amount: {event['amount']}")
            return

        event["amount"] = amount

        # Optional filtering
        if amount > 400:
            print(f"High value transaction detected: {event}")

        # Update global aggregates
        self.running_total += amount
        self.count += 1

        # Update per-user aggregates
        user = event.get("user_id", "UNKNOWN")
        self.amount_per_user[user] += amount
        self.count_per_user[user] += 1

        # Print live streaming metrics
        print("AGGREGATION")
        print(f"Total events: {self.count}")
        print(f"Total amount: {self.running_total:.2f}")
        print(f"Average amount: {self.running_total / self.count:.2f}")
        print(f"User {user} total: {self.amount_per_user[user]:.2f}")

# Debugging test


if __name__ == "__main__":
    """
    Run this alone to see consumer behavior.

    Note: It will block waiting for messages since no producer is running.
    """
    q = Queue()
    consumer = Consumer(q)
    consumer.start()
