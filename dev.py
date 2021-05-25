import hashtable_chaining as hc
import hashtable_linear_probing as hcl
from helpers import *

table = hc.HashTable()
data = dummy_dat()
vocab = list()

for i, x in enumerate(data):
    if x not in vocab:
        vocab.insert(0,x)
    # if i > 500:
    #     break
    table.insert(x[0], x[1])

for each in vocab:
    print(each[0], table.get(each[0]))
    print(f'should be equal to {each}')
    print('\n')


table = hcl.HashTable()
data = dummy_dat()
vocab = list()
for i, x in enumerate(data):
    if x not in vocab:
        vocab.insert(0,x)
    if i > 100:
        break
    table.insert(x[0], x[1])


for each in vocab:
    print(each[0], table.get(each[0]))
    print(f'should be equal to {each}')
    print('\n')