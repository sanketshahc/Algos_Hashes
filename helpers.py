import re

def dummy_hash(string):
  return int(
    sum(
    [
      k*10*n*2**.5 for k,n in enumerate(
        [ord(i) for i in string]
      )
    ]
  )
  )


def dummy_dat():
  for line in open('dat.txt', 'r').readlines():
    line = line.lower()
    line = re.sub("\W", " ", line)
    line = re.sub("(\s.{2}\s)|(\s.{1}\s.{1}\s)|(\s.{1}\s)", " ", line)
    line = re.sub("\s+", ",", line)
    line = re.sub(",$", "", line)
    for word in line.split(','):
      if len(word) > 1:
        yield (word, len(word))
