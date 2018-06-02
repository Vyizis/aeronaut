#!/usr/bin/env python

from random import choice
import sys
if __name__ == '__main__':
    print len(sys.argv)
    print sys.argv
    if len(sys.argv) >= 2:
        thing2blame = sys.argv[1:]
	print thing2blame
        newstr = ''.join(e for e in thing2blame if e.isalnum())
	print newstr
        print "DAMMIT, {0}!".format(newstr)
    else:
	print "elseflag"
        people2blame = ['nobody\'s fault, shit happens', 'vyizis', 'cptprime', 'cahbtexhuk', 'M0XIN', 'tgreer', 'the Computer. Do you secretly hate the Computer, citizen?']
        print people2blame
	person = choice(people2blame)
	print person
        print "It was {0}".format(person)
