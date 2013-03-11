from pprint import pprint # pretty print output formatting
from question1 import (common_words, common_words_min, common_words_tuple,
    common_words_safe)
from question2 import parse_links_regex, parse_links_xpath
from question3 import Person, Grid, Building, OfficeBuilding, House
from question4 import GITHUB_URL
# fill in the rest!

print "==testing question 1=="
print "common_words... ",
pprint(common_words("words.txt"))

print "common_words_min 2... ",
pprint(common_words_min("words.txt", 2))

print "common_words_min 5... ",
pprint(common_words_min("words.txt", 5))

print "common_words_min 9... ",
pprint(common_words_min("words.txt", 9))

print "common_words_tuple w/ min 5... ",
pprint(common_words_tuple("words.txt", 5))

print "common_words_safe... ",
pprint(common_words_safe("words_fail.txt", 5))
print


print "==testing question 2=="
print "regex... ",
pprint(parse_links_regex("crimson.html"))
pprint(parse_links_xpath("crimson.html"))
print


print "==testing question 3=="
print "buncha buildings..."
print "init a grid to store building locations: g = Grid()"
g = Grid()
pprint(g)
pprint("evaluating: a = Person('aran khanna', 'f')")
a = Person('aran khanna', 'f')
pprint(a)
pprint("init a building: bldg = Building((1,2),g)")
bldg = Building((1,2),g)
pprint(bldg)
pprint("a enter bldg: Building.enter(a,1)")
bldg.enter(a,1)
pprint("Building.rooms evaluates to {}")
pprint("test iterators: for in loop!")
for person in bldg:
  pprint(person.name)
  pprint(person.gender)
pprint("retrieve some building coordinates: g.buildings")
pprint(g.buildings)
pprint("Let's build an office. o = OfficeBuilding((1,2),['Luke Chang'],g)")
o = OfficeBuilding((1,2),['Luke Chang'],g)
pprint("Check that we get a list of buildings at coordinate (1,2). g.querylocation((1,2))")
pprint(g.querylocation((1,2)))
pprint("Let's find out where Aran is. bldg.where_is(a)")
pprint(bldg.where_is(a))
pprint("let's kick Aran out of the bldg.")
bldg.leave(a)
pprint("Can Aran get into the crimson offices? o.enter(a)")
o.enter(a,2)
pprint("Let's test the __setitem__ method. bldg[1] = a")
bldg[1] = a
pprint(bldg.rooms)
pprint("Create a house. h = House((1,2),g)")
h = House((1,2),g)
pprint("Aran is going back home. h.enter(a)")
h.enter(a)
z = Person('perpetrator', 'm')
pprint("Can a perpetrator get into Aran's house while he's home? h.enter(z)")
h.enter(z)

print


print "==testing question 4=="
print "github url: {}".format(GITHUB_URL)
print


print "==testing question 5=="
# ???
print
