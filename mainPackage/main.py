#main.py
# add an import statement for vehicle class

from vehicleClassPackage.vehicleClass import *

if __name__ == "__main__":
    #instantiate an object if type vehicle
    myCorvette = Vehicle("Car", 120)   # trigger a call to constructor
    myCorvette.printType()             # invoke the method on object
    
    #invoke the getter for maximum speed, store the return value in a variable
    # print that to the console.
    
    maximum_speed = myCorvette.getSpeed()
    print("maximum speed :", maximum_speed)
    
    #instantiate another vehicle object. we can name  it
    myLexus = Vehicle("Car")  # myLexus is an object of type vehicle
   
   
    # i want a list of 3 vehicles: Car, Boat, space ship
    # we can pick the names and properties
    # i want some friendly output to demo your work
    myVehicles =[Vehicle("Toyota corolla", 150)
                 , Vehicle("sailboat", 20)
                 , Vehicle("falcon Heavy", 4000)]
    for vehicle in myVehicles:
        vehicle.printType()
        print(vehicle.getSpeed())
    
    