class realestate(): #main class
#SOB34- utilized classes/objects/methods in this realestate scenario
#and initialized objects and modified it using certain using methods

    def __init__(self,location,supermarket,mall,park):
    #built in function that initiailizes the attributes so that it can be used within the file
        self.location=location
        self.supermarket=supermarket
        self.mall=mall
        self.park=park


    def __str__(self):
        return f' {self.location} {self.supermarket} {self.mall} {self.park} '


    def changes(self):
    #depending on the rent, the total number of certain attributes are changed (sob 32)
        if self.rent>1000 and self.rent<=1500:
            self.supermarket += 1
            print("(+1 supermarket)")
        elif self.rent>1500 and self.rent<=2000:
            self.mall += 1
            print("(+1 mall)")
        elif self.rent>2000 and self.rent<=3000:
            self.park += 1
            self.supermarket += 1
            print("(+1 supermarket and +1 park)")
        else:
            self.park += 1
            self.mall += 1
            self.supermarket +=2 
            print("(+2 supermarket, +1 mall and +1 park)")






class villa(realestate):  #subclass of realestate

    def __init__(self,location,supermarket,mall,park,floor,room,rent):
        super().__init__(location,supermarket,mall,park)
        self.floor=floor
        self.room=room
        self.rent=rent


    def increase_rent(self, room):
    #SOB32- creating a function that uses room as a parameter
    #in villa menu in main.py, there is an option to increase the number of rooms
    #and depending upon the total number of rooms entered, the rent is increased accordingly
        if self.room> 1 and self.room<3:
            self.rent+=350
            print("rent increased by 350 AED")
        elif self.room> 4 and self.room<7:
            self.rent+=450
            print("rent increased by 450 AED")
        else:
            self.rent+=500
            print("rent increased by 500 AED")
        self.room = room


    def __str__(self):
    #returns the attributes of the class in the form of a string
        return (f'\ndisplaying details...'
                f' \nlocated in {self.location}'
                f' \nsupermarket:{self.supermarket}   mall:{self.mall}   park:{self.park}'
                f' \nvilla with {self.floor} floors'
                f' and {self.room} rooms'
                f' \nrent {self.rent} AED per month')
