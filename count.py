# most_frequent function
from collections import Counter

def most_frequent(s):
    counter=Counter(s)
    return counter

s=input("Please enter a string: " )

print(most_frequent(s))
