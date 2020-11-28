#class programs for OOPs

class Car(): # define Car super class
    def __init__(self, efficiency):
        self._efficiency = efficiency
        self._fuel = 0 #class variables
        self._fuelcheck = 0
        path  = "C:\\Users\\Venki\\Desktop\\Venkat\\Python\\Project 2\\"
        f = open(path + 'FuelEffic.txt' , "r") #open the file in read mode
        lines = f.readlines() #read lines
        print("Miles per gallon:",lines[0].split()[3]) #print the miles in line
        print("Tank Size (in gallons): ",lines[1][len(lines[1])-2:])
        self._milage = int(lines[0].split()[3]) # assigns details to class variables
        self._tankSize = int(lines[1][len(lines[1])-2:])
        self._totaldistance = self._milage * self._tankSize
        print("Maximum Distance %0.2f miles"%self._totaldistance) #max distance the car can travel with full tank
        f.close #close the file

    def addGas(self,gas):
        self._fuelcheck=self._fuel + (gas) #temporary variable 
        if(self._fuelcheck>self._tankSize): #check if fuel to be added more than the tank size
            #print("Tank full, will be adding", (self._fuel + gas- self._tankSize)  )
            self._addnew = gas - (self._fuelcheck- self._tankSize) #calculate gas that can be added
            print("Tank would be full with", self._addnew, 'gallons')
            self._fuel= (self._fuel +  self._addnew) #new gas level
            return self._addnew
        else:
            self._fuel=self._fuel + (gas) #add the gas to tank
            return gas
            #print("Total fuel there", self._fuel) 

    def drive(self,distance):
        self._totaldistance = (self._milage*self._fuel) #updated distance based on updated gas level
        if self._fuel == 0: #if tank empty return distance tavelled as zero
            print("Tank empty")
            return self._totaldistance
        elif self._fuel >0:
            if distance > self._totaldistance:
                #print("Can drive only miles",self._totaldistance)
                self._fuel = (self._totaldistance- self._totaldistance)/self._efficiency #updated fuel level
                self._newdist = self._totaldistance
                self._totaldistance = (self._milage*self._fuel) #new distance based on updated gas level
                return self._newdist # return distance the car can travel
            else:
                self._fuel = (self._totaldistance-float(distance))/self._efficiency #updated fuel level
                #print("New tank size", self._fuel)
                self._totaldistance = (self._milage*self._fuel) #new distance based on updated gas level
                #print(self._totaldistance)
                return distance #distance can travelled

    def getfuellevel(self):
        return self._fuel  #return gas level of car
  