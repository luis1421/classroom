##Open file
f = open('C:\\Users\\USUARIO\\OneDrive\\Documentos\\VS\\EACD-01-FUNDAMENTOS\\local\\files\\abstract.txt', 'r')
#Read all lines
content = f.readlines()
#Close file
f.close()
print(content)


f = open("C:\\Users\\USUARIO\\OneDrive\\Documentos\\VS\\EACD-01-FUNDAMENTOS\\local\\files\\abstract.txt", "r")
content = []
line = "some arbitrary string to enter the loop"
while line != "":
    line = f.readline()
    content.append(line)
f.close()
print(content)

#Line by line
f = open("C:\\Users\\USUARIO\\OneDrive\\Documentos\\VS\\EACD-01-FUNDAMENTOS\\local\\files\\abstract.txt", "r")
content = []
line = "some arbitrary string to enter the loop"
while line != "":
    line = f.readline()
    if line !="":
        content.append(line)
f.close()
print(content)

#Read as a string
f = open("C:\\Users\\USUARIO\\OneDrive\\Documentos\\VS\\EACD-01-FUNDAMENTOS\\local\\files\\abstract.txt", "r")
content = f.read()
f.close()
print(content)

##Context manager
#nos proporciona la seguridad de que siempre nos estamos refiriendo 
#al mismo archivo y lo cierra para que otros procesos lo utilicen de ser necesario
with open("C:\\Users\\USUARIO\\OneDrive\\Documentos\\VS\\EACD-01-FUNDAMENTOS\\local\\files\\abstract.txt", "r") as f:
    content = f.readlines()
print(content)

##CSV files
import csv
with open('C:\\Users\\USUARIO\\OneDrive\\Documentos\\VS\\EACD-01-FUNDAMENTOS\\local\\data\\demodata.csv', 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row)
#Write file
data = [
    {"name": "julanito", "grade": 3.7},
    {"name": "peranito", "grade": 3.3}
]
with open("temp.csv", mode="w") as f:
    writer = csv.DictWriter(f, fieldnames=["name", "grade"])
    writer.writeheader()
    for row in data:
        writer.writerow(row)

##JSON
import json
#Read
with open('C:\\Users\\USUARIO\\OneDrive\\Documentos\\VS\\EACD-01-FUNDAMENTOS\\local\\files\\coco_example.json', 'r') as f:
    data = json.load(f)
print(data)

#Write
data = [
    {"name": "julanito", "grade": 3.7},
    {"name": "peranito", "grade": 3.3}
]
with open("data.json", "w") as f:
    json.dump(data, f)
    