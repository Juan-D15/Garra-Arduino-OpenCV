import cv2
from detector_gestos.main import GestureDetector
from interfaz_control.comunicacion_serial import ComunicacionSerial


class CarGestureControl:
    def __init__(self):
        self.cap = cv2.VideoCapture(0)
        self.cap.set(3, 640) #resolucion pantalla
        self.cap.set(4, 480)
        self.hand_gesture = GestureDetector()
        self.communication = ComunicacionSerial()

    def frame_processing(self):
        while True:
            t = cv2.waitKey(5)
            ret, frame = self.cap.read()
            command, draw_frame = self.hand_gesture.gesture_interpretation(frame)
            self.communication.sending_data(command + "\n" )

            cv2.imshow('Brazo control', draw_frame)
            if t == 27:
                break

        self.cap.release()
        cv2.destroyAllWindows()

detector = CarGestureControl()
detector.frame_processing()
