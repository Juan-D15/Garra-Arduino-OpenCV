#include <Servo.h>
// Declaración de servos
Servo servoBase;      // Movimiento izquierda/derecha
Servo servoBrazo1;    // Movimiento principal del brazo
Servo servoBrazo2;    // Ajuste del brazo
Servo servoGarra;     // Apertura/cierre de la garra

// Posiciones iniciales de los servos
int posBase = 90;     // Centro
int posBrazo1 = 90;   // Brazo en posición media
int posBrazo2 = 90;   // Ajuste en posición media
int posGarra = 90;    // Garra cerrada

void setup() {
    Serial.begin(9600);  // Iniciar comunicación serial
    Serial.setTimeout(10);
    servoBase.attach(3);
    servoBrazo1.attach(5);
    servoBrazo2.attach(6);
    servoGarra.attach(9);

    // Inicializar servos en posición central
    servoBase.write(posBase);
    servoBrazo1.write(posBrazo1);
    servoBrazo2.write(posBrazo2);
    servoGarra.write(posGarra);
}

void loop() {
    if (Serial.available()) {
        String command = Serial.readStringUntil('\n'); // Leer comando recibido

        // Convertir a char el primer carácter
        char action = command.charAt(0);

        switch (action) {
            case 'P':  // Parar el sistema
                Serial.println("PARAR");
                return;

            case 'I':  // Mover base a la izquierda
                posBase = constrain(posBase - 10, 0, 180);
                servoBase.write(posBase);
                break;

            case 'D':  // Mover base a la derecha
                posBase = constrain(posBase + 10, 0, 180);
                servoBase.write(posBase);
                break;

            case 'G':  // Control de la garra
                if (command == "G1") {
                    posGarra = 180;  // Cerrar garra
                } else if (command == "G2") {
                    posGarra = 90;   // Abrir garra
                }
                servoGarra.write(posGarra);
                break;

            case 'R':  // Movimiento del brazo (R1 y R2)
                if (command == "R1U") {
                    posBrazo1 = constrain(posBrazo1 - 10, 0, 180);
                    servoBrazo1.write(posBrazo1);
                } 
                else if (command == "R1D") {
                    posBrazo1 = constrain(posBrazo1 + 10, 0, 180);
                    servoBrazo1.write(posBrazo1);
                } 
                else if (command == "R2U") {
                    posBrazo2 = constrain(posBrazo2 - 10, 0, 180);
                    servoBrazo2.write(posBrazo2);
                } 
                else if (command == "R2D") {
                    posBrazo2 = constrain(posBrazo2 + 10, 0, 180);
                    servoBrazo2.write(posBrazo2);
                }
                break;

            default:
                Serial.println("Comando no reconocido");
                break;
        }

        // Confirmar movimiento en el monitor serie
        Serial.print("Command: ");
        Serial.println(command);
    }
}
