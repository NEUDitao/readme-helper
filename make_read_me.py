#!/usr/bin/env python

"""Helps newer software developers make a readme for their project"""

__author__ = 'Edward Li'
__email__ = 'li.edwa@husky.neu.edu'

import sys
import time


def read_with_code() -> str:
    """Reads in input that's meant to have code blocks in it"""
    print(
        """\nWrite your text block for the section below!
(hint, you can write inline code blocks using "`" marks, and you can write
blocks of code by surrounding what you want to write with "```". Try to keep
your inline code blocks on one line though!)
|------------------------------------------------------------------------------|
""")
    return sys.stdin.read()


def sec_title(default_str: str) -> str:
    """Reads in a section title"""
    name = input('What would you like to title this section? '
                 + '(default is', default_str, '\n')
    if name:
        return name
    return default_str


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
EOF object my way (press CTRL + D)!

Oh, and please be careful with line length. Anything over 80 characters will be
wrapped for you, but that means it'll probably not look so hot on GitHub's 
preview page. 80 characters is the width of a standard terminal. Just try not to
make it longer than the following line.
|------------------------------------------------------------------------------|
""")

descr = sys.stdin.read()


print("\nCool, now that we're done with setting up, we can get to "
      + "the nitty gritty")

time.sleep(1)

while(True):
    print("\nEnter a letter to edit a section:, or EXIT to save and exit")
    print("""1. Installation
2. Usage
3. Examples
4. Technologies Used (Built with)
5. How to contribute
6. Version information
7. Authors
8. Acknowledgements
9. License/Copyright
0. Edit previous fields
EXIT. Exit""")
    option = input()
    install, usage, ex, techs, contr, version, authors, ackn, lic = ('','',
                                                                     '','','',
                                                                     '','','',
                                                                     '')
    if option == 'EXIT':
        print('Thank you for using my tool!')
# TODO        save_file()
        print('Your file is saved at', file_name)
        print('Bye bye!\n\n')
        break

    elif option == '1':        
        install_name = sec_title('Installation')

        install = read_with_code()
        print(install_name, 'instructions complete!\n')

    elif option == '2':
        usage_name = sec_title('How to Use')

        usage = read_with_code()
        print(usage_name, 'instructions complete!\n')

    elif option == '3':
        ex_name = sec_title('Examples')

        ex = read_with_code()
        print(ex_name, 'instructions complete!\n')

    elif option == '4':
        techs_name = sec_title('Built With')

        techs = read_with_code()
        print(techs_name, 'instructions complete!\n')

    elif option == '5':
        contr_name = sec_title('Contribute')

        contr = read_with_code()
        print(contr_name, 'instructions complete!\n')

    elif option == '6':
        version_name = sec_title('Version History')

        version = read_with_code()
        print(contr_name, 'instructions complete!\n')

    elif option == '7':
        authors_name = sec_title('Authors')

        author = read_with_code()
        print(contr_name, 'instructions complete!\n')

    elif option == '8':
        ackn_name = sec_title('Acknowledgements')

        ackn = read_with_code()
        print(ackn_name, 'instructions complete!\n')

    elif option == '9':
        pass

    elif option == '10':
        pass

    else:
        print('\n\u001b[31;1mInvalid input, try again\u001b[31;0m')
