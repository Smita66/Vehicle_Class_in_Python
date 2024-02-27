#vehiclecalss.py

class Vehicle:
    '''
    Vehicle Class
    This class models a vehicle on a used car lot
    Change Order: we need to add maximum speed to the model
    change Order: need a way to read maximum speed from the model
    change Order: some developers need to use the constructor without having to provide a max speed
    '''
    #constructor. its called when  and instantiate an object if vehicle type
    def __init__(self, type, max_speed = None):
        '''
        @param type: the kind of vehicle
        @param max_speed = maximum speed of the vehicle, defaults to None
        '''
        self.type = type;            # type encapsulate the class 
        self._thisisprivate = 42     # This is the weak attempt to support the data hiding
        self.max_speed = max_speed   # save a copy in current object
    # A instance method. it operates on an instance of the vehicle class
    def printType(self):
        print(self.type);
    
    def getSpeed(self):        # "a getter"
        return self.max_speed

if __name__ == "__main__":
    # Some code to test the class would go here.
    # If there's no code, just pass
    pass