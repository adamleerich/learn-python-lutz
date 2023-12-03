import re

dir(re)

m = re.match('(.*)(c)(.*)', 'abcdabcd')
m.groups()
m.groups()[2]
