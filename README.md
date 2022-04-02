# Enron_Project
This project collects, filters, aggregates, explores, and visualizes data from a large collection of enron email files.

## Tools: Networkx, Python, Feather

## Data: 
1.7G worth of Enron email messages 
## Steps:
(Code.py)
* Extract "Subject", "Sender", "Receipients", "Date" from each email message
* Normalize the "Receipients" email addresses and filter out the ones not within Enron organization
(Enron.pdf)
* Get first 5000 Data (sort by Date) of the previous step
* Explore email traffic and connection by different plots
