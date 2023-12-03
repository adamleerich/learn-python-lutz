# What the following statement actually does:
#
#   1. Create an object to represent the value 3
#   2. Create the variable/name a, if it doesn't exist
#   3. Link the variable to the new object
#   4. If a already existed, decrement the reference count for the object that it used to point to
#   5. If that reference count drops to zero, send the object to garbage collection
#
# Variables are entries in a system table
# Objects are pieces of allocated memory
# References are automatically followed pointers from variables to objects
# Python references are similar to C pointers
# However, they are automatically dereferenced when used
# You can think of references as C `void*` pointers
#
# TODO what are cyclic references?
#

L = ['a', 'n', 'w']
M = L
L[1] = 0
M

import copy

N = copy.copy(L)
N
L[0] = 'zero'
L
N
P = ['a', 'b', L]
P
Q = copy.copy(P)
R = copy.deepcopy(P)
Q
R
P[0] = 'zero'
Q
R
L[0] = 'updated L'
P
Q
R

import sys

sys.getrefcount(L)
