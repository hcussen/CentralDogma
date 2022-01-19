# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
tRNA = {}


def translate(s):
    s = s.upper()
    start = s.find("AUG")

    protein = ""
    while start + 2 < len(s):
        codon = s[start:3]
        protein += tRNA[codon]

    return protein


def getinput():
    print("What is the DNA string? \n Press 1 for DNA -> Protein")
    opt = input()

    if opt == 1:
        s = str(input())
    return s


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    s = getinput()
    print(translate(s))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
