#!/usr/bin/env python

from random import choice
import sys
if __name__ == '__main__':
    if len(sys.argv[1:]) >= 0:
        thing2blame = sys.argv[1:]
        newstr = ''.join(e for e in thing2blame if e.isalnum())
        print "DAMMIT, {0}!".format(newstr)
    else:
        people2blame = ['nobody\'s fault, shit happens', 'vyizis', 'cptprime', 'cahbtexhuk', 'M0XIN', 'tgreer', 'the Computer. Do you secretly hate the Computer, citizen?']
	person = choice(people2blame)
        print "It was {0}".format(person)
