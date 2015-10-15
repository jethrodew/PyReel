      88888888ba                88888888ba                           88
      88      "8b               88      "8b                          88
      88      ,8P               88      ,8P                          88
      88aaaaaa8P'  8b       d8  88aaaaaa8P'   ,adPPYba,   ,adPPYba,  88
      88""""""'    `8b     d8'  88""""88'    a8P_____88  a8P_____88  88
      88            `8b   d8'   88    `8b    8PP"""""""  8PP"""""""  88
      88             `8b,d8'    88     `8b   "8b,   ,aa  "8b,   ,aa  88
      88               Y88'     88      `8b   `"Ybbd8"'   `"Ybbd8"'  88
                      d8'
                    d8'

/***************************************************************************\

Pyreel is a python utility which provides a commandline RSS output for the BBC news. 
Replacing the necessary RSS feeds will change the output accordingly. 
This will eventually be 
1) more customisable to make it easier to plug in different feeds and information 
2) ready to work specifically for smaller screens. I intend to release this for the Raspberry Pi 3.5inch screen attachment for a handy, portable desk feed.

Configuration:
	Copy the config.example.py to a file called config.py, modify to your desired options

How To Run:
	Browse to the directory in a terminal or similar and run "python reel.py"


Author:

	Jethro Dew (jethrodew.co.uk)

License:

	See LICENSE.txt in the Project Root. This excludes additional Libraries detailed below.


Required Libraries:

	Feedparser: This will need to be checked out and installed from: https://github.com/kurtmckee/feedparser

