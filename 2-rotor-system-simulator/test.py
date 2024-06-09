from multiprocessing import Process
from os import system
from pathlib import Path
from sys import path as sys_path
from time import time
from typing import Any


# Define directories
BASE_DIR = Path(__file__).parent.absolute()
SRC_DIR = BASE_DIR / "src"

# Import rotor simulator solution module
sys_path.append(str(SRC_DIR))
rotor_sim = __import__("rotor_sim")


# Set up Python rotor simulator
def show_rotor(rotors: Any):
    # print(rotors, end="\r")
    pass


rotor_sim = rotor_sim.RotorSim(show_rotor)
rotors = [0]
rotor_size = 10
rotors_max_num = 7


# Set up C rotor simulator
system(f"gcc {str(SRC_DIR / 'rotor_sim.c')} -o {str(SRC_DIR / 'rotor_sim.out')}")


def c_breaker():
    start = time()
    system(f"{str(SRC_DIR / 'rotor_sim.out')}")
    print(f"time to completion: {time()-start}\n")


# Run both sims in parallel
for x in range(5):
    print(f"\n{x+1}. ---------------------------------\n")

    py_breaker_process = Process(
        target=rotor_sim.f3, args=(rotors, rotor_size, rotors_max_num)
    )
    c_breaker_process = Process(target=c_breaker)

    py_breaker_process.start()
    c_breaker_process.start()

    py_breaker_process.join()
    c_breaker_process.join()
