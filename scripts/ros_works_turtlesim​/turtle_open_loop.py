#!/usr/bin/env python
# coding: utf-8

import rospy
from turtlesim.msg import Pose
import math

from turtle_kinematics import TurtleKinematics

class TurtleOpenLoop(TurtleKinematics):
    ''' Classe para o controle em malha aberta da tartaruga.
    O movimento da tartaruga deve se basear na cinematica classica:
        Deslocamento = Velcidade x Temp
    '''
    def __init__(self):
        ''' Construtor da classe TurtleOpenLoop
        Todo metodo da classe deve ter como primeiro parametro o ponteiro da classe (self)

        Analogamente, variaveis inicializadas dentro da classe devem ser chamadas e declaradas
        pelo o prefixo self.var_name.
        '''
        TurtleKinematics.__init__(self) # calls parent class constructor
        # Posicao linear e angular da tartaruga
        self.turtle_pose = Pose(x=0, y=0, theta=0)
        # equivalent to:
        #   self.turtle_pose.x = 0
        #   self.turtle_pose.y = 0
        #   self.turtle_pose.theta = 0

    def move_untill(self, time, vel, ang):
        ''' Realiza movimento durante uma quantidade de tempo definida.
        O movimento eh definido por velocidade angular e velocidade linear.
        O intervalo de tempo, em segundos deve ser informado para a funcao.
        '''
        now = rospy.get_time()
        wait_time = now + time
        rate = rospy.Rate(10) # loop rate (Hz)
        while now < wait_time:
            self.move_general(vel, ang)
            now = rospy.get_time()
            rate.sleep()
        self.stop()

    def turn_theta(self, theta, vel_ang):
        ''' Realiza uma rotacao de theta radianos, com velocidade angular vel_ang '''
        # Estima o tempo pela cinematica
        time = theta/vel_ang
        self.move_untill(time, 0, vel_ang)

    def move_distance(self, distance, vel_lin):
        ''' Move a tartaruga pela distancia dist, com velocidade vel_lin '''
        # Estima o tempo pela cinematica
        time = distance/vel_lin
        self.move_untill(time, vel_lin, 0)

    def go_to_point_relative(self, x, y, vel_lin=0.5, vel_ang=0.5):
        ''' Recebe ponto relativo a tartaruga em 2D e vai ate o ponto.
        Realiza primeiro o movimento angular e depois o linear.
        '''
        theta = math.atan2(y, x)
        distance = math.sqrt(y**2 + x**2)
        self.turn_theta(theta, vel_ang)
        self.move_distance(distance, vel_lin)


    def run(self, x, y):
        '''
            Funcao principal da classe
            Recebe dois valores float x e y.
            Os valores denotam a posicao alvo da tartaruga.
        '''
        try:
            self.go_to_point_relative(x, y)
        except rospy.ROSInterruptException:
            pass
