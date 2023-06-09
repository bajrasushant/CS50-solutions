import csv
import sys
import re


def main():
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
    # TODO: Check for command-line usage
    if len(sys.argv) != 3:
        print("Error: Try Again")
        sys.exit(1)

    else:

    # TODO: Read database file into a variable
        file_db = open(sys.argv[1], "r")
        db_reader = csv.DictReader(file_db)

    # TODO: Read DNA sequence file into a variable
        file_sequence = open(sys.argv[2], "r")
        sq_reader = csv.reader(file_sequence)

    # TODO: Find longest match of each STR in DNA sequence
        data = file_sequence.read().rstrip('\n')
        for i in dna_types:  # searching the dna types in data
            # num_occurence = data.count(i)  # returns number of occurence of i(dna types)
            # max_run = i * num_occurence  # max number of occurance of i ie ABABAB if 3 AB repetition but different places
            # while (max_run not in data):  # update if ABABAB even though is the number of occurence but not simulataneous
            #     num_occurence -= 1
            #     max_run = i * num_occurence
            # exits loop when consecutive repetition is found.
            # dna[i] = num_occurence
            dna[i] = longest_match(data, i)

    # TODO: Check database for matching profiles
        count = 0
        for line in db_reader:
            for i in dna_types:
                if i in line:
                    to_comp = line[i]
                    if int(to_comp) == int(dna[i]):
                        count += 1
                        if count == (len(line) - 1):
                            print(line["name"])
                            return
                    else:
                        count = 0
                        continue
                else:
                    continue
        print("No match")
        return
        

def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):

        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of consecutive matches
        while True:

            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1

            # If there is no match in the substring
            else:
                break

        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in seqeuence, return longest run found
    return longest_run


main()
