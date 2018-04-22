from turtle import Turtle
import turtle

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
        return ''

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

    def CSS_logo(self):
        pass
