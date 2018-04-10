#!/usr/bin/env python
# coding: utf-8
import rospy
import turtle_closed_loop

def recebe_valor():
    ''' Função que recebe valor e verifica por ctrl C '''
    try:
        valor = input()
    except KeyboardInterrupt:
        pass
    return valor

def interface_usuario():
    ''' Interface de Usuario Principal '''
    print 'Aonde deseja ir?'
    print 'X: '
    x = recebe_valor()
    print 'Y: '
    y = recebe_valor()
    return x, y

if __name__ == '__main__':
    ''' Nó executável para o controle em malha fechada '''
    rospy.init_node('turtle_closed_loop')

    turtle = turtle_closed_loop.TurtleClosedLoop()

    while not rospy.is_shutdown():
        try:
            x, y = interface_usuario()
            turtle.run(x, y)
        except rospy.ROSInterruptException:
            pass
