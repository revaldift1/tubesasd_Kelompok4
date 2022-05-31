import cv2
import mediapipe as mp
import time


class handDetector():
    def __init__(self, mode=False,maxHands=2, detectionCon=0.5,modelComplexity=1, trackCon=0.5):
        self.mode = mode
        self.maxHands = maxHands
        self.detectionCon = detectionCon
        self.modelComplex = modelComplexity
        self.trackCon = trackCon

        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(self.mode,self.maxHands,self.modelComplex,self.detectionCon, self.trackCon)
        self.mpDraw = mp.solutions.drawing_utils
