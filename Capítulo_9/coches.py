import sys
sys.path.append('../clases/')
from clases.car import Car
from clases.electricCar import ElectricCar

print("Térmico ------------ ")
my_car = Car('audi', 'a4', 2009)
print(my_car.get_descriptive_name())
my_car.update_odometer(125000)
my_car.read_odometer()
my_car.update_odometer(124000)
my_car.increment_odometer(-13)
my_car.read_odometer()
my_car.fill_gas_tank()
print("Electrico ----------- ")
my_car2 = ElectricCar("Nissan", "Leaf", 2024)
print(my_car2.get_descriptive_name())
my_car2.battery.battery_size = 65
my_car2.battery.describe_battery()
my_car2.battery.get_range()
my_car2.fill_gas_tank()