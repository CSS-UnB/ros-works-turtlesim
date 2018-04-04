from turtle import Turtle, kill_turtle

class Menu():
    def __init__(self):
        kill_turtle('turtle1') #TODO: TRATAR SE A TURTLE! JA FOI APAGADA
        self.print_menu()
        self.turtleList = []        #Armazena as turtle vivas
        #pass

    def print_menu(self):
        print '--------- ROS WORKS TURTLESIM SWARM --------- (v0.1)'
        print '1 - Create turtle'
        print '2 - Kill turtle'

        self.get_option()
        self.call_option()

    def get_option(self):
        self.option = raw_input('\nChoose an option:\n>> ')
        self.option = int(self.option)

    def call_option(self):
        if self.option == 1:
            new_turtle = Turtle()
            #new_turtle.set_param()
            spawn_name = raw_input("\nChoose your turtle's name:\n>> ")
            new_turtle.spawn(spawn_name)
            self.turtleList.append(new_turtle)
            print '{} created!\n\n'.format(new_turtle.name)

        elif self.option == 2:
            killing_name = raw_input('\nType the name of turtle you want to kill:\n>> ')
            killing_name = str(killing_name)
            kill_turtle(killing_name)
            print '{} killed!\n\n'.format(killing_name)
