Python 3.6.0 (v3.6.0:41df79263a11, Dec 23 2016, 07:18:10) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> """In Python we have the following terms (characters and phrases) for determining if something is "True" or "False." Logic on a computer is all about seeing if some combination of these characters and some variables is True at that point in the program.

and
or
not
!= (not equal)
== (equal)
>= (greater-than-equal)
<= (less-than-equal)
True
False
You actually have run into these characters before but maybe not the terms. The terms (and, or, not) actually work the way you expect them to, just like in English.

The Truth Tables

We will now use these characters to make the truth tables you need to memorize.

NOT	True?
not False	True
not True	False
OR	True?
True or False	True
True or True	True
False or True	True
False or False	False
AND	True?
True and False	False
True and True	True
False and True	False
False and False	False
NOT OR	True?
not (True or False)	False
not (True or True)	False
not (False or True)	False
not (False or False)	True
NOT AND	True?
not (True and False)	True
not (True and True)	False
not (False and True)	True
not (False and False)	True
!=	True?
1 != 0	True
1 != 1	False
0 != 1	True
0 != 0	False
==	True?
1 == 0	False
1 == 1	True
0 == 1	False
0 == 0	True
Now use these tables to write up your own cards and spend the week memorizing them. Remember though, there is no failing in this book, just trying as hard as you can each day, and then a little bit more."""
'In Python we have the following terms (characters and phrases) for determining if something is "True" or "False." Logic on a computer is all about seeing if some combination of these characters and some variables is True at that point in the program.\n\nand\nor\nnot\n!= (not equal)\n== (equal)\n>= (greater-than-equal)\n<= (less-than-equal)\nTrue\nFalse\nYou actually have run into these characters before but maybe not the terms. The terms (and, or, not) actually work the way you expect them to, just like in English.\n\nThe Truth Tables\n\nWe will now use these characters to make the truth tables you need to memorize.\n\nNOT\tTrue?\nnot False\tTrue\nnot True\tFalse\nOR\tTrue?\nTrue or False\tTrue\nTrue or True\tTrue\nFalse or True\tTrue\nFalse or False\tFalse\nAND\tTrue?\nTrue and False\tFalse\nTrue and True\tTrue\nFalse and True\tFalse\nFalse and False\tFalse\nNOT OR\tTrue?\nnot (True or False)\tFalse\nnot (True or True)\tFalse\nnot (False or True)\tFalse\nnot (False or False)\tTrue\nNOT AND\tTrue?\nnot (True and False)\tTrue\nnot (True and True)\tFalse\nnot (False and True)\tTrue\nnot (False and False)\tTrue\n!=\tTrue?\n1 != 0\tTrue\n1 != 1\tFalse\n0 != 1\tTrue\n0 != 0\tFalse\n==\tTrue?\n1 == 0\tFalse\n1 == 1\tTrue\n0 == 1\tFalse\n0 == 0\tTrue\nNow use these tables to write up your own cards and spend the week memorizing them. Remember though, there is no failing in this book, just trying as hard as you can each day, and then a little bit more.'
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> True and True
True
>>> False and True
False
>>> 1==1 and 2==1
False
>>> "test"=="test"
True
>>> 1==1 or 2!=1
True
>>> True and 1==1
True
>>> False and 0 !=0
False
>>> not(True and False)
True
>>> not(1==1 and 0!=1)
False
>>> not ("testing" == "testing" and "Zed" == "Cool Guy")
True
>>> 1 == 1 and (not ("testing" == 1 or 1 == 0))
True
>>> "chunky" == "bacon" and (not (3 == 4 or 3 == 3))
False
>>> 3 == 3 and (not ("testing" == "testing" or "Python" == "Fun"))
False
>>> 
