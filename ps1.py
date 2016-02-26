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
    lead writer:
    

    what it does:
    
    
    Expected arguments:
    
    """


def checkword(s):
    """
    lead writer:
    

    what it does:
    
    
    Expected arguments:
    
    """

    
    