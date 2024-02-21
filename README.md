# dsk2po and po2dsk
Python scripts to convert Apple II/III .DSK (DO) images to ProDOS-ordered images
and vice versa.

This is nothing very exciting, it just maps sectors in .dsk (DOS-order, .do) files
into those of a .po (ProDOS-order) file.  Most Apple II emulators can handle both,
but certain utilities (with which I wanted to use existing .dsk images) assume
ProDOS-ordered files.

Usage is just (assuming you've done `chmod 755 dsk2po.py`, else precede with python command):

    ./dsk2po.py image.dsk

This will create image.dsk.po alongside it.  Pretty much no checking is done.
It just goes through all the tracks and converts them, then ends.

Both scripts will handle an arbitrary number of tracks, but will print a
warning if the number of tracks is not 35.

This can be used as an action for find, like so:

    find imagefolders/\*/\*.dsk -exec ./dsk2po.py {} \;

...which was mostly the point.

You can also go the opposite direction:

    ./po2dsk.py image.po
