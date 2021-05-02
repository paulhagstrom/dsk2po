#!/usr/bin/env python3
# scramble po back into dsk
# Chris Torrence, Oct 2020
import sys, getopt, re
from dsk2po import dsk2po
def main(argv=None):
  print("po2dsk - convert po files to dsk files")

  try:
    opts, args = getopt.getopt(sys.argv[1:], '')
  except getopt.GetoptError as err:
    print(str(err))
    usage()
    return 1
  try:
    filenameIn = args[0]
  except:
    print('You need to provide the name of a PO file to begin.')
    return 1

  tracks = []
  # Note that the same algorithm can be used to convert in either direction
  with open(filenameIn, mode="rb") as fileIn:
    for track in range(35):
      trackbuffer = fileIn.read(4096)
      tracks.append(dsk2po(trackbuffer))
  dskfilename = re.sub('\.po$', '', filenameIn, flags=re.IGNORECASE) + ".dsk"
  print('Writing dsk image to {}'.format(dskfilename))
  with open(dskfilename, mode="wb") as file:
    for track in tracks:
      file.write(track)
  return 1

if __name__ == "__main__":
  sys.exit(main())
