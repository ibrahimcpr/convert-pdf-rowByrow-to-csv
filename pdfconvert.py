from tika import parser # pip install tika
import csv
raw = parser.from_file('pdf.pdf')
pdf=str(raw['content'])
cols=pdf.split('\n')
with open('shows.csv', 'w',newline='') as f:
    write = csv.writer(f)
    for item in cols:
        write.writerow([item])
