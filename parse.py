import re

def parse(string):
# Remove dashes that often separate words that cross over lines in a book
    text = re.sub(r'(--)|"', ' ', string)
# Remove parantheses
    text = re.sub(r'\(|\)', ' ', string)
    return text.split()
