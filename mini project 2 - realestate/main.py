#program in which a realtor could enter details for an apartment or villa
#each of them has it own menu
#options in the case of apartment are that it can display the details,show the flat type,increase the rent depending
#upon the floor selected with access to gym or/and pool and add more attributes depending on the rent
#options in the case of villa are that it can dsiplay the details,increase rent by adding more rooms
#and add more attributes depending on the rent

from realestate import *
from apartment import *


def main_menu(): #function which gives us the option to select between apartment and villa 
    decision=True
    while decision==True:
        print("-"*50)
        print("MAIN MENU")
        print("1. for Apartments")
        print("2. for Villa")
        print("0. to exit the program")
        choice=int(input("enter the choice: "))
        if choice==1:
            apartment_menu()
            pass
        elif choice==2:
            villa_menu()
            pass
        elif choice==0:
            print("thank you for using the program!")
            print("exiting....")
            decision=False
        else:
            print("invalid choice. try again!")
            decision=False


def apartment_menu():
    
    apartment_decision=True
    print("\ndetails for apartment")
    location=str(input("enter location: "))
    supermarket=int(input("enter the number of supermarkets in the vicinity: "))
    mall=int(input("enter the number of malls in nearby vicinity: "))
    park=int(input("enter the number of parks in nearby vicinity: "))
    floorno=int(input("enter the floor number of the apartment: "))
    room=int(input("enter the number of rooms: "))
    flattype=str(input("enter the type of flat (single/duplex): "))
    rent=int(input("enter the rent of the flat (1000 and above): "))
    apartment1=apartment(location,supermarket,mall,park,floorno,room,flattype,rent)

    while apartment_decision==True:
        print("-"*50)
        print("1. to show details of the flat")
        print("2. to show flat type of the apartment")
        print("3. to increase the rent of the flat depending upon the floor number")
        print("4. to add more benefits based on rent")
        print("0. to exit apartment menu")
        choice = int(input("enter the choice: "))
        if choice==1:
            print(apartment1.__str__())   #displays all the details entered for the apartment
        elif choice==2:
            floor_number=int(input("enter the floor number of the current apartment: "))
            room_number=int(input("enter the room number of the current apartment: "))
            print(apartment1.show_flattype(room_number,floor_number))
        elif choice==3:
            print("since floor number is ",apartment1.floorno)
            apartment1.increase_rent()
        elif choice==4:
            apartment1.changes()
            print(apartment1.__str__())
        else:
            print("exiting apartment menu...")
            apartment_decision=False
            main_menu()



def villa_menu():

    villa_decision=True
    print("\ndetails for villa")
    location=str(input("enter location: "))
    supermarket=int(input("enter the number of supermarkets in the vicinity: "))
    mall=int(input("enter the number of malls in nearby vicinity: "))
    park=int(input("enter the number of parks in nearby vicinity: "))
    floor=int(input("enter the number of floors in the villa: "))
    room=int(input("enter the number of rooms in the villa: "))
    rent=int(input("enter the rent of the villa(1000 and above): "))
    villa1=villa(location,supermarket,mall,park,floor,room,rent)

    while villa_decision==True:
        print("-"*50)
        print("1. to show details about the villa")
        print("2. to add more rooms and increase the rent")
        print("3. to add more benefits based on rent")
        print("0. to exit villa menu")
        choice=int(input("enter the choice: "))
        if choice==1:
            print(villa1.__str__())  #displays all the details entered for the villa
        elif choice==2:
            print("number of rooms before changing: ",villa1.room)
            roomno=int(input("enter the total number of rooms required in the villa: "))
            villa1.increase_rent(roomno) 
        elif choice==3:
            villa1.changes()
            print(villa1.__str__())
        else:
            print("exiting villa menu...")
            villa_decision=False
            main_menu()


main_menu()

