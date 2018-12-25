'''
This script gets the alias from README
and add them to bashrc to see if it throws an error or not.
'''

README = open("README.md")
ALIAS = ""
FOUND = False

for line in README:
    if FOUND:
        if line.strip() == "```":
            print(ALIAS)
            FOUND = False
        else:
            ALIAS += line
    else:
        if line.strip() == "```sh":
            FOUND = True
            ALIAS = ""

README.close()
