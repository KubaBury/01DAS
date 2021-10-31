import numpy as np
import pandas as pd 
import csv


file = open("article_archive.csv")
csvreader = csv.reader(file)
header = next(csvreader)
print(header)
zpravy_csv = []
for row in csvreader:
    zpravy_csv.append(row)
file.close()

pom = zpravy_csv[0]   

zpravy = [
    {'id': pom[0], header[1]:  pom[1], header[2]: pom[2], header[3]: pom[3], header[4]: pom[4], header[5]: pom[5], header[6]: pom[6], header[7]: pom[7], header[8]: pom[8]}
    ]


for i in range(1,np.size(zpravy_csv,0)):
    pom = zpravy_csv[i]
    zpravy.append({'id': pom[0], header[1]:  pom[1], header[2]: pom[2], header[3]: pom[3], header[4]: pom[4], header[5]: pom[5], header[6]: pom[6], header[7]: pom[7], header[8]: pom[8]})