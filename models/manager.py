
from typing import NoReturn
from models.detector import Detector
from models.camera import Camera
from PyQt5.QtCore import QObject, pyqtSignal
from PyQt5 import QtCore
from dotenv import load_dotenv, find_dotenv
import os

class Manager(QObject):
    sendResult = pyqtSignal(object)

    def __init__(self) -> NoReturn:
        super().__init__()

        load_dotenv(find_dotenv())
        input = os.getenv("INPUT")

        if input is not None:
            if input.isdigit():
                input = int(input)
        else:
            input = 0
        


        self.cam = Camera(input)
        self.inference = Detector()

        self.cam.sendFrame.connect(self.inference.receiveFrame, QtCore.Qt.DirectConnection)
        self.inference.sendInferences.connect(self.sendResult, QtCore.Qt.DirectConnection)
        


    def start(self) -> NoReturn:
        self.inference.start()
        self.cam.start()
        

    
