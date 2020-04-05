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
        print "Success 1"
        if data_obj.count() < 1:
            data_set = ScrapFromWiki().getDataIndia()
            data = {
                "data" : json.dumps(data_set)
            }
            Scrapping.objects.create(**data)
            print "Success 2"
            return False, data_set
        else:
            print "Success 2.1"
            if ((timezone.now() - data_obj[0].updated).total_seconds() < 1800):
                print "Success 2.2.0"
                return False, json.loads(data_obj[0].data)
            else:
                print "Success 2.2.1"
                data_set = ScrapFromWiki().getDataIndia()
                current = data_obj[0]
                print "Data object to be updated", current
                setattr(current, "data", json.dumps(data_set))
                current.save()
    @property
    def get_data(self):
        data = {}
        try:
            status, data = self.check_last_scrap()
        except Exception as e:
            print "Error Scraping Data", e
        return data
