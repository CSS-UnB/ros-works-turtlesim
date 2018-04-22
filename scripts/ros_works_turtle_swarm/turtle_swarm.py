from menu import Menu
from turtle import Turtle
import turtle

class TurtleManage:
    ''' Classe de gestao de multiplas tartarugas '''
    def __init__(self):
        ''' Construtor da classe '''
        # remove tartaruga inicial da simulacao
        turtle.kill_turtle('turtle1') #TODO: TRATAR SE A TURTLE! JA FOI APAGADA
        self.turtleList = []   # lista de tartarugas vivas
        self.menu = Menu()

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

    def run(self):
        ''' Funcao principal da TurtleSwarm
        O menu retorna um valor inteiro que representa a operacao que o usuario deseja realizar.
        '''
        option = self.menu.print_menu()
        if option == 1:
            # Create Turtle
            self.list_turtles()
            turtle_name = self.menu.get_name('\nChoose your turtle`s name:\n>> ')
            coord_x = self.menu.get_value('- X position >> ')
            coord_y = self.menu.get_value('- Y position >> ')
            coord_theta = self.menu.get_value('- Orientation >> ')
            self.create_turtle(coord_x, coord_y, coord_theta, turtle_name)
        if option == 2:
            # Kill turtle
            self.list_turtles()
            turtle_name = self.menu.get_name('\nType the name of turtle you want to kill:\n>> ')
            self.kill_turtle(turtle_name)
        if option == 3:
            # Move turtle
            self.list_turtles()

            turtle_name = self.menu.get_name('\nType the name of turtle you want to move:\n>> ')
            turtle = self.get_turtle(turtle_name)
            coord_x = self.menu.get_value('- X position >> ')
            coord_y = self.menu.get_value('- Y position >> ')

            turtle.move_to_point(coord_x, coord_y)
