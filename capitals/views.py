from core.models import Country_and_Capital
from .serializers import CountryAndCapitalSerializer
from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
import random
import requests


class CapitalApiViewSet(viewsets.ViewSet):

    parser_classes = [ JSONParser ]
    
    def get_object(self, uuid):
        try:
            return Country_and_Capital.objects.get(uuid=uuid)
        except:
            return None

    def check_capital(self, request):
        
        queryset = self.get_object(request.data["uuid"])
        
        if queryset != None:
            serializer = CountryAndCapitalSerializer(queryset, partial = True)
            
            if serializer.data["capital"].lower() == request.data["capital"].strip().lower():
                return Response({"success" : True, "payload": serializer.data["capital"], "error" : None}, status=status.HTTP_200_OK)
            else:
                return Response({"success" : False, "payload": serializer.data["capital"], "error" : None}, status=status.HTTP_200_OK)
                                
        return Response({"success" : False, "payload": None, "error" : "bad request"}, status=status.HTTP_400_BAD_REQUEST)


    def random_country(self, request):        
        
        url = 'https://countriesnow.space/api/v0.1/countries/capital'
        
        response = requests.get(url).json()['data']
        
        random_country = random.choice(response)
        
        del random_country["iso2"]
        del random_country["iso3"]
        
        random_country["country"] = random_country.pop("name")
          
        serializer = CountryAndCapitalSerializer(data = random_country)
        
        if serializer.is_valid():
            
            serializer.save()
            
            res_data = serializer.data
            
            del res_data["capital"]
            
            return Response({"success" : True, "payload": res_data, "error" : None}, status=status.HTTP_200_OK)

        return Response({"success" : False, "payload": None, "error" : "bad request"}, status=status.HTTP_400_BAD_REQUEST)
        
        