from rest_framework import generics
from rest_framework import mixins
from rest_framework.status import HTTP_201_CREATED
from src.lib.customresponse import CustomResponse
from src.lib.scrap_from_wiki import ScrapFromWiki

class GetData(generics.GenericAPIView, mixins.UpdateModelMixin, mixins.DestroyModelMixin,
                mixins.ListModelMixin):

    def get(self, requests):
        data = requests.GET
        response = ScrapFromWiki().getDataIndia()
        return CustomResponse(message="Covid-19 Count India", payload=response, code=HTTP_201_CREATED)