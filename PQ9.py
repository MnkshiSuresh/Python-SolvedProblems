#Write a Python program to check if every consecutive sequence of zeroes is followed by a consecutive sequence of ones of same length in a given string. Return True/False.
#Original sequence: 01010101
#Check if every consecutive sequence of zeroes is followed by a consecutive sequence of ones in the said string:
#True
#Original sequence: 00
#Check if every consecutive sequence of zeroes is followed by a consecutive sequence of ones in the said string:
#False
#Original sequence: 000111000111
#Check if every consecutive sequence of zeroes is followed by a consecutive sequence of ones in the said string:
#True
#Original sequence: 00011100011
#Check if every consecutive sequence of zeroes is followed by a consecutive sequence of ones in the said string:
#False




def functionzero(data):
    countzero = 0
    countone = 0

    for i in range(len(data)):
        if data[i] == '0':
            countzero += 1
        elif data[i] == '1':
            countone += 1

        # Check if there's a transition from 1 to 0
        if i > 0 and data[i - 1] == '1' and data[i] == '0':
            if countzero == countone:
                return "no"
            else:
                return "yes"

    # If there's no transition from 1 to 0
    if countzero == countone:
        return "no"
    else:
        return "yes"

print("Enter a sequence separated by space:")
sequence = input("Enter here: ")
data = sequence.split()

if data[0] == '0':
    print(functionzero(data))

