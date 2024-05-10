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
    location = []


    def __init__(self, in_rooms, in_rent):
        self.rooms = in_rooms
        self.rent = in_rent

    def add_rooms(self, in_rooms):
        self.rooms = in_rooms

    
    
    
