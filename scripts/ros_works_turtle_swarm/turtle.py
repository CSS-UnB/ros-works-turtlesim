import numpy as np
import rospy
from turtlesim.srv import Spawn
from turtlesim.srv import Kill
from turtlesim.srv import SetPen

from turtle_closed_loop import TurtleClosedLoop

def kill_turtle(turtlename):
    kill = rospy.ServiceProxy("kill", Kill)
    kill(turtlename)

class Turtle():
    ''' Turtle instance '''
    def __init__(self, name):
        self.x = 0
        self.y = 0
        self.theta = 0
        self.name = name
        self.movements = TurtleClosedLoop(self.name)

    def set_param(self, x, y, theta, name):
        ''' Set turtle initial parameters '''
        self.x = x
        self.y = y
        self.theta = theta
        self.name = name

    def spawn_turtle(self):
        ''' Spawn Turtle '''
        self.spawn = rospy.ServiceProxy("spawn", Spawn) #TODO: TRATAR NOMES DIFERENTES
        self.name_sys = self.spawn(self.x, self.y, self.theta, self.name)

    def kill(self):
        ''' Remove essa tartaruga '''
        kill_turtle(self.name)

    def random_pen_color(self, width=5):
        ''' Choose a random dark color for turtle pen '''
        rgb = list(np.random.choice(range(200), size=3))
        self.pen_handle = rospy.ServiceProxy(self.name+"/set_pen", SetPen)
        self.pen_handle(rgb[0], rgb[1], rgb[2], width, False)

    def move_to_point(self, x, y, vel=1, kp=1):
        ''' Move turtle to point '''
        self.movements.go_to_point(x, y, vel, kp)
