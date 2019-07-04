#!/usr/bin/env python

import sys
from glob import glob
from os import system
from os.path import basename
from os.path import splitext

pandoc = "C:\\Users\\efucile\\AppData\\Local\\Pandoc\\pandoc.exe"

docxDir = "../docx"
outType = sys.argv[1]
outDir = "../" + outType
conversion = " --wrap=none --atx-headers --extract-media=" + outDir + "/extracted-media -o "


docxFilenames = [f for f in glob(docxDir + "/*.docx")]

for docxFilename in docxFilenames:
    outFilename = outDir + "/" + splitext(basename(docxFilename))[0] + "." + outType
    command = pandoc + conversion + outFilename +" "+docxFilename
    print(command)
    system(command)
