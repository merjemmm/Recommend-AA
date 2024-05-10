from enum import Enum

#Mkae a class to relate to the places. 
#each place will be a member of teh class


class Habitat:
    APARTMENT = 1
    HOUSE = 2
    DORM = 3

    _rooms = 0
    _rent = 0
    _location = []


    def __init__(self, in_rooms, in_rent):
        self.rooms = in_rooms
        self.rent = in_rent

    def add_rooms(self, in_rooms):
        self.rooms = in_rooms


    
    
