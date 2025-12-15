# Lab 1: Python Streaming Lab — Producer & Consumer Using CSV

In this lab, you will build a **simple streaming system** using only Python standard libraries.

Instead of processing data all at once, you will process events **one by one as they arrive**, simulating a real-time data stream.

---

## What Are We Building?

We are building a **producer–consumer pipeline**:

- A **Producer** reads data from a CSV file and emits events gradually
- A **Consumer** receives events and processes them immediately
- A **Queue** is used to pass events safely between components
- **Threads** allow the producer and consumer to run at the same time

---

## Project Structure


- producer.py → Reads CSV rows and streams them into a queue
- consumer.py → Reads and processes events
- pipeline.py → Runs producer + consumer simultaneously
- transactions.csv →  CSV file

---

##  Why Do We Use Threads?

In a streaming system:
- Data is produced and consumed **simultaneously**
- The producer should not wait for the consumer (and vice versa)

Threads allow both components to run **in parallel**, making the system behave like a real streaming pipeline.

---

## Why Do We Use a Queue?

The queue is the **communication channel** between the producer and the consumer.

It:
- Transfers events safely between threads
- Blocks the consumer when no data is available
- Ensures events are processed in order

---

## How the Pipeline Works

1. `pipeline.py` creates a shared queue  
2. The producer reads one row from the CSV and sends it to the queue  
3. The consumer waits for events and processes them immediately  
4. This continues until all CSV rows are consumed  

---

## How to Run the Lab

Run the full pipeline:

```bash
python pipeline.py
```

You should see events being produced and consumed in real time.

---

## What You Will Learn

- How streaming differs from batch processing

- The producer–consumer pattern

- How concurrency works using threads

- How events can be processed in real time

-> This lab prepares you for more advanced streaming tools later in the course.
