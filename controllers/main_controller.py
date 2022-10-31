from models.manager import Manager
from views.view import MainWindow
from models.resultshandler import ResultsHandler
from PyQt5.QtCore import QObject


class MainController(QObject):

    def __init__(self) -> None:
        super().__init__()
        self.manager = Manager()
        
        self.window = MainWindow()
        self.manager.sendResult.connect(self.window.show_frame)

    def run(self) -> None:
        self.window.showMaximized()
        
        self.manager.start()


