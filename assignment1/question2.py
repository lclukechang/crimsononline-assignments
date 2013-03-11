
#assumes tags are wellformed, and all anchor tags are labelled with some
#label

import re
def parse_links_regex(filename):
  try:
    f = open(filename, 'r')
    html = f.read()
    labels = re.findall(r"(?i)<a.+>(.+)</a>",html)
    f.seek(0)
    html = f.read()
    links = re.findall(r"(?i)<a href *= *\"(.+)\">",html)
    return dict(zip(labels,links))
  except IOError:
    print "Could not open file \"{}\".".format(filename)

from lxml import etree
def parse_links_xpath(filename):
  try:
    #init HTML parser
    parser = etree.HTMLParser()
    tree = etree.parse(filename, parser)
    #retrieve all elements that at anchors with href sources
    links = tree.findall('//a[@href]')
    lst = dict()
    #strip and return dictionary
    for link in links:
      lst[link.text] = link.attrib['href']
    return lst
  except IOError:
    print "Could not open file \"{}\".".format(filename)

##
 #
 # Xpath/lxml is much better than Regex. lxml actually parses and processes
 # the html into a object tree that is much less error prone to searches 
 # than an arbitrary regular expression match.
 #
 ##
