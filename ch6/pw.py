#! python3
# pw.py - Password locker

PASSWORDS = {'email': '{#C1~YDGvW+".$D',
             'Github': '9,#munRDtKM^J-x',
             'Twitter': '=Hw`VsVZEUv+\2@'}

import sys, pyperclip

if len(sys.argv) < 2:
    print('Usage: python pw.py [account] - copy account password')
    sys.exit()

account = sys.argv[1]  # first command line arg is the account name

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print('Password for ' + account + ' copied to clipboard.')
else:
    print('There is no account named ' + account)

