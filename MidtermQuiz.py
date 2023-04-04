class DistanceConversion:
    def __init__(self, distance):
        self.__distance = distance

    def __meter_to_cm(self):
        return self.__distance * 100

    def __meter_to_km(self):
        return self.__distance / 1000

    def __meter_to_inch(self):
        return self.__distance * 39.3701

    def convert(self):
        return (self.__meter_to_cm(), self.__meter_to_km(), self.__meter_to_inch())


distance = float(input("Distance: "))
converter = DistanceConversion(distance)
centimeter, kilometer, inch = converter.convert()
print(f"{distance} meters = {centimeter} centimeters")
print(f"{distance} meters = {kilometer} kilometers")
print(f"{distance} meters = {inch} inches")