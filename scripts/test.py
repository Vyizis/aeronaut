#!/usr/bin/env python

import os
print ("This is the name of the script: ", os.environ.get('IRCCAT_COMMAND')))
print ("Number of arguments: ", len(os.environ.get('IRCCAT_ARGS')))
print ("The arguments are: " , str(os.environ.get('IRCCAT_ARGS')))