#!/usr/bin/env python

from random import choice
import sys
import re
if __name__ == '__main__':
    if len(sys.argv) > 1:
        thing2blame = sys.argv[1:]
        blah = re.sub('\W+','', thing2blame)
        print "DAMMIT, {0}!".format(blah)
    else:
        people2blame = ['nobody\'s fault, shit happens', 'vyizis', 'cptprime', 'cahbtexhuk', 'M0XIN', 'tgreer', 'the Computer. Do you secretly hate the Computer, citizen?']
        person = choice(people2blame)
        print "It was {0}".format(person)
