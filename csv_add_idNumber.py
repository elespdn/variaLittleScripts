import csv

with open("addIDnumber.csv", 'r') as input, open('addedIDnumber.csv', 'w') as output:
    reader = csv.reader(input, delimiter = ',')
    writer = csv.writer(output, delimiter = ',')

    all = []
    row = next(reader)
    row.insert(0, 'ID')
    all.append(row)
    count = 530
    for row in reader:
        count += 1
        row.insert(0, count)
        all.append(row)
    writer.writerows(all)