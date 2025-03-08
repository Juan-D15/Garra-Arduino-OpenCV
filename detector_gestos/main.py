import numpy as np
from typing import List, Tuple

from detector_gestos.extractor_gestos import HandProcessing
from detector_gestos.drawing_functions import DrawingFunctions


class GestureDetector:
    def __init__(self):
        self.hand_detector = HandProcessing(threshold_detection=0.9)
        self.draw = DrawingFunctions()

    def fingers_interpretation(self, fingers_up: List[int]) -> str:
        commands = {
            (0, 0, 0, 0, 0): 'G1',  #Garra (Agarrar)
            (1, 1, 1, 1, 1): 'G2',  #Garra (Soltar)
            (0, 0, 0, 0, 1): 'I',   #Izquierda
            (1, 0, 0, 0, 0): 'D',   #Derecha
            (1, 0, 0, 0, 1): 'P',   #Parar
            (0, 1, 0, 0, 0): 'R1U', #Rotor 1 (Arriba) 
            (0, 1, 1, 0, 0): 'R1D', #Rotor 1 (Abajo)
            (1, 1, 0, 0, 0): 'R2U', #Rotor 2 (Arriba)
            (1, 1, 1, 0, 0): 'R2D', #Rotor 2 (Abajo)

        }
        return commands.get(tuple(fingers_up), "")

    def gesture_interpretation(self, img: np.ndarray) -> Tuple[str, np.ndarray]:
        frame = img.copy()
        frame = self.hand_detector.find_hands(frame, draw=True)
        hand_list, bbox = self.hand_detector.find_position(frame, draw_box=False)
        if len(hand_list) == 21:
            fingers_up = self.hand_detector.fingers_up(hand_list)
            print(fingers_up)
            command = self.fingers_interpretation(fingers_up)
            frame = self.draw.draw_actions(command, frame)
            return command, frame
        else:
            return "P", frame #retornar parar si hay un error


