#!/usr/bin/env python

from random import choice
import sys
if __name__ == '__main__':
    arg = sys.argv[1:]
    thing2blame = ''.join(e for e in arg if e.isalnum())
    if len(thing2blame) > 0:
        print "DAMMIT, {0}!".format(thing2blame)
    else:
        people2blame = ['nobody\'s fault, shit happens', 'vyizis', 'cptprime', 'cahbtexhuk', 'M0XIN', 'tgreer', 'the Computer. Do you secretly hate the Computer, citizen?']
        person = choice(people2blame)
        # person = 'tgreer'
        print "It was {0}".format(person)