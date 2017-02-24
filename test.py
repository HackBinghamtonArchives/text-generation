import random
import textgen
import os

my_gen = textgen.Generator()
# my_gen = textgen.Hat()

os.chdir('data')
files = os.listdir()

for i in files:
    with open(i, 'r') as f:
        text = f.read()
        my_gen.train(text)

lines = []
for i in range(10):
    lines.append(my_gen.gen_sentence(random.randint(7,15)))
print('\n'.join(lines))
