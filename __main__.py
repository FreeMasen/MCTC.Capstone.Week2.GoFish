'''Main Go Fish module'''
from src.UI import UserInterface
def main():
    '''The main entry point for the game Go Fish'''
    ui = UserInterface()
    ui.welcome()

if __name__ == '__main__':
    main()
