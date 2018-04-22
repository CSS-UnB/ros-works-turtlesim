from turtle import Turtle
import turtle
import math

class TurtleManage:
    ''' Classe de gestao de multiplas tartarugas '''
    def __init__(self):
        ''' Construtor da classe '''
        # remove tartaruga inicial da simulacao
        turtle.kill_turtle('turtle1') #TODO: TRATAR SE A TURTLE! JA FOI APAGADA
        self.turtleList = []   # lista de tartarugas vivas

    def list_turtles(self):
        ''' Lista nomes das tartarugas '''
        print 'Turtles in Workspace: '
        print [turtle.name for turtle in self.turtleList]

    def get_turtle(self, name):
        for turtle in self.turtleList:
            if turtle.name == name:
                return turtle
        print 'Turtle not found'
        return False

    def pop_turtle(self, name):
        ''' Remove tartaruga da lista '''
        #[self.turtleList.remove(turtle) for turtle in self.turtleList if turtle.name != name]
        # TODO: nao esta funcionando
        pass

    def create_turtle(self, x, y, theta, name):
        '''Funcao que cria uma nova turtle e a adiciona a turtleList '''
        new_turtle = Turtle(name)
        new_turtle.set_param(x, y, theta, name)
        new_turtle.spawn_turtle()
        self.turtleList.append(new_turtle)
        print '{} created!\n\n'.format(new_turtle.name)
        return new_turtle

    def kill_turtle(self, victim_name):
        ''' Funcao que remove uma tartaruga da simulacao '''
        turtle.kill_turtle(victim_name)
        print '{} killed!\n\n'.format(victim_name)
        self.pop_turtle(victim_name)

class TurtleSwarm(TurtleManage):
    ''' Classe de comando de multiplas tartarugas '''
    def __init__(self):
        ''' Construtor da classe '''
        TurtleManage.__init__(self) # calls parent class constructor

    def proportional_demo(self):
        ''' Demonstrates influence of proportional gain on movement.
        Creates turtle called CSS on point (2.5,2.5) and make it move to (7.5,7.5).
        Asks for user input of how much should the proportional gain be.
        '''
        # Creates turtle
        turtle_name = 'CSS'
        coord_x1, coord_y1 = 2.5, 2.5
        coord_theta = -3*math.pi/4 # -135 degrees
        # Check if turtle exists
        css_turtle = self.get_turtle(turtle_name)
        if(not css_turtle):
            css_turtle = self.create_turtle(coord_x1, coord_y1, coord_theta, turtle_name)
        # Ask for proportional gain
        value = raw_input('Proportional gain >> ')
        kp = float(value)
        # Move to (7.5, 7.5)
        coord_x2, coord_y2 = 7.5, 7.5
        css_turtle.move_to_point(coord_x2, coord_y2, 1, kp)
        # Move back to (2.5, 2.5)
        css_turtle.move_to_point(coord_x1, coord_y1, 1, kp)
