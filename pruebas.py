import cv2 as cv
import mediapipe as mp
import serial

com = serial.Serial("COMX", 9600, write_timeout=10)
