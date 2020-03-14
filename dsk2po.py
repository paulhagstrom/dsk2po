#!/usr/bin/env python3
# unscramble dsk into po
# Paul Hagstrom, Dec 2015
import sys, getopt, re
def main(argv=None):
	print("dsk2po - convert dsk files to po files")

	try:
		opts, args = getopt.getopt(sys.argv[1:], '')
	except getopt.GetoptError as err:
		print(str(err))
		usage()
		return 1
	try:
		dskfilename = args[0]
	except:
		print('You need to provide the name of a DSK file to begin.')
		return 1

	potracks = []
	with open(dskfilename, mode="rb") as dskfile:
		for track in range(35):
			trackbuffer = dskfile.read(4096)
			potracks.append(dsk2po(trackbuffer))
	pofilename = re.sub('\.dsk$', '', dskfilename, flags=re.IGNORECASE) + ".po"
	print('Writing po image to {}'.format(pofilename))
	with open(pofilename, mode="wb") as pofile:
		for potrack in potracks:
			pofile.write(potrack)
	return 1

# From Beneath Apple ProDOS, table 3.1
# block 000 physical 0, 2 DOS 0, E page 0, 1
# block 001 physical 4, 6 DOS D, C page 2, 3
# block 002 physical 8, A DOS B, A page 4, 5
# block 003 physical C, E DOS 9, 8 page 6, 7
# block 004 physical 1, 3 DOS 7, 6 page 8, 9
# block 005 physical 5, 7 DOS 5, 4 page a, b
# block 006 physical 9, B DOS 3, 2 page c, d
# block 007 physical D, F DOS 1, F page e, f

# dsk images are in DOS order, so I need to convert from
# DOS sectors into blocks.  That is combine D and C into 2 and 3

block_map = [0, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 15]

def dsk2po(trackbuffer):
	potrack = bytearray()
	for chunk in range(16):
		chunk_start = 256*block_map[chunk]
		chunk_end = chunk_start + 256
		potrack.extend(trackbuffer[chunk_start:chunk_end])
	return potrack

if __name__ == "__main__":
	sys.exit(main())
