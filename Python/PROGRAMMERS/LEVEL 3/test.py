import re
page = '0muzi0muzi0'
word = 'muzi'
word_pattern = '(?=([^a-z^A-Z]{w}[^a-z^A-Z]))|(?=(^{w}[^a-z^A-Z]))|(?=([^a-z^A-Z]{w}$))'.format(w = word)
print(re.sub('[^a-z]','.',page.lower()).split('.'))
#
# s = "acblllaxb"
#
# p = re.compile('a.b')
# m = p.findall(s)
#
# print(m) #['acb', 'axb']

# s = "expression.py\nimage.png"
#
# p = re.compile('(.*)\.(.*)')
# m = p.findall(s)
#
# print(m) #[('expression', 'py'), ('image', 'png')]