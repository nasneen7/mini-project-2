from realestate import *
#SOB33- importing realestate class details to this file
#imports everything i.e,classes,functions and attributes from other files
#so that it can be used in this file


class apartment(realestate): #subclass of realestate 

    def __init__(self,location,supermarket,mall,park,floorno,room,flattype,rent):
        super().__init__(location,supermarket,mall,park)
        self.floorno=floorno
        self.room=room
        self.flattype=flattype
        self.rent=rent


    def suffix(self): #function for adding suffixs to the floor numbers
        if self.floorno==1:
            return "st"
        elif self.floorno==2:
            return "nd"
        elif self.floorno==3:
            return "rd"
        else:
            return "th"


    def show_flattype(self,room,floorno):
    #SOB32
    #SOB35- function with 2 parameteres inside the class which includes certain properties and methods
    #function for checking if the floor number and number of rooms go with the values entered earlier
    #and if so it prints the type of flat entered for that particular apartment
        if room==self.room:
            if floorno==self.floorno:
                return f'- flat in {self.floorno}{self.suffix()} floor with {self.room} rooms has a flat type of {self.flattype}'
            else:
                return f'{self.floorno}{self.suffix()} does not correspond with the room number of the apartment'
        else:
            return f'{self.room} you entered does not correspond with the room number of the apartment'


    def increase_rent(self):
    #depending upon the floor number of the apartment, rents are increased with access to gym or/and pool
        if self.floorno>=1 and self.floorno<=5:
            self.rent +=100
            print("(100AED increased and access to gym)")
        elif self.floorno>=6 and self.floorno<=10:
            self.rent +=500
            print("(500AED increased and access to gym & building pool)")


    def __str__(self):
        return (f'\ndisplaying details....'
               f' \nlocated in {self.location}'
               f' \nsupermarket:{self.supermarket}  mall:{self.mall}   park:{self.park}'
               f' \n{self.floorno}{self.suffix()} floor and has {self.room} bedrooms'
               f' \n{self.flattype} flat'
               f' \nrent {self.rent} AED per month')

