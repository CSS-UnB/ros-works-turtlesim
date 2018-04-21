import turtle

class Menu():
    ''' Classe interface de usuario para a movimentacao de tartarugas '''
    def __init__(self):
        pass

    def print_menu(self):
        print '--------- ROS WORKS TURTLESIM SIM --------- (v0.1)'
        print 'Tell us where do you want to go.'
        coord_x = self.get_value('- X position >> ')
        coord_y = self.get_value('- Y position >> ')
        return coord_x, coord_y


    def get_value(self, str):
        ''' Imprime pergunta e recebe valor inteiro '''
        value = raw_input(str)
        value = int(value)
        return value
