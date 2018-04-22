from turtle import Turtle, kill_turtle

class Menu():
    ''' Interface de usuario principal do Turtle Swarm '''
    def __init__(self):
        ''' Construtor da classe Menu '''
        pass

    def print_menu(self):
        ''' Imprime menu e retorna opcao escolhida '''
        print '--------- ROS WORKS TURTLESIM SWARM --------- (v0.1)'
        print '1 - Create turtle'
        print '2 - Kill turtle'
        print '3 - Move turtle'

        return self.get_value('\nChoose an option:\n>> ')

    def get_value(self, message):
        ''' Imprime pergunta e recebe valor inteiro '''
        value = raw_input(message)
        value = int(value)
        return value

    def get_name(self, message):
        ''' Imprime pergunta e recebe string '''
        name = raw_input(message)
        name = str(name)
        return name
