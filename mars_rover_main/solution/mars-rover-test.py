import unittest
from mars_rover_solution import Rover

class TestRover(unittest.TestCase):
    def testConstructor(self):

        # Create rover instance with values
        rover = Rover(1, 2 , 'N')
        self.assertEqual(rover.xpos, 1)
        self.assertEqual(rover.ypos, 2)
        self.assertEqual(rover.heading, 0)
        
    def test_turns_rover_left(self):
        rover = Rover(1, 2 , 'N')
        rover.move('L', 5 , 5)
        self.assertEqual(rover.xpos,1)
        self.assertEqual(rover.ypos, 2)
        self.assertEqual(rover.heading, 3)


    def test_turns_rover_right(self):
        rover = Rover(1, 2 , 'N')
        rover.move('R', 5 , 5)
        self.assertEqual(rover.xpos, 1)
        self.assertEqual(rover.ypos, 2)
        self.assertEqual(rover.heading, 1)


    def test_move_directions(self):
        rover = Rover(1, 2 , 'N')
        rover.move('M', 5 , 5)
        self.assertEqual(rover.xpos, 1)
        self.assertEqual(rover.ypos, 3)
        self.assertEqual(rover.heading, 0)



    def test_given_example(self):
        rover = Rover(1, 2 , 'N')
        rover.move('LMLMLMLMM', 5 , 5)
        self.assertEqual(rover.xpos, 1)
        self.assertEqual(rover.ypos, 3)
        self.assertEqual(rover.heading, 0)

        rover = Rover(3, 3 , 'E')
        rover.move('MMRMMRMRRM', 5 , 5)
        self.assertEqual(rover.xpos, 5)
        self.assertEqual(rover.ypos, 1)
        self.assertEqual(rover.heading, 1)

if __name__ == '__main__':
    unittest.main()

