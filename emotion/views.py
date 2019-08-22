
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import POST
from .Emotion.Analysis import Emo


def get_result(text):
    Class = Emo()
    Class.add_data(text)
    result = Class.get_emo()
    del Class
    return result


class EmoView(APIView):
    def post(self, request, *args, **kwargs):
        try:
            target = request.data.get('text').replace('\n','')
            length = len(target)
            value = get_result(target)
            return Response(data={'length':length,'target':target,'value':value})
        except:
            return Response(data={'length':0,'target':'ERROR','value':0})
