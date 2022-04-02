# Enron_Emails_Visualizations
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

## Visualizations:
### Email traffic over time
Histogram showing the overall traffic:
![Goal2](https://github.com/TinaLiu46/Enron-Visualization/blob/master/Images/distribution.png?raw=true "Title")
Histogram showing the overall traffic for richard.shapiro:
![Goal2](https://github.com/TinaLiu46/Enron-Visualization/blob/master/Images/richard_email.png?raw=true "Title")
Histogram showing the overall traffic for john.lavorato:
![Goal2](https://github.com/TinaLiu46/Enron-Visualization/blob/master/Images/john_email.png?raw=true "Title")

### Email heatmap
![Goal2](https://github.com/TinaLiu46/Enron-Visualization/blob/master/Images/heatmap.png?raw=true "Title")

### Plotting graph subsets using NetworkX
![Goal2](https://github.com/TinaLiu46/Enron-Visualization/blob/master/Images/graph.png?raw=true "Title")


