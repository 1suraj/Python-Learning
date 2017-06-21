from sys import argv
from os.path import exists

script, F_File, To_File =argv

FileX=open(F_File)
TexttoCopy=FileX.read()


FileY=open(To_File)

TexttoCopy=FileY.read()

#FileY.write(TexttoCopy)

#FileX.close()
#FileY.close()
