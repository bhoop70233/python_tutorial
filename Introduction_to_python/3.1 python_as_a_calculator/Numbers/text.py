a='spam eggs' #single quotes
print(a)
b="Paris rabbit got your back :) ! Yay!" #double quotes
print(b)
c='1995' #digits and numerals enclosed in quotes are also strings
print(c)

a='doesn\'t' # use \' to escape the single quote
print(a)
a='"Yes," they said.'
print(a)
a="\"Yes,\" they said."
print(a)
a='"Isn\'t,"they said.'
print(a)
s='First line.\nSecond line.' # \n means newline
print(s)

print('c:\some\name') #here \n means newline
print(r'C:\some\name')  #note the r before the quote
print("""\
    Usage: thingy [options]
    -h            Display this usage message
    -H hostname   Hostname to connect to
    """
)

# 3 times 'un',followed by 'ium'
a=3*'un'+'ium'
print(a)

a='py' 'thon'
print(a)


prefix='py'
a=prefix+'thon'
print(a)
word='Python'
a=word[0] #character in position 0
print(a)


#indices may also be negative numbers,to start counting from the right
a=word[-1] #last character
print(a)

a=word[0:2] #characters from position 0 (included) to 2 (excluded)
print(a)
