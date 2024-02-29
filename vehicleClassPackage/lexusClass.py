from vehicleClassPackage.Car import Car
# This works but Eclipse flags an error in the editor.
class Lexus(Car):
  def __init__(self, type, make, model, batteryKVA):
    self.batteryKVA = batteryKVA;
    Car.__init__(self, type, make, model);
  def printBatteryKVA(self):
    print(self.batteryKVA);