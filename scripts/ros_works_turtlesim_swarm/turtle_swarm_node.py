#!/usr/bin/env python
import rospy
import turtle
import menu

def main():
    rospy.init_node('turtle_swarm')

    menu_ = menu.Menu()

    while not rospy.is_shutdown():
        try:
            menu_.print_menu()

        except rospy.ROSInterruptException:
            pass

if __name__ == '__main__':
    main()
