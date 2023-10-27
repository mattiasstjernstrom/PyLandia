import os
import sys
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from Entities.common.Combat import run_game


def run():
    run_game()

if __name__ == '__main__':
    run()