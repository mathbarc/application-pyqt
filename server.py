from models.manager import Manager
from models.api_manager import ApiManager
import PyQt5
import sys
from PyQt5.QtCore import QLibraryInfo
import os
import cv2
    
os.environ["QT_QPA_PLATFORM_PLUGIN_PATH"] = QLibraryInfo.location(
    QLibraryInfo.PluginsPath
)

if __name__=='__main__':
    app = PyQt5.QtCore.QCoreApplication(sys.argv)
    manager = Manager()
    api_manager = ApiManager()

    manager.sendResult.connect(api_manager.sendToBackend)
    manager.start()
    
    sys.exit(app.exec_())

