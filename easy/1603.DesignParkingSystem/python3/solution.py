class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.parking=dict(zip(range(1,4), (big,medium,small)))

    def addCar(self, carType: int) -> bool:
        if self.parking[carType] <= 0:
            return False
        self.parking[carType] -= 1
        return True