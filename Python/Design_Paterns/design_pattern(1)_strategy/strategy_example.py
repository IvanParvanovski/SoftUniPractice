from abc import abstractmethod, ABC


class IVehicleFact(ABC):
    @abstractmethod
    def interesting_fact(self):
        pass


class ILandVehicleFact(IVehicleFact):
    def interesting_fact(self):
        return 'I have wheels.'


class IAirVehicleFact(IVehicleFact):
    def interesting_fact(self):
        return 'I have wings.'


class IWaterVehicleFact(IVehicleFact):
    def interesting_fact(self):
        return 'I am on water.'


class Vehicle:
    def __init__(self, vehicle_type, model, i_fact):
        self.vehicle_type = vehicle_type
        self.model = model
        self.i_fact = i_fact

    def interesting_fact(self):
        return self.i_fact.interesting_fact()

    def __str__(self):
        return f'I am a {self.vehicle_type} {type(self).__name__} !'


land_vehicles_fact = ILandVehicleFact()
air_vehicles_fact = IAirVehicleFact()
water_vehicles_fact = IWaterVehicleFact()
vehicles = list()

print('--------- MotorBike ---------')
motorbike = Vehicle('motorbike',
                    'Suzuki',
                    land_vehicles_fact)

print(motorbike.interesting_fact())
print(motorbike)
print('\n')

print('--------- Jeep ---------')
jeep = Vehicle('jeep',
               'Land Rover',
               land_vehicles_fact)

print(motorbike.interesting_fact())
print(jeep)
print('\n')

print('--------- Yacht ---------')
yacht = Vehicle('yacht',
                'Nautilus',
                water_vehicles_fact)

print(yacht.interesting_fact())
print(yacht)
print('\n')

print('--------- Boat ---------')
boat = Vehicle('boat',
               'ABSOLUTE 60',
               water_vehicles_fact)

print(boat.interesting_fact())
print(boat)
print('\n')

print('--------- Firefighter Jet ---------')
firefighter_jet = Vehicle('firefighter jet',
                          'J10',
                          air_vehicles_fact)

print(firefighter_jet.interesting_fact())
print(firefighter_jet)
print('\n')

print(' --------- Plane ---------')
plane = Vehicle('plane',
                'boeing 47',
                air_vehicles_fact)

print(plane.interesting_fact())
print(plane)
