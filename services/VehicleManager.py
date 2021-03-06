from repo.GetData import GetData
from repo.SaveData import SaveData
from Models.Vehicle import Vehicle

REGISTRATION_NUMBER = 0
RENTED = 1
MODEL_YEAR = 2
BRAND = 3
PRICE = 4
CAR_TYPE = 5
VEHICLE_FILE = "cars.csv"
class VehicleManger(object):
    def __init__(self):

        self.__Vehicles_Data = GetData(VEHICLE_FILE).readData()
        self.__Vehicles = []
        self.__AvailableVehicles = []
        self.__VehiclesInRent = []
        self.__DataSaver = SaveData(VEHICLE_FILE)
        self.loadVehicles()
        self.loadRentedVehicles()
        self.loadAvailableVehicles()

    def loadVehicles(self):
        for line in self.__Vehicles_Data:
            regnum = line[REGISTRATION_NUMBER]
            rented = line[RENTED]
            model_year = line[MODEL_YEAR]
            brand = line[BRAND]
            price = line[PRICE]
            car_type = line[CAR_TYPE]
            car = Vehicle(regnum, model_year, rented, brand, price, car_type)
            self.__Vehicles.append(car)

    def loadAvailableVehicles(self):
        for Veh in self.__Vehicles:
            if not Veh.getRented():
                self.__AvailableVehicles.append(Veh)

    def loadRentedVehicles(self):
        for Veh in self.__Vehicles:
            if Veh.getRented():
                self.__VehiclesInRent.append(Veh)

    def registerNewVehicle(self, registration_number, rented, model_year, brand, price, car_type):
        newVehicle = Vehicle(registration_number, model_year, rented, brand, price, car_type)
        self.__Vehicles.append(newVehicle)
        self.Save() #Save-a í hvert sinn sem við bætum við nýjum bíl
        return newVehicle

    def getVehicles(self):
        return self.__Vehicles

    def getAvailable(self):
        return self.__AvailableVehicles
        
    def getRentedVehicles(self):
        return self.__VehiclesInRent

    def Save(self):
        self.__DataSaver.WriteData(self.__Vehicles)
        
