import cv2
import numpy as np

class DrawingFunctions:
    def __init__(self):
        # Cargar imágenes con verificación y conversión
        self.agarrar = self.load_image('detector_gestos/resources/images/Agarrar.png')
        self.soltar = self.load_image('detector_gestos/resources/images/Soltar.png')
        self.izquierda = self.load_image('detector_gestos/resources/images/Izquierda.png')
        self.derecha = self.load_image('detector_gestos/resources/images/Derecha.png')
        self.parar = self.load_image('detector_gestos/resources/images/Parar.png')
        self.R1Arriba = self.load_image('detector_gestos/resources/images/Arriba.png')
        self.R1Abajo = self.load_image('detector_gestos/resources/images/Abajo.png')
        self.R2Arriba = self.load_image('detector_gestos/resources/images/Arriba.png')
        self.R2Abajo = self.load_image('detector_gestos/resources/images/Abajo.png')

    def load_image(self, path):
        """ Cargar imagen y convertir a formato compatible """
        image = cv2.imread(path, cv2.IMREAD_UNCHANGED)

        if image is None:
            print(f"Advertencia: No se pudo cargar {path}")
            return None

        # Convertir imagen a BGR si es en escala de grises
        if len(image.shape) == 2:
            image = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)

        # Convertir imagen BGRA (con transparencia) a BGR
        elif image.shape[2] == 4:
            image = cv2.cvtColor(image, cv2.COLOR_BGRA2BGR)

        # Redimensionar imagen a tamaño estándar (ejemplo: 100x50 px)
        image = cv2.resize(image, (100, 50))

        return image

    def draw_image(self, original_frame: np.ndarray, action_image: np.ndarray):
        if action_image is None:
            print("Advertencia: La imagen de acción no se cargó correctamente.")
            return original_frame

        al, an = action_image.shape[:2]  # Alto y ancho

        # Asegurar que la imagen no sobrepase los límites
        y1 = max(original_frame.shape[0] - al - 10, 0)  # 10 px de margen inferior
        y2 = min(original_frame.shape[0], y1 + al)
        x1 = 10  # Margen izquierdo
        x2 = min(original_frame.shape[1], x1 + an)

        # Insertar la imagen en la región correcta
        original_frame[y1:y2, x1:x2] = action_image

        return original_frame

    def draw_actions(self, action: str, original_frame: np.ndarray) -> np.ndarray:
        actions_dict = {
            'G1': self.agarrar,
            'G2': self.soltar,
            'I': self.izquierda,
            'D': self.derecha,   
            'P': self.parar,   
            'R1U': self.R1Arriba,   
            'R1D': self.R1Abajo,   
            'R2U': self.R2Arriba,   
            'R2D': self.R2Abajo,   
        }

        if action in actions_dict:
            movement_image = actions_dict[action]
            if movement_image is not None:
                original_frame = self.draw_image(original_frame, movement_image)
            else:
                print(f"Advertencia: No hay imagen para la acción '{action}'")
        return original_frame