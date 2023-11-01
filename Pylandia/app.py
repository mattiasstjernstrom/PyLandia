import os
import sys
# from Pylandia.Components.combat import test_combat # Import to test combat

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

def run():
    print('Game is running!')

if __name__ == '__main__':
    run()
    # test_combat() # Import to test combat