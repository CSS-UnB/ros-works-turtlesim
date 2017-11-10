#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
import math

class TurtleClosedLoop:
    ''' Classe para o controle de malha fechada da tartaruga '''
    def __init__(self):
        self.vel = 1
        self.pub = rospy.Publisher('turtle1/cmd_vel', Twist, queue_size = 1)
        self.rate = rospy.Rate(10) #Hertz
        rospy.Subscriber("turtle1/pose", Pose, self.callback)
        self.turtle_x = 0
        self.turtle_y = 0
        self.turtle_theta = 0
        self.turtle_linear_velocity = 0
        self.turtle_angular_velocity = 0

    def callback(self, msg):
        self.turtle_x = msg.x
        self.turtle_y = msg.y
        self.turtle_theta = msg.theta
        self.turtle_linear_velocity = msg.linear_velocity
        self.turtle_angular_velocity = msg.angular_velocity
        # print 'x = ',self.turtle_x,'\ny = ',self.turtle_y

    def move_angular(self, vel):
        vel_msg = Twist()
        vel_msg.angular.z = vel
        self.pub.publish(vel_msg)
        turtle.rate.sleep()

    def move_linear(self, vel):
        print 'Move turtle'
        vel_msg = Twist()
        vel_msg.linear.x = vel
        self.pub.publish(vel_msg)
        turtle.rate.sleep()

    def stop(self):
        vel_msg = Twist()
        self.pub.publish(vel_msg)

    def go_to_point(self, x, y):
        ''' Recebe ponto, vai ao ponto '''
        tolerance = 0.1
        diff_x = x - self.turtle_x
        diff_y = y - self.turtle_y
        theta_goal = math.atan2(diff_y, diff_x)
        diff_theta = theta_goal - self.turtle_theta
        while abs(diff_theta) > tolerance:
            self.move_angular(self.vel)
            diff_theta = theta_goal - self.turtle_theta
        self.stop()
        print diff_x, diff_y

        while abs(diff_x) > tolerance or abs(diff_y) > tolerance:
            self.move_linear(self.vel)
            diff_x = x - self.turtle_x
            diff_y = y - self.turtle_y
        self.stop()

    def run(self):
        ''' Funcao principal '''
        while not rospy.is_shutdown():
            try:
                print 'Aonde deseja ir?'
                print 'X: '
                x = input()
                print 'Y: '
                y = input()
                self.go_to_point(x, y)
            except rospy.ROSInterruptException:
                pass

if __name__ == '__main__':

    rospy.init_node('turtle_closed_loop')

    turtle = TurtleClosedLoop()

    turtle.run()
