class Rover:
# initializing the class attributes
    def __init__(self, x, y,heading):
        """
        initializing parameters
        """
        self.xpos = x
        self.ypos = y
        self.heading = self.headers(heading)
        # attribute getter method.
    def getPos (self):
        return self.xpos, self.ypos, self.heading
         # attribute getter method.
    def setPos (self, x , y, z):
        self.xpos = x
        self.ypos = y
        self.heading = z
        # the parameters in the move function represent the instructions i.e MLR and 
        # the maximum and minimum size of the grid that the rover can move which is 5 by 5. 
        # the move function also executes forward or turn right or left movements.
    def move(self, command, maxX, maxY):
        x,y,z = self.getPos()

        for c in command: # iterate through all the commands/instructions given to the rover.

            x,y,z = self.getPos()
            # x : is the position in the x-axis.
            # y : is the position in the y-axis.
            # z : represents the direction the rover is facing.
            if c in 'MLR': # check if the command is valid.
                if c == 'M':
                    # check if a move can be made before making it.
                    if z ==0:
                        if self.validate(maxY,y+1): 
                            self.setPos(x,y+1,z)
                    elif z ==1:
                        if self.validate(maxX,x+1):
                            self.setPos(x+1,y,z)
                    elif z ==2:
                        if self.validate(maxY,y-1):
                            self.setPos(x,y-1,z)
                    elif z ==3:
                        if self.validate(maxY,x-1):
                            self.setPos(x-1,y,z)
                 
                elif c == 'L': # L initiates anticlockwise rotation by 90 degrees. This should increment the number and reset itself when necessary.
                    a=(z-1)%4
                    self.setPos(x,y,a)

                elif c == 'R': # R initiates clockwise rotation by 90 degrees. This should increment the number and reset itself when necessary.
                    a=(z+1)%4
                    self.setPos(x,y,a) 
                

    def validate(self,maxX, z):
        # checks whether a move violates plateau size.
        if z <=maxX and z>=0:
            return True
        else :
            return False
       
    def headings(self,c): # converts direction to number notation N=0, E=1, S=2, W=3 
        if c == 0:
            return 'N'
        elif c == 1:
            return 'E'
        elif c == 2:
            return 'S'
        elif c == 3:
            return 'W'
        else :
            return 'invalid'

    def headers(self, c): # converts direction to direction notation N=0, E=1, S=2, W=3 
        if c == 'N':
            return 0
        elif c == 'E':
            return 1 
        elif c == 'S':
            return 2
        elif c == 'W':
            return 3
        else :
            return 'invalid'

    def dispThis(self): # shows the current rover position and orientation.
        x,y,z = self.getPos()
        return [x,y,self.headings(z)]

if __name__ == '__main__':
    rovers = 2 # assume a case of two rovers.
    result = []
    xmax, ymax = map(int, input('plateau grid size:').split()) # collect plateau size and extract coordinates.

    for _ in range(rovers):
        # get rover coordinates and N-E-S-W bearing.
        x, y, bearing = input('coordinates for rover{}:' .format(_+1)).split() # collect rover coordinates and bearing.
        rover = Rover(int(x), int(y), bearing) # create an instance of the rover class for each rover. 
        print(rover.getPos())
        instruction = input("instructions for rover:") # collect rover instructions.
        rover.move(instruction,xmax,ymax) # execute instructions.
        r = rover.dispThis() # display the rover position.
        result.append(r)

    for x in result:
        print(x)

