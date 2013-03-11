class Person(object):
  def __init__(self,name,gender):
    #capitalize name
    self.name = str.title(name)
    #check gender
    check = str.lower(gender)
    if check != 'm' and check!= 'f':
      raise ValueError("Please enter a valid value for gender: M or F")
    else :
      self.gender = gender.upper()
    #to prevent multi-building states and body-splitting
    self.building = False

class Grid(object):
  def __init__(self):
    #store buildings for keys of location tuples (x,y)
    self.buildings = {}
  
  def querylocation(self,location):
    return self.buildings.get(location)

class Building(object):
  def __init__(self,location,grid):
    self.rooms = {}
    #place building in location. if there is already a building, add it to the list of buildings at a given location tuple
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
  #enable person to leave building
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
    

##
 #
 # note: all inheritance for base classes changed to 'object' to enable use of 'super' due to  #       old-style object issue
 #
 ##

    
