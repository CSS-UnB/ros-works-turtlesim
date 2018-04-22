#!/usr/bin/env python
# coding: utf-8

import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
import math

from turtle_kinematics import TurtleKinematics

class TurtleClosedLoop(TurtleKinematics):
    ''' Classe para o controle de malha fechada da tartaruga.
    Torna-se possível fechar a malha por meio do callback no "tópico turtle1/pose".
    Ele fornece a posição atual da tartaruga dentro da simulação.
    '''
    def __init__(self, turtle_name='turtle1'):
        ''' Construtor da classe TurtleClosedLoop '''
        TurtleKinematics.__init__(self, turtle_name) # calls parent class constructor
        # parametros de movimento
        self.kp = 1
        self.vel = 1
        # Elemento subscriber ROS
        rospy.Subscriber(turtle_name+'/pose', Pose, self.callback)
        # inicializacao de variaveis recebidas no callback
        self.turtle_x = 0
        self.turtle_y = 0
        self.turtle_theta = 0
        self.turtle_linear_velocity = 0
        self.turtle_angular_velocity = 0

    def callback(self, msg):
        ''' Funcao chamada toda a vez que atualiza-se o topico: turtle1/pose '''
        self.turtle_x = msg.x
        self.turtle_y = msg.y
        self.turtle_theta = msg.theta
        self.turtle_linear_velocity = msg.linear_velocity
        self.turtle_angular_velocity = msg.angular_velocity
        # print 'x = ',self.turtle_x,'\ny = ',self.turtle_y

    def go_to_point(self, x, y):
        '''
            Recebe ponto, vai ao ponto.
            Realiza um controle proporcional da orientacao da tartaruga, enquanto se move em velocidades constantes.
            A velocidade padrao e self.vel
            O ganho proporcional e self.kp
        '''
        tolerance = 0.1
        diff_x = x - self.turtle_x
        diff_y = y - self.turtle_y
        theta_goal = math.atan2(diff_y, diff_x)
        diff_theta = theta_goal - self.turtle_theta
        while abs(diff_x) > tolerance or abs(diff_y) > tolerance:
            diff_x = x - self.turtle_x
            diff_y = y - self.turtle_y
            theta_goal = math.atan2(diff_y, diff_x)
            diff_theta = theta_goal - self.turtle_theta
            self.move_general(self.vel , self.kp * diff_theta)

        self.stop()

    def run(self, x, y):
        '''
            Funcao principal da classe
            Recebe dois valores float x e y.
            Os valores denotam a posicao alvo da tartaruga
        '''
        try:
            self.go_to_point(x, y)
        except rospy.ROSInterruptException:
            pass
