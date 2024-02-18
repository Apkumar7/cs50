import csv
import sys

longest_sequence = {}


def main():
    # TODO: Check for command-line usage
    if len(sys.argv) != 3:
        print("INVALID USAGE!!!!!")
        sys.exit(1)

    # TODO: Read database file into a variable
    databasefile = open(sys.argv[1], "r")
    database = csv.DictReader(databasefile)
    database2 = csv.reader(databasefile)

    # TODO: Read DNA sequence file into a variable
    sequencefile = open(sys.argv[2], "r")
    sequence = sequencefile.read()

    # TODO: Find longest match of each STR in DNA sequence
    databasefile.seek(0)
    for i in database2:
        subvalue = i[1:]
        break
    for i in subvalue:
        longest_sequence[i] = longest_match(sequence, i)

    # TODO: Check database for matching profiles
    databasefile.seek(0)
    for i in database:
        match = False
        for key in longest_sequence:
            if str(longest_sequence[key]) == i[key]:
                match = True
            else:
                match = False
                break
        if match:
            print(i["name"])
    if match == False:
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
