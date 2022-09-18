## Problem one : Mars Rover

A squad of robotic rovers are to be landed by NASA on a plateau on Mars. This plateau, which is curiously rectangular, must be navigated by the rovers so that their onboard cameras can get a complete view of the surrounding terrain to send back to Earth. A rover's position is represented by a combination of an x and y coordinates and a letter representing one of the four cardinal compass points. The plateau is divided up into a grid to simplify navigation. An example position might be 0, 0, N, which means the rover is in the bottom left corner and facing North. In order to control a rover, NASA sends a simple string of letters. The possible letters are 'L', 'R' and 'M'. 'L' and 'R' makes the rover spin 90 degrees left or right respectively, without moving from its current spot. 'M' means move forward one grid point, and maintain the same heading. Assume that the square directly North from (x, y) is (x, y+1).

## Input

The first line of input is the upper-right coordinates of the plateau, the lower-left coordinates are assumed to be 0,0. The rest of the input is information pertaining to the rovers that have been deployed. Each rover has two lines of input. The first line gives the rover's position, and the second line is a series of instructions telling the rover how to explore the plateau. The position is made up of two integers and a letter separated by spaces, corresponding to the x and y co-ordinates and the rover's orientation. Each rover will be finished sequentially, which means that the second rover won't start to move until the first one has finished moving.

## Output

The output for each rover should be its final coordinates and heading.

## The following is the test Input

```
5 5   # This is the grid size.

1 2 N   # This is the position coordinate of the first rover.
LMLMLMLMM  #This represent the movements of the second rover. 

3 3 E   # This is the position coordinate of the second rover.
MMRMMRMRRM   # This represent the movements of the second rover. 
```

## The following is expected Output

```
1 3 N   # Output of the first rover.
5 1 E  # Output of the second rover.
```

## Steps followed
The steps below have been well commented in the mars-rover-solution program which is inline with the design i used to approach this particular problem.
* Assume a case of two rovers.
* Create an instance of the rover class for each rover.
* Define the positions of the axis both x and y and the bearing. 
* Define the moves i.e forward, left or right.
* Check if a move can be made before making it.
* Iterate through all the commands/instructions given to the rover.
* Checks whether a move violates plateau size.
* Collect the plateau grid size.
* Collect rover coordinates and bearing.
* Collect rover instructions/movements.
* Execute the rover instructions.
* Display the rover position as the ouput.


## How to run this project

* You will need to clone this repository if you already have Python 3.6 and higher versions.
* When prompted, please type file name i.e filename sampleIn.txt, sampleIn2.txt etc

```sh
git clone https://github.com/EugeneGitonga/mars-rover-solution.git
cd mars-rover-solution/mars_rover_main/solution
python3 mars_rover_solution.py

```
* When asked for input you should key in as seen in the above test input section in that sequence.


## Run this project in docker

```sh
$ docker-compose up
$ docker-compose exec app python3 mars_rover_solution.py
```

## Testing this project

* The tests use the Python built-in `unittest` module and are located in file `mars-rover-test.py`. 
* To run the tests, just run the file as common Python code:

```sh
python3 mars-rover-test.py

```

## Recommendations

* Have a graphical representation of both the plateau grid and the rovers for easier understanding of the problem.


## Hypothesis

* The inputs given are fixed in the program.
* The grid size given is the maximum size and the rovers have to be within the grid.
* The inputs given are in the order of plateau grid size followed by the position of rover and last section is the movement commands.
