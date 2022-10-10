import win32api
import time

elevatorID = 1
floorRequestButtonID = 1
callButtonID = 1

class Column:
    def __init__(_id, _status, _amountOfFloors, _amountOfElevators):
        self.id = _id
        self.status = _status
        self.elevatorList = []
        self.callButtonList = []

        self.createElevators(_amountOfFloors, _amountOfElevators)
        self.createCallButtons(_amountOfFloors)

    def createCallButtons(_amountOfFloors):
       buttonFloor = 1
       for i in _amountOfFloors:

        if i < _amountOfFloors:
         callButton = CallButton(callButtonID, OFF, buttonFloor, buttonFloor)
         self.callButtonList.append(callButton)
         callButtonID += 1

        if (buttonFloor > 1):
         callButton = CallButton(callButtonID, OFF, buttonFloor, Down)
         callButtonList.append(callButton)
         callButtonID += 1

        buttonFloor += 1

     

    def createElevators(_amountOfFloors, _amountOfElevators):
        
        for elevator  in _amountOfElevators:
            elevator = Elevator(elevatorID, idle, _amountOfFloors, 1)
            self.elevatorList.append(elevator)
            elevatorID+= 1


    def requestElevator(floor, direction, elevator):
        elevator = self.findElevator(floor, direction, elevator)
        requestList.push(elevator)
        elevator(move)
        elevator(operateDoors)
        return elevator


    def findElevator(requestedFloor, requestedDirection, bestElevator):
        bestElevator
        bestScore = 5
        referenceGap = 10000000
        bestElevatorInformations
        for elevator in self.elevatorsList:
            if requestedFloor == Elevator.currentFloor and Elevator.status == stopped and requestedDirection == Elevator.direction:
                bestElevatorInformations = self.checkIfElevatorIsBetter(1, elevator, bestScore, referenceGap, bestElevator, requestedFloor, bestElevatorInformations)

            elif requestedFloor > Elevator.currentFloor and Elevator.direction == Up and requestedDirection == Elevator.direction:
                bestElevatorInformations = self.checkIfElevatorisBetter(2, elevator, bestScore, referenceGap. bestElevator, requestedFloor, bestElevatorInformations)

            elif requestedFloor < Elevator.currentFloor and Elevator.direction == down and requestedDirection == Elevator.direction:
                bestElevatorInformations = self.checkIfElevatorisBetter(2, elevator, bestScore, referenceGap. bestElevator, requestedFloor, bestElevatorInformations)

            elif Elevator.status == idle:
                bestElevatorInformations = self.checkIfElevatorisBetter(3, elevator, bestScore, referenceGap. bestElevator, requestedFloor, bestElevatorInformations)
            else:
                bestElevatorInformations = self.checkIfElevatorisBetter(4, elevator, bestScore, referenceGap. bestElevator, requestedFloor, bestElevatorInformations)
            
            bestElevator = bestElevatorInformations.bestElevator
            bestScore = bestElevatorInformations.bestScore
            referenceGap = bestElevatorInformations.referenceGap

        return bestElevator

    def checkIfElevatorIsBetter(scoreToCheck, newElevator, bestScore, referenceGap, bestElevator, floor, bestElevatorInformations):
        if (scoreToCheck < bestScore):
            bestScore = scoreToCheck
            bestElevator = newElevator
            referenceGap = newElevator.currentFloor - floor; #a verifier ABSOLUTE VALUE?

        elif (bestScore == scoreToCheck):
            gap = newElevator.currentFloor - floor
            if (referenceGap > gap):
                bestElevator = newElevator
                referenceGap = gap

        return bestElevator and bestScore and referenceGap.bestElevatorInformations # a verifier AS ?


class Elevator:
    def __init__(_id, _status, _amountOfFloors, _currentFloor):
        self.id = _id
        self.status = _status
        self. currentFloor = _currentFloor
        self.direction = null
        self.door = Door(_id, closed)
        self.floorRequestButtonList = []
        self.floorRequestList = []

        self.createFloorRequestButtons(_amountOfFloors)

    def createFloorRequestButtons(_amountOfFloors):
        buttonFloor = 1
        for i in _amountOfFloors:
            floorRequestButton = FloorRequestButton(floorRequestButtonID, OFF, buttonFloor)
            self.floorButtonsList.push(floorRequestButton)
            buttonFloor += 1
            floorRequestButtonId += 1

    def requestFloor(floor):
        self.requestList.push(floor)
        self.move()
        self.operateDoors()

    def move():
        while (self.requestList != []):
            destination = self.requestList[0]
            self.status = moving
            if self.currentFloor < destination:
                self.direction = up
                self.sortFloorList()
                while (self.currentFloor < destination):
                    self.currentFloor += 1
                    self.screenDisplay = self.currentFloor

                
            elif self.currentFloor > destination:
                self.direction = down
                self.sortFloorList()
                while (self.currentFloor > destination):
                    self.currentFloor -= 1
                    self.screenDisplay = self.currentFloor

            self.status = stopped;
            self.requestList.pop(0) #removes the first element of an array

        self.status = idle

    def sortFloorList():
        if self.direction == up:
            self.requestList.sort()

        else:
            self.requestList.reverse()

    def operateDoors():
        self.door.status = opened
        time.sleep(10) # a remplacer
        if self.door.status != overweight:
            self.door.status = closing
            if not obstruction:
                self.door.status = closed

            else:
                self.operateDoors

        else:
            while (self == overweight): # self instead of this ???
                win32api.MessageBox(0, 'ALERT', 'title')

            self.operateDoors()


class CallButton:
    def __init__(_id, _status, _floor, _direction):
        self.id = _id
        self.status = _status
        self.floor = _floor
        self.direction = _direction

class FloorRequestButton:
    def __init__(_id, _status, _floor):
        self.id = _id
        self.status = _status
        self.floor = _floor

class Door:
    def __init__(_id, _status):
        self.id = _id
        self.status = _status


#module.exports = { Column, Elevator, CallButton, FloorRequestButton, Door }