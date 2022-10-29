import csv

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

file = open("small.csv", "r")
reader = csv.DictReader(file)

count = 0
for line in reader:
    for i in dna_types:
        to_comp = line[i]
        if (to_comp == dna[i]):
            count += 1
    if count == len(line):
        print(line["name"])
    else:
        continue

file.close()