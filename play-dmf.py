#!/usr/bin/env python3

import os

example = '/storage/dosbox/DMFTRACK/'

for root, dirs, files in os.walk(example):
    for file in files:
        if file.endswith('.DMF') or file.endswith('dmf'):
             item = os.path.join(root,file)
             os.system('cvlc --play-and-exit '+item)
             print ('\n\nSound Datei: '+item+'\n')
