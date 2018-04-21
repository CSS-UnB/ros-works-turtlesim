#!/usr/bin/env python
# coding: utf-8
import rospy
from turtle_open_loop import TurtleOpenLoop
from menu import Menu

def main():
    ''' Nó executável para o controle em malha aberta '''
    rospy.init_node('turtle_open_loop')

    menu = Menu()
    turtle = TurtleOpenLoop()

    while not rospy.is_shutdown():
        try:
            coord_x, coord_y = menu.print_menu()
            turtle.run(coord_x, coord_y)
        except rospy.ROSInterruptException:
            pass

if __name__ == '__main__':
    main()
