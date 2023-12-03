import string


S = 'Spam'
S[:]
len(S)
S[0]
S[1]
S[0:1]
S[0:]
S[0:-1]
S[1:-1]
S[0:len(S)]
S * 8

L = list(S)
L
''.join(L)

B = bytearray(b'spam')
B
B.extend(b'eggs')
B
B.decode()

dir(string)
S[S.find('pa'):]
S.replace('pa', 'XYZ123')
line = 'aaa,bbb,ccc,ddd'
line.split(',')
S.upper()
S.isalpha()
S.isnumeric()
'123'.isnumeric()
'123e-1'.isnumeric()
'1.23'.isnumeric()
str(1.23).isnumeric()
str(123).isnumeric()
str(123e3).isnumeric()
str(123e3)

W = '\n\n\t This is a string with lots of whitespace!\t\t\n\n\r'
W.lstrip()
W.rstrip()
W.strip()
W.split('\n')

'%s and %s' % ('A', 'B')
'{0} and {1}'.format('A', 'B')
'{0} and {0}'.format('A', 'B')
'{} and {}'.format('A', 'B')

'{:,.2f}'.format(29599.234)


# Getting help, page 106-107
help(S.replace)


# Other ways to code strings, page 107
S = 'A\nB\tC'
len(S)
ord('\n')
S = 'A\0B\0C'
len(S)
S

