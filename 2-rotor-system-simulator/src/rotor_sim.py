from time import time
from typing import Callable


class RotorSim:

    def __init__(
        self,
        after_turn_consumer: Callable,
    ) -> None:
        self.after_turn_consumer = after_turn_consumer

    def f3(self, rotors: list, rotor_size: int, rotors_max_num: int):
        """Combine the add and append_rotor while loops into one
        # 1
        """

        start_time = time()

        while len(rotors) <= rotors_max_num:

            self.after_turn_consumer(rotors)

            # Turn base rotor
            rotors[0] += 1
            rotors[0] %= rotor_size

            # Turn non-base rotors
            i = 0
            add_rotor_flag = False
            while i < len(rotors):
                if rotors[i] != 0:
                    add_rotor_flag = False
                    break

                if (len(rotors) > 1) and (i < len(rotors) - 1):
                    rotors[i + 1] += 1
                    rotors[i + 1] %= rotor_size

                if i == len(rotors) - 1:
                    if rotors[i] == 0:
                        add_rotor_flag = True

                i += 1

            # Add rotor
            if add_rotor_flag:
                rotors.append(0)

        print(f"PYTHON ROTOR SIMULATOR")
        print(f"rotors: {rotors}")
        print(f"time to completion: {time()-start_time}")
