'''
AMU-lator

by David Gallivan

A program to calculate the molar mass of chemicals
Quick & dirty

Requires amus.txt

Cannot parse parentheses - just repeat ions!
'''
def main():
    amufile = open("amus.txt")
    data = dict()
    for line in amufile.readlines():
        thisline = line.split();
        data[str(thisline[1])] = float(thisline[3])
    #print(data)

    elements = []
    elemcount = 0
    formula = input("Enter a chemical formula: ")
    for char in formula:
        if char.isdigit(): #note that this will fail for two-digit numbers
            for i in range(1,int(char)):
                elements.append(elements[-1])
        elif char.isupper():
            index = formula.index(char)
            elements.append(char)
            elemcount += 1
        elif char.islower():
            elements[-1] += char
    print(elements)

    molar_mass = 0
    for elm in elements:
        molar_mass += data[elm]
    input(molar_mass)
main()