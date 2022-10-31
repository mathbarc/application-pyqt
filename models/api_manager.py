
from typing import NoReturn
from PyQt5.QtCore import QObject, pyqtSignal
from dotenv import load_dotenv, find_dotenv
from requests import Session, Response
from requests.adapters import HTTPAdapter, Retry
import os

class ApiManager(QObject):
    sendLog = pyqtSignal(object)

    def __init__(self) -> NoReturn:
        super().__init__()

        load_dotenv(find_dotenv())
        self.url = os.getenv("API_URL")

        retries = Retry(
            total=int(os.getenv("REQUEST_MAX_RETRIES")),
            backoff_factor=int(os.getenv("REQUEST_RETRY_BACKOFF_FACTOR")),
            status_forcelist=[500, 502, 503, 504]
        )

        session = Session()
        self.session = session.mount("http://", HTTPAdapter(max_retries=retries))

    

    def sendToBackend(self, data) -> NoReturn:
        return self.session.post(url=self.url, json=data)
        

    
