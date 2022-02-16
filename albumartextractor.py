import os
from mutagen.id3 import ID3
from mutagen.flac import FLAC
from mutagen.mp4 import MP4

pict_name = "folder.jpg"

rootdir = input("rootdir: ")

for root, dirs, files in os.walk(rootdir):
	#assumes that only directories that work as an album have files
	if (files != [] and pict_name not in files):
		audiofile = root + '/' + files[0]
		print(audiofile)

		ext = audiofile.split('.')[-1]
		if (ext == "mp3"):
			pict = ID3(audiofile).getall("APIC")[0].data
		elif (ext == "flac"):
			pict = FLAC(audiofile).pictures[0].data
		elif (ext == "m4a"):
			pict = MP4(audiofile).tags["covr"][0]
		else:
			raise Exception(ext + " is not supported.")

		with open(root + '/' + pict_name, "wb") as fout:
			fout.write(pict)