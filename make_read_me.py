#!/usr/bin/env python

"""Helps newer software developers make a readme for their project"""

__author__ = 'Edward Li'
__email__ = 'li.edwa@husky.neu.edu'

import sys
import time

print('Welcome to the \u001b[31;1mR\u001b[32;1mE\u001b[33;1mA'
      + '\u001b[34;1mD\u001b[35;1mM\u001b[36;1mE \u001b[31;1mm'
      + '\u001b[32;1ma\u001b[33;1mk\u001b[34;1me\u001b[35;1mr'
      + '\u001b[36;1m!\n')

file_name = input('\u001b[0;1mTo get started, where would you like to store'
                  + ' your file? (default is README.md)\n')

if file_name:
    pass
else:
    file_name = 'README.md'

print('Alright, cool, your file will be stored at ' + file_name)

time.sleep(1)

title = input('\n\nNow, what is the title of your project?\n')

while not title:
    title = input('\n\nYou seemed to input an empty string... try again:\n')

title = '# ' + title

print('Got it! You can change these at any time later on too.')

time.sleep(1)

print(
    """\n\nOne last thing... can you describe your project? For instance, 
describe what your project does, what it's based off of, and if it exists,
what other project inspired you to make it. If you want to add a link, just
do [NAME](URL) for wherever you want to stick it) When you're done, send an
EOF object my way (press CTRL + D)!\n""")

descr = sys.stdin.read()


print("\nCool, now that we're done with setting up, we can get to "
      + "the nitty gritty")

time.sleep(1)

print("\nEnter a letter/number to edit a section:")
print("""1. Installation
2. Usage
3. Examples
4. Technologies Used (Built with)
5. How to contribute
6. Version information
7. Authors
8. Acknowledgements
9. License/Copyright
0. Edit file name or title of project and exit""")
