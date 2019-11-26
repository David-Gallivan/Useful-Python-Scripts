'''+JMJVSS

Fibonacci's greedy Egyptian fraction expansion algorithm

by David Gallivan
'''
from math import ceil

#gcd
#
#returns the greatest common denominator of two integers
#source: https://codereview.stackexchange.com/questions/66450/simplify-a-fraction
def gcd(a, b):
    """Calculate the Greatest Common Divisor of a and b.
    Unless b==0, the result will have the same sign as b (so that when
    b is divided by it, the result comes out positive).
    """
    while b:
        a, b = b, a % b
    return a

#simplify_fraction
#
#takes two ints, a numerator and a denominator
#reduces a fraction to the lowest possible terms
#returns a tuple of the reduces numerator and denominator
#source: https://codereview.stackexchange.com/questions/66450/simplify-a-fraction
def simplify_fraction(numer, denom):
    if denom == 0:
        return "Division by 0 - result undefined"

    # Remove greatest common divisor:
    common_divisor = gcd(numer, denom)
    (reduced_num, reduced_den) = (numer / common_divisor, denom / common_divisor)
    # Note that reduced_den > 0 as documented in the gcd function.

    return(int(reduced_num), int(reduced_den))

#FibEFE
#
#takes two integers, a numerator and a denominator
#performs Fibonacci's greedy algorithm for an Egyptian fraction expansion
#returns the fraction expansion as a string
def FibEFE(num, denom):
    string = ''
    (num, denom) = simplify_fraction(num, denom)
    if num == 1:
        string += '1 / ' + str(denom)
        return string
    else:
        firstTermDenom = int(ceil( float(denom) / float(num) ))
        string += '1 / ' + str(firstTermDenom) + '   +   '
        newFracNumerator = ( (- denom) % num )
        newFracDenominator = ( denom * int(ceil( float(denom) / float(num))) )
        #The New Fraction needs reduced!
        newFracNumerator, newFracDenominator = simplify_fraction(newFracNumerator, newFracDenominator)
        return string + FibEFE(newFracNumerator, newFracDenominator) #Recursion

def main():
    while(1):
        print("Give a fraction to expand or 'q' to quit")
        x = input("Numerator:   ")
        if x=='q' or x=='Q':
            print("Ciao")
            break
        if not x.isdigit() or int(x)<1:
            print("only positive integers please!")
            continue

        y = input("Denominator: ")
        if y=='q' or y=='Q':
            print("Ciao")
            break
        if not y.isdigit() or int(y)<1:
            print("only positive integers please!")
            continue

        print( FibEFE(int(x),int(y)) )
main()
