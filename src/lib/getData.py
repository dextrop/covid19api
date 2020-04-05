from datetime import datetime
from src.models.scrap_data import Scrapping

class getData():
    def __init__(self):
        print "get Data"

    def check_last_scrap(self):
        data_set = Scrapping.objects.filter()
        if data_set.count() < 1:
            return True
        else:
            print datetime.now() - data_set.updated
            return False

    @property
    def get_data(self):
        self.check_last_scrap()
        return {}
