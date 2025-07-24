class ParkingSystem:
    """
    Intuition - we need a DS to store the current available space for parking. I feel HM will do a great job since we want to store the available space corresponding to each cartype, or we could also use a list where each index will be the cartype.
    """

    def __init__(self, big: int, medium: int, small: int):
       self.slot = [0] * 4
       self.slot[1] = big 
       self.slot[2] = medium
       self.slot[3] = small 

    def addCar(self, carType: int) -> bool:
        if not self.slot[carType]: return False

        self.slot[carType] -= 1

        return True

# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)


# O(1)
# O(1)
