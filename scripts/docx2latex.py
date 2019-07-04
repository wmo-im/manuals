#!/usr/bin/env python

import sys
import string
from glob import glob
from os import system
from os import listdir
from os.path import basename
from os.path import splitext

pandoc = "C:\\Users\\efucile\\AppData\\Local\\Pandoc\\pandoc.exe"
docxDir = sys.argv[1]
adocDir = sys.argv[2]

docxFilenames = [f for f in glob(docxDir + "/*.docx")]

for docxFilename in docxFilenames:
    outFilename = adocDir + "/" + splitext(basename(docxFilename))[0] + ".tex"
    system(pandoc + " --from=docx --to=latex --wrap=none --atx-headers \
    --extract-media=extracted-media \
    -o "+outFilename +" "+docxFilename)
