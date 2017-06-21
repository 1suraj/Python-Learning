from sys import argv

script, filename=argv

print(f"We're going to erase {filename}.")
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN.")

input("?")

OpenFile=open(filename,'w')


OpenFile.truncate()

print("All text Deleted")


#OpenFile=open(filename)
#
#input("Check")
#print(OpenFile.read())

print("Now Let's write Something")

line1=input("Line1:")
line2=input("Line2:")
line3=input("Line3:")


OpenFile.write(line1)
OpenFile.write('\n')
OpenFile.write(line2)
OpenFile.write(line3)

print("All Done")

OpenFile.close()

