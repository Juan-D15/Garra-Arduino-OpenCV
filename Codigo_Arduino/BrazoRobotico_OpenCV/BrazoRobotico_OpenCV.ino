#include <Servo.h>

// Declaración de servos
Servo servoBase;      // Movimiento izquierda/derecha
Servo servoBrazo1;    // Movimiento principal del brazo
Servo servoBrazo2;    // Ajuste del brazo
Servo servoGarra;     // Apertura/cierre de la garra

// Posiciones iniciales de los servos
int posBase = 90;
int posBrazo1 = 80;
int posBrazo2 = 10;
int posGarra = 90;

// Función para mover los servos suavemente
void moverSuavemente(Servo &servo, int &posActual, int nuevaPos, int paso = 2, int delayTime = 10) {
    if (posActual < nuevaPos) {
        for (int i = posActual; i <= nuevaPos; i += paso) {
            servo.write(i);
            delay(delayTime);
        }
    } else {
        for (int i = posActual; i >= nuevaPos; i -= paso) {
            servo.write(i);
            delay(delayTime);
        }
    }
    posActual = nuevaPos; // Actualizar la posición real
}

void setup() {
    Serial.begin(9600);
    Serial.setTimeout(10);

    servoBase.attach(3);
    servoBrazo1.attach(5);
    servoBrazo2.attach(6);
    servoGarra.attach(9);

    servoBase.write(posBase);
    servoBrazo1.write(posBrazo1);
    servoBrazo2.write(posBrazo2);
    servoGarra.write(posGarra);
}

void loop() {
    if (Serial.available()) {
        String command = Serial.readStringUntil('\n');
        char action = command.charAt(0);

        switch (action) {
            case 'P':
                Serial.println("PARAR");
                return;

            case 'I':  
                moverSuavemente(servoBase, posBase, constrain(posBase - 10, 0, 180));
                break;

            case 'D':  
                moverSuavemente(servoBase, posBase, constrain(posBase + 10, 0, 180));
                break;

            case 'G':  
                if (command == "G1") {
                    moverSuavemente(servoGarra, posGarra, 180);
                } else if (command == "G2") {
                    moverSuavemente(servoGarra, posGarra, 90);
                }
                break;

            case 'R':  
                if (command == "R1U") {
                    moverSuavemente(servoBrazo1, posBrazo1, constrain(posBrazo1 - 10, 50, 180));
                } 
                else if (command == "R1D") {
                    moverSuavemente(servoBrazo1, posBrazo1, constrain(posBrazo1 + 10, 50, 180));
                } 
                else if (command == "R2U") {
                    moverSuavemente(servoBrazo2, posBrazo2, constrain(posBrazo2 - 10, 0, 180));
                } 
                else if (command == "R2D") {
                    moverSuavemente(servoBrazo2, posBrazo2, constrain(posBrazo2 + 10, 0, 180));
                }
                break;

            default:
                Serial.println("Comando no reconocido");
                break;
        }

        Serial.print("Command: ");
        Serial.println(command);
    }
}
