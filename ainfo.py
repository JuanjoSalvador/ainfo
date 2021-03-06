#!/usr/bin/env python

import sys
from magic import Magic
from lib import mp3
from lib import flac

# VERSION
VERSION = "0.3-Dev"

BOLD      = '\033[1m'
UNDERLINE = '\033[4m'
END       = '\033[0m'

# Return true if is an audio file
def isAudio(file):
    isAudio = False
    try:
        mime = Magic(mime=True)
        mimetype = mime.from_file(file)
        typeOfFile = mimetype.split("/")
        
        if typeOfFile[0] == "audio":
            isAudio = True
        else:
            print inputFile, "is not a valid file"
    except IOError:
        print inputFile, "is not a valid file or it doesn't exist."
    
    return isAudio

def typeOfAudio(file):
    mime = Magic(mime=True)
    mimetype = mime.from_file(file)
    typeOfFile = mimetype.split("/")

    return typeOfFile[1]
  
def showHelp():
    print BOLD + UNDERLINE + "AudioInfo Tool v" + VERSION + END
    print ""
    print "USAGE"
    print ""
    print "    ainfo <option> /path/to/my.mp3"
    print ""
    print "OPTIONS"
    print ""
    print "    -f      Shows full info about audio file"
    print "    -t      Shows technical info about file"
    print "    -i      Shows IDv2/IDv3 metatags from file"
    print "    --help  Shows help"
    print ""
    print "AUTHOR"
    print ""
    print "    AudioInfo Tools written by Juanjo Salvador - http://juanjosalvador.es\n    View project on GitHub - http://github.com/JuanjoSalvador/ainfo"
    print ""

def needHelp():
    print "Do you need help? Try ainfo --help"

try:
    if len(sys.argv) > 2:
        inputFile = sys.argv[2]
        option    = sys.argv[1]

        # Technical
        if option == "-t":
            if isAudio(inputFile):
                if typeOfAudio(inputFile) == "mpeg":
                    mp3.technical(inputFile)
                elif typeOfAudio(inputFile) == "x-flac":
                    flac.technical(inputFile)
        # Full
        elif option == "-f":
            if isAudio(inputFile):
                if typeOfAudio(inputFile) == "mpeg":
                    mp3.full(inputFile)
                elif typeOfAudio(inputFile) == "x-flac":
                    flac.full(inputFile)
                else:
                    print typeOfAudio(inputFile)
        # ID tags
        elif option == "-i":
            if isAudio(inputFile):
                if typeOfAudio(inputFile) == "mpeg":
                    mp3.idtags(inputFile)
                elif typeOfAudio(inputFile) == "x-flac":
                    flac.idtags(inputFile)
        # Help
    else:
        if sys.argv[1] == "--help":
            showHelp()
        else:
            needHelp()
            
except IndexError as e:
    needHelp()
