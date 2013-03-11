"""question 3

a)  Implement classes representing people and buildings. People should support
    name and gender, seamlessly verifying that gender is either M or F (if it
    isn't, what's the best way to inform the calling code that a mistake was
    made?) and enforcing capitalization of both first name and last name.

b)  Buildings should support a function enter that takes a person and a room
    number. The building should then keep track of anyone who enters/leaves the
    building and respond to some type of where_is(person) query with the room
    number that person is in. Ensure, naturally, that no one can be in more
    than one building at a time.

c)  Make the building class iterable over the people in it. That is, make it
    possible to write a for loop of the form:
        for person in building:
            ...

d)  Implement a class that represents an office building, an object that
    behaves the same as a building but only allows people to enter if they are
    on a list of employees passed in when the OfficeBuilding is instantiated.
    You may want to look up the super function in the Python documentation
    concerning classes.

e)  Implement a class that represents a house. The House class should implement
    enter to take only a Person object, and the House class should not support
    where_is at all. It should instead support at_home(Person), a function that
    returns a Boolean.

f)  Modify all buildings, houses included, to remember their location as an
    (x, y) tuple. Then make it possible to call some function that takes such
    a tuple and returns the building object at that tuple or None if no
    building exists at that location. You may choose whether any given location
    can only hold one building or multiple buildings, but you need to handle
    this corner case in some logical fashion.

g)  With a minimum of code duplication, modify the Building class so that
    bldg[roomnumber] = person accomplishes the same thing as
    bldg.enter(person, roomnumber). Be careful with how you do this if you
    chose to inherit any classes from Building (which you should have).
"""

class Person(object):
  def __init__(self,name,gender):
    self.name = str.title(name)
    check = str.lower(gender)
    if check != 'm' and check!= 'f':
      raise ValueError("Please enter a valid value for gender: M or F")
    else :
      self.gender = gender.upper()
    self.building = False

class Grid(object):
  def __init__(self):
    self.buildings = {}

  def querylocation(self,location):
    return self.buildings.get(location)

class Building(object):
  def __init__(self,location,grid):
    self.rooms = {}
    if grid.buildings.has_key(location) == True:
      grid.buildings[location].append(self)
    else:
      grid.buildings[location] = [self]

  def __iter__(self):
    return self.rooms.itervalues()

  def enter(self, person, room_no):
    if person.building == True:
      print "{} is already in a building.".format(person.name)
    elif self.rooms.has_key(room_no):
      print "{} is already in that room! No break-ins!".format(self.rooms[room_no].name)
    else:
      person.building = True
      self.rooms[room_no] = person

  def __setitem__(self, key, value):
    self.enter(value, key)

  def where_is(self, person):
    if person.building == False:
      print "{} is currently not in a building.".format(person.name)
    else :
      return [key for (key,value) in self.rooms.items() if value == person]

  def leave(self, person):
    if person.building == False:
      print "{} is not in any building. Check your brains, yo.".format(person.name)
    else:
      for key,value in self.rooms.iteritems():
        if value == person:
          print "{} has left the building. Dang.".format(person.name)
          del self.rooms[key]
          person.building = False
          break
            



class OfficeBuilding(Building):
  def __init__(self, location, employees, grid):
    self.employees = employees
    super(OfficeBuilding,self).__init__(location, grid)

  def enter(self, person, room_no):
    if person.name in self.employees:
      super(OfficeBuilding,self).enter(person, room_no)
    else:
      print "Sorry, but {} is not an employee here!.".format(person.name)

class House(object):
  def __init__(self, location,grid):
    self.location = location
    self.occupant = None
    if grid.buildings.has_key(location) == True:
      grid.buildings[location].append(self)
    else:
      grid.buildings[location] = [self]


  def enter(self, person):
    if self.occupant == None:
      self.occupant = person
      person.building == True
    else:
      print "{} lives here. Don't break-in. Make good life decisions.".format(self.occupant.name)

  def at_home(self,person):
    if self.occupant == person:
      return True
    else:
      return False
    
    
