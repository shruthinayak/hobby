'''
USAGE:
python friends.py "<path-to-the-friends-folder>"'''

import sys
import random
import os
from os import listdir
from os.path import isfile, isdir, join
if len(sys.argv)==2:
	path = sys.argv[1]
	print path
	seasons = [ f for f in listdir(path) if isdir(join(path,f)) ]
	print seasons
	season_choice = random.randint(0,len(seasons))
	path+=str(seasons[season_choice])
	print path
	episodes = [ f for f in listdir(path) if isfile(join(path,f)) ]
	episode_choice = random.randint(0,len(episodes))
	video = (path+"/"+episodes[episode_choice]).replace(" ","\\ ").replace("'","\\'").replace(".","\.")
	print video
	cmd='vlc '+video
	os.system(cmd)
else:
	print
	print "USAGE:"
	print "python friends.py <path-to-the-friends-folder>"
	print "REQUIRED: "
	print "VLC Media Player"
