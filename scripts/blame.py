#!/usr/bin/env python

from random import choice
import os
import re
if __name__ == '__main__':
    thing2blame = re.sub(r'\W+', ' ', os.environ.get('IRCCAT_ARGS'))
    if len(thing2blame) > 0:
        print ("DAMMIT, {0}!".format(thing2blame))
    else:
        people2blame = ['nobody\'s fault, shit happens', 'vyizis', 'cptprime', 'cahbtexhuk', 'M0XIN', 'tgreer', 'the Computer. Do you secretly hate the Computer, citizen?']
        person = choice(people2blame)
        # person = 'tgreer'
        print ("It was {0}".format(person))
