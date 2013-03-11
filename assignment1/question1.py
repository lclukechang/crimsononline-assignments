
from re import findall
from collections import Counter

def common_words(filename):
  words = findall(r"\b[A-z]+\b",(open(filename).read().lower()))
  freqs = Counter(words)
  return freqs.keys()
  

# could also use lambdas and map/filter here instead of copy/pasting
from re import compile
def common_words_min(filename, min_chars):
  regex = compile(r"\b[A-z]{%d,}\b"%min_chars)
  words = regex.findall(open(filename).read())
  words = [str.lower() for str in words]
  freqs = Counter(words)
  return freqs.keys()

def common_words_tuple(filename, min_chars):
  regex = compile(r"\b[A-z]{%d,}\b"%min_chars)
  words = regex.findall(open(filename).read().lower())
  freqs = Counter(words)
  return freqs.viewitems()

def common_words_safe(filename, min_chars):
  try:
    regex = compile(r"\b[A-z]{%d,}\b"%min_chars)
    f = open(filename)
    words = regex.findall(f.read().lower())
    freqs = Counter(words)
    return freqs.viewitems()
 
  except IOError:
    print "Error opening the file \"{}\".".format(filename)

