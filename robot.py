import turtle

"""
Initialize the turtle robot
"""
def initialize_robot():
    robot = turtle.Turtle()
    robot.color("blue")

    return robot

"""
Move robot forward, backward, left, right
"""
def go_forward(robot):
    robot.forward(1)

def go_backward(robot):
    robot.backward(1)

def turn_left(robot):
    robot.left(1)

def turn_right(robot):
    robot.right(1)
