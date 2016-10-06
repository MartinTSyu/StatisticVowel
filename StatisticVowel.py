#coding:utf-8

string1 = raw_input("Please enter a string:")

VowelLetter = 0
aLetter = 0
eLetter = 0
iLetter = 0
oLetter = 0
uLetter = 0
ConsonantLetter = 0
Others = 0

for letter in string1:
    if letter.lower() in 'aeiou':
        VowelLetter += 1
        if letter.lower() in 'a':
            aLetter += 1
        elif letter.lower() in 'e':
            eLetter += 1
        elif letter.lower() in 'i':
            iLetter += 1
        elif letter.lower() in 'o':
            oLetter += 1
        elif letter.lower() in 'u':
            uLetter += 1
    elif letter.lower() in 'bcdfghjklmnpqrstvwxyz':
        ConsonantLetter += 1
    elif letter not in 'abcdefghijklmnopqrstuvwxyz':
        Others += 1

print "In this string , have VowelLetter:", VowelLetter
print "aLetter:", aLetter
print "eLetter:", eLetter
print "iLetter:", iLetter
print "oLetter:", oLetter
print "uLetter:", uLetter
print "ConsonantLetter:", ConsonantLetter
print "Ohters:", Others
print "The length 'use len()' of this string is ", len(string1)
print "VowelLetter + ConsonantLetter + Others =" , VowelLetter + ConsonantLetter + Others
