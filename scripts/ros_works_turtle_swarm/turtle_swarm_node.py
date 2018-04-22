#!/usr/bin/env python
import rospy
from turtle_swarm import TurtleSwarm

def print_menu():
    ''' Imprime menu e retorna opcao escolhida '''
    print '--------- ROS WORKS TURTLESIM SWARM --------- (v0.1)'
    print '1 - Create turtle'
    print '2 - Kill turtle'
    print '3 - Move turtle'

    return get_value('\nChoose an option:\n>> ')

def get_value(message):
    ''' Imprime pergunta e recebe valor inteiro '''
    value = raw_input(message)
    value = int(value)
    return value

def get_name(message):
    ''' Imprime pergunta e recebe string '''
    name = raw_input(message)
    name = str(name)
    return name

def main(turtle_swarm):
    ''' Funcao principal do Node TurtleSwarm '''
    option = print_menu()
    if option == 1:
        # Create Turtle
        turtle_swarm.list_turtles()
        turtle_name = get_name('\nChoose your turtle`s name:\n>> ')
        coord_x = get_value('- X position >> ')
        coord_y = get_value('- Y position >> ')
        coord_theta = get_value('- Orientation >> ')
        turtle_swarm.create_turtle(coord_x, coord_y, coord_theta, turtle_name)
    if option == 2:
        # Kill turtle
        turtle_swarm.list_turtles()
        turtle_name = get_name('\nType the name of turtle you want to kill:\n>> ')
        turtle_swarm.kill_turtle(turtle_name)
    if option == 3:
        # Move turtle
        turtle_swarm.list_turtles()
        turtle_name = get_name('\nType the name of turtle you want to move:\n>> ')
        turtle = turtle_swarm.get_turtle(turtle_name)
        coord_x = get_value('- X position >> ')
        coord_y = get_value('- Y position >> ')
        turtle.move_to_point(coord_x, coord_y)
    if option == 4:
        # CSS logo
        turtle_swarm.CSS_logo()


if __name__ == '__main__':
    rospy.init_node('turtle_swarm_node')
    turtle_swarm = TurtleSwarm()

    while not rospy.is_shutdown():
        try:
            main(turtle_swarm)

        except rospy.ROSInterruptException:
            pass
