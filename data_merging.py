import csv

dataset_1 = []
dataset_2 = []

#encoding can translate unique code character to a matching unique binary string
with open('dwarf_stars.csv', 'r') as f:
    csvreader = csv.reader(f)
    for row in csvreader:
        dataset_1.append(row)

with open('bright_stars.csv', 'r') as f:
    csvreader = csv.reader(f)
    for row in csvreader:
        dataset_2.append(row)

headers_1 = []
headers_1.append(dataset_1[0])
star_data_1 = dataset_1[1:]

headers_2 = []
headers_2.append(dataset_2[0])
star_data_2 = dataset_2[1:]

headers = headers_1 + headers_2

#solar_radius = dataset_1[3] * int(0.102763)
#solar_mass = dataset_1[2] * int(0.000954588)

#headers_1.append(solar_mass + solar_radius)
star_data = []

for i in star_data_1:
    star_data.append(i)

for j in star_data_2:
    star_data.append(i)

#for index, data_row in enumerate(star_data_1):
    #star_data.append(star_data_1[index]+star_data_2[index])

with open('merge_dataset.csv', "a+") as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(headers)
    csvwriter.writerows(star_data)