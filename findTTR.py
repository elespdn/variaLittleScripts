

# Attention! Put the name of the source txt file at line 8


import re

txtfile = open('../allSommer.txt', 'r', encoding='utf-8')
txt = txtfile.read()

# everything that is not a letter is replaced by a space
txt_tokens = re.sub('[^A-Za-z]+', ' ', txt).lower()

# count the number of tokens
tokens = len(txt_tokens.split())

# count the number of types, by trasforming the list of tokens into a set (only unique values)
types = len(set(txt_tokens.split()))

TTR = types / tokens * 100 
print(TTR)
