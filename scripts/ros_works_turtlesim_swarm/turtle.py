import rospy
from turtlesim.srv import Spawn
from turtlesim.srv import Kill

def kill_turtle(turtlename):
    kill = rospy.ServiceProxy("kill", Kill)
    kill(turtlename)

class Turtle():
    def __init__(self):
        self.x = 0
        self.y = 0
        self.theta = 0
        self.name = ''

    def set_param(self, x, y, theta, name = ''):
        self.x = x
        self.y = y
        self.theta = theta
        self.name = name

    def spawn_turtle(self):
        self.spawn = rospy.ServiceProxy("spawn", Spawn) #TODO: TRATAR NOMES DIFERENTES
        self.name = self.spawn(self.x, self.y, self.theta, self.name)

    def kill(self):
        kill_turtle(self.name)
