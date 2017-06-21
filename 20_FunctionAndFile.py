from sys import argv

script, input_file = argv



def printall(alltext):
    print(alltext)

def gotoline(alltext):
    alltext.seek(0)

def pintaline(line_count,alltext):
    print(line_count,alltext.readline())



alltext=open(input_file)
line_count=1
Line=gotoline(alltext)

print(pintaline(line_count,alltext))

Line=gotoline(alltext)+1

print(pintaline(line_count,alltext))

Line=gotoline(alltext)+3
