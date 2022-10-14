elevatorID = 1
floorRequestButtonID = 1
callButtonID = 1

class Column:
    def __init__(self, _ID, _amountOfFloors, _amountOfElevators):
        self.ID = _ID
        self.status = ""
        self.elevatorList = []
        self.callButtonList = []
        self.floorRequestList = []
        self.createElevators(_amountOfFloors, _amountOfElevators)
        self.createCallButtons(_amountOfFloors)

    # Button press function, Up or Down
    def createCallButtons(self, _amountOfFloors):
       global elevatorID
       global callButtonID
       global floorRequestButtonID
       buttonFloor = 1

       for i in range(_amountOfFloors):
        if buttonFloor < _amountOfFloors:
         callButton = CallButton(callButtonID, buttonFloor, "Up")
         self.callButtonList.append(callButton)
         callButtonID += 1

        if buttonFloor > 1:
         callButton = CallButton(callButtonID, buttonFloor, "Down")
         self.callButtonList.append(callButton)
         callButtonID += 1
        buttonFloor += 1

    # Create Elevator function for the different scenarios
    def createElevators(self, _amountOfFloors, _amountOfElevators):
        global elevatorID
        global callButtonID
        global floorRequestButtonID
        
        for i in range(_amountOfElevators):# a verifier
            elevator = Elevator(elevatorID, _amountOfFloors)
            self.elevatorList.append(elevator)
            elevatorID += 1

    # Simulate when a user press a button outside the elevator
    def requestElevator(self, floor, direction):
        elevator = self.findElevator(floor, direction)
        elevator.floorRequestList.append(floor) #<-----
        elevator.move()
        elevator.operateDoors()
        elevator.floorRequestList = []
        return elevator

    #We use a score system depending on the current elevators state. Since the bestScore and the referenceGap are 
    #higher values than what could be possibly calculated, the first elevator will always become the default bestElevator, 
    #before being compared with to other elevators. If two elevators get the same score, the nearest one is prioritized.
    def findElevator(self, requestedFloor, requestedDirection):
        bestElevator = None
        bestScore = 5
        referenceGap = 10000000
        
        for elevator in self.elevatorList:
            
            #The elevator is at my floor and going in the direction I want
            if requestedFloor == elevator.currentFloor and elevator.status == "stopped" and requestedDirection == elevator.direction:
                bestElevator, bestScore, referenceGap = self.checkIfElevatorIsBetter(1, elevator, bestScore, referenceGap, bestElevator, requestedFloor)
            #The elevator is lower than me, is coming up and I want to go up
            elif requestedFloor > elevator.currentFloor and elevator.direction == "up" and requestedDirection == elevator.direction:
                bestElevator, bestScore, referenceGap = self.checkIfElevatorIsBetter(2, elevator, bestScore, referenceGap, bestElevator, requestedFloor)
            #The elevator is higher than me, is coming down and I want to go down
            elif requestedFloor < elevator.currentFloor and elevator.direction == "down" and requestedDirection == elevator.direction:
                bestElevator, bestScore, referenceGap = self.checkIfElevatorIsBetter(2, elevator, bestScore, referenceGap, bestElevator, requestedFloor)
            #The elevator is idle
            elif elevator.status == "idle":
                bestElevator, bestScore, referenceGap = self.checkIfElevatorIsBetter(3, elevator, bestScore, referenceGap, bestElevator, requestedFloor)
            #The elevator is not available, but still could take the call if nothing better is found        
            else:
                bestElevator, bestScore, referenceGap = self.checkIfElevatorIsBetter(4, elevator, bestScore, referenceGap, bestElevator, requestedFloor)
        return bestElevator

    # Select the closest/best elevator to do the scenario
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
        self.ID = _id
        self.status = ""
        self.currentFloor = 1
        self.direction = "null"
        self.door = Door(_id) 
        self.floorRequestButtonList = []
        self.floorRequestList = []
        self.createFloorRequestButtons(_amountOfFloors)

    # Push the request demands in lists 
    def createFloorRequestButtons(self, _amountOfFloors):
        global floorRequestButtonID
        buttonFloor = 1
        for i in range(_amountOfFloors):
            floorRequestButton = FloorRequestButton(floorRequestButtonID, buttonFloor) 
            self.floorRequestButtonList.append(floorRequestButton)
            buttonFloor += 1 
            floorRequestButtonID += 1

    # Simulate when a user press a button inside the elevator
    def requestFloor(self, floor):
        self.floorRequestList.append(floor)
        self.move()
        self.operateDoors()

    # Move elevator to the direction based on what floor we are currently
    def move(self):
        while len(self.floorRequestList) != 0:
            destination = self.floorRequestList[0]
            self.status = "moving"
            if (self.currentFloor < destination):
                self.direction = "up"
                self.sortFloorList()
                while self.currentFloor < destination:
                    self.currentFloor += 1
                    self.screenDisplay = self.currentFloor
            elif (self.currentFloor > destination):
                self.direction = "down"
                self.sortFloorList()
                while (self.currentFloor > destination):
                    self.currentFloor -= 1
                    self.screenDisplay = self.currentFloor
            self.status = "stopped"
            self.floorRequestList.pop(0) 
        self.status = "idle"
        self.floorRequestList = []

    # Sort list function to pick up other requests mid destination
    def sortFloorList(self):
        if self.direction == "up":
            self.floorRequestList.sort()

        else:
            self.floorRequestList.reverse()

    # Alert preventing doors obstructions and overweight oad in the elevator
    def operateDoors(self):
        self.door.status = "opened"
        
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
