# -*- coding: utf-8 -*-
"""
Problem Set 1

Authors:

    checkpalindrome(s): Victoria Sardelli
    v2na(verb):
    checkword(s):

Submission Month and Year:
    February 2016
"""

import string


def checkpalindrome(s):
    """
    lead writer:
        Victoria Sardelli

    what it does:
        Takes a string as input and prints out whether or not it's a palindrome
        Disregards capitalization, spaces, and punctuation

    Expected arguments:
        s - string
    """

    # get string and strip whitespace
    s1 = s.replace(" ","")

    # get rid of punctuation
    exclude = set(string.punctuation)
    s1 = "".join(ch for ch in s1 if ch not in exclude)

    # capitalize all letters in string
    s1 = s1.upper()

    # split string into two halves for comparison
    half = len(s1)//2
    if len(s1) % 2 == 0:
        sLeft = s1[:half]
    else:
        sLeft = s1[:half+1]
    sRight = s1[half:]
    sRight = sRight[::-1] #flip it around

    if sLeft == sRight:
        print("\"" + s + "\" is a palindrome!\n")
    else:
        print("\"" + s + "\" is not a palindrome.\n")


def v2na(verb):
    """
    lead writer: Mike Nolan
    what it does:
    Expected arguments: verb: string
    """
    root = verb[:-3] # cuts off 'ity'
    if root[-2] == 'i':
        root = root + 'e'
    print(root)

def checkword(s):
    """
    lead writer: Zach Sherman
    what it does: Various operations on a string.
    Expected arguments: A string named s.
    """
    
    sLowercase = s.lower()
    # Does it begin with a vowel? Or a consonant?
    if sLowercase[0] == "a" or sLowercase[0] == "e" or sLowercase[0] == "i" or sLowercase[0] == "o" or sLowercase[0] == "u":
        print("Begins with a vowel.")
    else:
        print("Does not begin with a vowel. Sorry about that.")

    # How long is the word in number of characters?
    stringLength = len(s)
    print("The length of this string is " + str(stringLength))

    # How many letters <e> does the word have? If there are two, are they adjacent?
    eCounter = 0
    lastIndex = 0
    isAdjacent = False
    while True:
        eLocation = sLowercase.find("e", lastIndex)
        if eLocation != -1:
            if eLocation == lastIndex:
                isAdjacent = True
            eCounter += 1
            lastIndex = eLocation + 1

        else:
            break

    print("The number of e's within the string is equal to " + str(eCounter))
    if isAdjacent:
        print("There are adjacent e's in this string.")

    else:
        print("There are no adjacent e's in this string.")

    # Does the word end in the noun morphemes <ality> or <fest>?
    if sLowercase[-5:] == "ality":
        print("This word ends in 'ality.'")
    elif sLowercase[-4:] == "fest":
        print("This word ends in 'fest.'")
    else:
        print("This word does not end in 'ality' or 'fest.'")

    # Is the word a multiword expression (eg. hot dog or two-year-old)?
    sMultiword = sLowercase.find(" ") != -1
    if sMultiword:
        print("This is a multiword expression.")
    else:
        print("This is not a multiword expression.")

    # Is the word likely a proper name (eg. of a person, place, or organization)?
    intFirstLetter = ord(s[0])
    if intFirstLetter >= 65 and intFirstLetter <= 90:
        print("This word is capitalized and probably a proper name.")
    else:
        print("This word is not capitalized, so I am assumming it is not a proper name. Great.")




