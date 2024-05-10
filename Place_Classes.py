from enum import Enum

#Mkae a class to relate to the places. 
#each place will be a member of teh class

class House_type(Enum):
    APARTMENT = 1
    HOUSE = 2
    DORM = 3

class Habitat:
    rooms = 0
    rent = 0
    
