class ParkingSystem:
    def __init__(self, big: int, medium: int, small: int):
        self._slots = {
            1: big,
            2: medium,
            3: small
        }

    def addCar(self, carType: int) -> bool:
        if not self._slots[carType]:
            return False
        self._slots[carType] -= 1
        return True


parkingSystem = ParkingSystem(1, 1, 0)
print(parkingSystem.addCar(1))
print(parkingSystem.addCar(2))
print(parkingSystem.addCar(3))
print(parkingSystem.addCar(1))
