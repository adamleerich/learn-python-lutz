M = [[1, 2, 3], 
     [4, 5, 6],
     [7, 8, 9]]

# M is a list of lists, each element is a row
len(M)
M[0]

# Get a column
col2 = [row[1] for row in M]
col2

[c*2 for c in 'spam']

list(range(4))

[[x*1.0, x/2.0, x*2.0] for x in range(-6, 7, 2) if x > 0]


# Generator functions!
G = (sum(row) for row in M)
next(G)
next(G)
next(G)


# map a function across an iterable
list(map(sum, M))


