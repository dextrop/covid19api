import json
from datetime import datetime
from src.models.scrap_data import Scrapping
from src.lib.scrap_from_wiki import ScrapFromWiki
from django.utils import timezone

class getData():
    def __init__(self):
        print "get Data"

    def check_last_scrap(self):
        data_obj = Scrapping.objects.filter()
        if data_obj.count() < 1:
            data_set = ScrapFromWiki().getDataIndia()
            data = {
                "data" : json.dumps(data_set)
            }
            Scrapping.objects.create(**data)
            return False, data_set
        else:
            if ((timezone.now() - data_obj[0].updated).total_seconds() < 1800):
                return False, json.loads(data_obj[0].data)
            else:
                data_set = ScrapFromWiki().getDataIndia()
                current = data_obj[0]
                setattr(current, "data", data_set)
                current.save()
    @property
    def get_data(self):
        data = {}
        try:
            status, data = self.check_last_scrap()
        except Exception as e:
            print e
        return data
