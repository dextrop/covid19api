import json
from datetime import datetime
from src.models.scrap_data import Scrapping
from src.lib.scrap_from_wiki import ScrapFromWiki

class getData():
    def __init__(self):
        print "get Data"

    def check_last_scrap(self):
        data_set = Scrapping.objects.filter()
        if data_set.count() < 1:
            data_set = ScrapFromWiki().getDataIndia()
            data = {
                "data" : json.dumps(data_set)
            }
            Scrapping.objects.create(**data)
            return False, data_set
        else:
            print datetime.now() - data_set[0].updated
            return False, {}

    @property
    def get_data(self):
        try:
            status, data = self.check_last_scrap()
        except Exception as e:
            print e
        return {}
