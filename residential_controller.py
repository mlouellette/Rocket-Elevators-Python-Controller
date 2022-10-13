
elevatorID = 1
floorRequestButtonID = 1
callButtonID = 1


class Column:
    def __init__(self, _ID, _amountOfFloors, _amountOfElevators):
        self.ID = _ID
        self.status = ""
        self.elevatorList = []
        self.callButtonList = []

        self.createElevators(_amountOfFloors, _amountOfElevators)
        self.createCallButtons(_amountOfFloors)

    def createCallButtons(self, _amountOfFloors):
       buttonFloor = 1
       callButtonID = 1

       for i in range(0, _amountOfFloors):
        if buttonFloor < int(i):
         callButton = CallButton(callButtonID, buttonFloor, "Up")
         self.callButtonList.append(callButton)
         callButtonID += 1

        if buttonFloor > 1:
         callButton = CallButton(callButtonID, buttonFloor, "Down")
         self.callButtonList.append(callButton)
         callButtonID += 1

        buttonFloor += 1

    def createElevators(self, _amountOfFloors, _amountOfElevators):
        elevatorID = 1
        for i in range(_amountOfElevators):# a verifier
            elevator = Elevator(elevatorID, _amountOfFloors)
            self.elevatorList.append(elevator)
            elevatorID += 1

    def requestElevator(self, floor, direction):
        
        elevator = self.findElevator(floor, direction)
        elevator.floorRequestList.append(floor)
        elevator.move()
        elevator.operateDoors()
        elevator.floorRequestList = []
        return elevator

    def findElevator(self, requestedFloor, requestedDirection):
        bestElevator = None
        bestScore = 5
        referenceGap = 10000000
        bestElevatorInformations = None
        for i in self.elevatorList:
            #elevator = self.elevatorList[i]
            if requestedFloor == i.currentFloor and i.status == "stopped" and requestedDirection == i.direction:
                bestElevator, bestScore, referenceGap = self.checkIfElevatorIsBetter(1, i, bestScore, referenceGap, bestElevator, requestedFloor)

            elif requestedFloor > i.currentFloor and i.direction == "up" and requestedDirection == i.direction:
                bestElevator, bestScore, referenceGap = self.checkIfElevatorIsBetter(2, i, bestScore, referenceGap, bestElevator, requestedFloor)

            elif requestedFloor < i.currentFloor and i.direction == "down" and requestedDirection == i.direction:
                bestElevator, bestScore, referenceGap = self.checkIfElevatorIsBetter(2, i, bestScore, referenceGap, bestElevator, requestedFloor)

            elif i.status == "idle":
                bestElevator, bestScore, referenceGap = self.checkIfElevatorIsBetter(3, i, bestScore, referenceGap, bestElevator, requestedFloor)
            else:
                bestElevator, bestScore, referenceGap = self.checkIfElevatorIsBetter(4, i, bestScore, referenceGap, bestElevator, requestedFloor)
            
            #bestElevator = bestElevatorInformations.bestElevator
            #bestScore = bestElevatorInformations.bestScore
            #referenceGap = bestElevatorInformations.referenceGap

        
        return bestElevator

    def checkIfElevatorIsBetter(self, scoreToCheck, newElevator, bestScore, referenceGap, bestElevator, floor):
        
        if scoreToCheck < bestScore:
            bestScore = scoreToCheck
            bestElevator = newElevator
            referenceGap = abs(newElevator.currentFloor - floor)

        elif bestScore == scoreToCheck:
            gap = abs(newElevator.currentFloor - floor)
            if referenceGap > gap:
                bestElevator = newElevator
                referenceGap = gap

        return bestElevator, bestScore, referenceGap

class Elevator:
    def __init__(self, _id, _amountOfFloors):
        #super(Column, self).__init__(self, _id, _amountOfFloors)
        self.ID = _id
        self.status = ""
        self.currentFloor = ""
        self.direction = "null" # a verifier
        self.door = Door(_id) # removed "closed" because of status change error
        self.floorRequestButtonList = []
        self.floorRequestList = []
        

        self.createFloorRequestButtons(_amountOfFloors)

    def createFloorRequestButtons(self, _amountOfFloors):
        floorRequestButtonID = 1
        buttonFloor = 1
        for i in range(0, _amountOfFloors):
            floorRequestButton = FloorRequestButton(floorRequestButtonID, buttonFloor) # before "OFF" between floorrequest and button
            self.floorRequestButtonList.append(floorRequestButton)
            buttonFloor += 1 
            floorRequestButtonID += 1

    def requestFloor(self, floor):
        self.floorRequestList.append(floor)
        self.move()
        self.operateDoors()

    

    def move(self):
        while not self.floorRequestList:
            destination = self.floorRequestList[0]
            print("PRINT-----")
            print(self.floorRequestList)
            self.status = "moving"
            if (self.currentFloor < destination):
                self.direction = "up"
                self.sortFloorList()
                while (self.currentFloor < destination):
                    self.currentFloor += 1
                    self.screenDisplay = self.currentFloor

            elif (self.currentFloor > destination):
                self.direction = "down"
                self.sortFloorList()
                while (self.currentFloor > destination):
                    self.currentFloor -= 1
                    self.screenDisplay = self.currentFloor

            self.status = "stopped"
            self.floorRequestList.pop(0) #removes the first element of an array

        self.status = "idle"
        self.floorRequestList = []


    def sortFloorList(self):
        if self.direction == "up":
            self.floorRequestList.sort()

        else:
            self.floorRequestList.reverse()

    def operateDoors(self):
        self.door.status = "opened"
        # setTimeout(5000)
        if (self.door.status != "overweight"):
            self.door.status = "closing"
            if (self != "Obstruction"):
                self.door.status = "closed"

            else:
                self.operateDoors

        else:
            while self == "overweight":
               print("Overweight")
            self.operateDoors()
            
            

class CallButton:
    def __init__(self, _id, _floor, _direction):
        self.ID = _id
        self.status = ""
        self.floor = _floor
        self.direction = _direction

class FloorRequestButton:
    def __init__(self, _id, _floor ):
        self.ID = _id
        self.status = ""
        self.floor = _floor

class Door:
    def __init__(self, _id):
        self.ID = _id
        self.status = ""



#module.exports = { Column, Elevator, CallButton, FloorRequestButton, Door}