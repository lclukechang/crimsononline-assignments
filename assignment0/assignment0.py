#!/usr/bin/python

# 2. FizzBuzz!

def execFizzBuzz():
  nums = range(1,101)
  for n in nums:
    if  (n % 3) + (n % 5) == 0:
      print "FizzBuzz"
    elif n % 3 == 0:
      print "Fizz"
    elif n % 5 == 0:
      print "Buzz"
    else:
      print n

#print "Let's playing FizzBuzz!"
#execFizzBuzz()




# 3(v1). swapchars - "common" letters are defined to be case-insensitive
class char:
  value = ''
  freq = 0

def case_insen_count(string,query):
  return str.count(string,query) + str.count(string,str.swapcase(query))

def case_sen_swap(sw_out,sw_in):
  if str.isupper(sw_out):
    return str.upper(sw_in)
  else:
    return str.lower(sw_in)
 
def swapchars(string):
  #init char objects store values/freqs of most/least commons
  most = char()
  least = char()
  #iterate through chars of string to perform case-insensitive count
  for c in string:
    #skip whitespaces
    if c == ' ':
      continue
    count = case_insen_count(string,c)
    if count > most.freq:
      most.value = c
      most.freq = count
    elif least.freq == 0 or count <= least.freq:
      least.value = c
      least.freq = count
  #new list of chars to store output string
  strlist = list()
  for c in string:
    #output each char preserving case of target position in string
    if str.lower(c) == str.lower(most.value):
      strlist.append(case_sen_swap(c,least.value))
    elif str.lower(c) == str.lower(least.value):
      strlist.append(case_sen_swap(c,most.value))
    else:
      strlist.append(c)
  return ''.join(strlist)
        
#input = raw_input('swapchars(case-insensitive!) - Enter a string: ')
#swapchars(input)


#3(v2). swapchars_sen - counts letters with regards to case: e.g T and t are
                       #considered two different characters
import collections

def swapchars_sen(string):
  #use Counter function to determine freqs
  freqs = collections.Counter(string).most_common()
  #conditionals to avoid operating with whitespaces:
  if freqs[0][0] == ' ':
    most = freqs[1][0]
    least = freqs[-1][0]
  elif freqs[-1][0] == ' ':
    most = freqs[0][0]
    least = freqs[-2][0]
  else:
    most = freqs[0][0]
    least = freqs[-1][0]
  strlist = list()
  for c in string:
    if c == most:
      strlist.append(least)
    elif c == least:
      strlist.append(most)
    else:
      strlist.append(c)
  return ''.join(strlist)

#input = raw_input('swapchars_sen! - Enter a string: ')
#swapchars_sen(input)



#4. sortcat

def sortcat( n, *strings ):
  if n == -1:
    return ''.join(sorted(strings, key = len, reverse = True))
  else:
    return ''.join(sorted(strings, key = len)[:-n-1:-1])



#5b. Luigi wins

#use random module
from random import choice

def luigi_simu(n):
  #possible directions for opponents
  dir = ['fw','up','dn','lt','rt']
  wins = 0.
  for i in range(n):
    opp = 3
    for j in range(5):
      for k in range(3):
        if choice(dir) == 'fw':
          opp -= 1
          break
    if opp <= 0:
      wins += 1
  return wins/n

print(luigi_simu(1000))
      



  


print("I love the Crimson tech department!")
