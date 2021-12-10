import csv
import numpy as np

file = open("../data/article_archive_all_9_12_10am_cat.csv", encoding='utf8')
csvreader = csv.reader(file)
header = next(csvreader)
zpravy_csv = []
for row in csvreader:
    zpravy_csv.append(row)
file.close()

pom = zpravy_csv[0]

zpravy = [
    {'id': 0, header[1]:  pom[1], header[2]: pom[2], header[3]: pom[3], header[4]: pom[4], header[5]: pom[5], header[6]: pom[6], header[7]: pom[7]}
        ]

for i in range(1,np.size(zpravy_csv,0)):
    pom = zpravy_csv[i]
    zpravy.append({'id': i, header[1]:  pom[1], header[2]: pom[2], header[3]: pom[3], header[4]: pom[4], header[5]: pom[5], header[6]: pom[6], header[7]: pom[7]})
