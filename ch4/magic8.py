# -*- coding: utf-8 -*-
"""
Created on Sun Feb 14 22:11:14 2016

@author: Rob
"""

import random

messages = ['It is certain', 
            'It is decidedly so',
            'Yes definitely',
            'Reply hazy try again',
            'Ask again later',
            'Concentrate and ask again',
            'My reply is no',
            'Outlook not so good',
            'Very doubtful']

print(messages[random.randint(0, len(messages) -1)])

