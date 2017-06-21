from sys import argv

scripts, filename = argv

txt=open(filename)

print("heres is your file {filename}")

print(txt.read())



print("Type the file again:")
file_again=input("> ")

txt_again=open(file_again)
print(txt_again.read())
