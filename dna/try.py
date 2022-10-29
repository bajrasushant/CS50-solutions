import csv
from sys import exit

dna_types = ["AGATC", "TTTTTTCT", "AATG", "TCTAG", "GATA", "TATC", "GAAA", "TCTG"]
dna = {
    "AGATC": 2,
    "TTTTTTCT": 0,
    "AATG": 8,
    "TCTAG": 0,
    "GATA": 0,
    "TATC": 3,
    "GAAA": 0,
    "TCTG": 0
}
data = "AAGGTAAGTTTAGAATATAAAAGGTGAGTTAAATAGAATAGGTTAAAATTAAAGGAGATCAGATCAGATCAGATCTATCTATCTATCTATCTATCAGAAAAGAGTAAATAGTTAAAGAGTAAGATATTGAATTAATGGAAAATATTGTTGGGGAAAGGAGGGATAGAAGG"

file = open("databases/small.csv", "r")
reader = csv.DictReader(file)

count = 0

for line in reader:
    for i in dna_types:
        if (i in line):
            # print(i)
            # print(line)
            to_comp = line[i]
            # print(to_comp)
            # print(dna[i])
            if (int(to_comp) == int(dna[i])):
                count += 1
                # print(count)
                if count == len(line) - 1:
                    print(line["name"])
                    exit(0)
        else:
            continue

file.close()