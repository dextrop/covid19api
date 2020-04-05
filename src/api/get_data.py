from rest_framework import generics
from rest_framework import mixins
from rest_framework.status import HTTP_201_CREATED
from src.lib.customresponse import CustomResponse
from src.lib.getData import getData

class GetData(generics.GenericAPIView, mixins.UpdateModelMixin, mixins.DestroyModelMixin,
                mixins.ListModelMixin):

    def get(self, requests):
        data = requests.GET
        response = getData().get_data
        return CustomResponse(message="Covid-19 Count India", payload=response, code=HTTP_201_CREATED)