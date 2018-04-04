#!/usr/bin/env python
import rospy
from turtle import Turtle
from menu import Menu

def main():
    rospy.init_node('turtle_swarm')

    menu_ = Menu()

    while not rospy.is_shutdown():
        try:
            menu_.print_menu()

        except rospy.ROSInterruptException:
            pass

if __name__ == '__main__':
    main()
