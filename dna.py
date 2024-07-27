import csv
import sys

#Information To Help Me:
#Hints: Reader and DictReader
#Sys.argv like argv in C
#Open(filename) is the equivalent of fread()

#WHAT I WROTE

def main():

    # TODO: Check for command-line usage
    if len(sys.argv) != 3:
        sys.exit("Incorrect input")
    # TODO: Read database file into a variable
    memorie = []
    with open(sys.argv[1], 'r') as file:
        read = csv.DictReader(file)
        for row in read:
            memorie.append(row)
    # TODO: Read DNA sequence file into a variable
    with open(sys.argv[2], 'r') as file:
        dna_sequence = file.read()
    # TODO: Find longest match of each STR in DNA sequence
    subsequences = list(memorie[0].keys())[1:]
    rez = {}
    for sub in subsequences:
        rez[sub] = longest_match(dna_sequence, sub)
    # TODO: Check database for matching profiles
    subsequences = list(memorie[0].keys())[1:]

    rez = {}
    for sub in subsequences:
        rez[sub] = longest_match(dna_sequence, sub)

    # TODO: Check database for matching profiles
    for person in memorie:
        match = 0
        for sub in subsequences:
            if int(person[sub]) == rez[sub]:
                match += 1
        if match == len(subsequences):
            print(person["name"])
            return

    print("No match")

    return


#WHAT CS50 WROTE

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
