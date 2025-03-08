import cv2
import numpy as np


class DrawingFunctions:
    def __init__(self):
        #Rutas de imagenes
        self.img_forward = None  #cv2.imread('gesture_detector/resources/images/forward.png')

    def draw_image(self, original_frame: np.ndarray, action_image: np.ndarray):
        if action_image is not None:
            al, an, c = action_image.shape
            original_frame[600:600 + al, 50:50 + an] = action_image
        return original_frame

    def draw_actions(self, action: str, original_frame: np.ndarray) -> np.ndarray:

        actions_dict = {
            'P': self.img_forward,   
        }
        if action in actions_dict:
            movement_image = actions_dict[action]
            original_frame = self.draw_image(original_frame, movement_image)
        return original_frame