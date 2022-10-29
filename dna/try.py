dna_types = ["AGATC", "TTTTTTCT", "AATG", "TCTAG", "GATA", "TATC", "GAAA", "TCTG"]
dna = {
    "AGATC": 0,
    "TTTTTTCT": 0,
    "AATG": 0,
    "TCTAG": 0,
    "GATA": 0,
    "TATC": 0,
    "GAAA": 0,
    "TCTG": 0
}
data = "AAGGTAAGTTTAGAATATAAAAGGTGAGTTAAATAGAATAGGTTAAAATTAAAGGAGATCAGATCAGATCAGATCTATCTATCTATCTATCTATCAGAAAAGAGTAAATAGTTAAAGAGTAAGATATTGAATTAATGGAAAATATTGTTGGGGAAAGGAGGGATAGAAGG"
for i in dna_types:
    num_occurence = data.count(i)
    max_run = i * num_occurence
    while (max_run not in data):
        num_occurence -= 1
        max_run = i * num_occurence

    dna[i] = num_occurence
print(dna)