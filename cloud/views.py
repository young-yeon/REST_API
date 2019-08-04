
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import POST
from .WordCloud.MakeCloud import Cloud


def make_cloud(title, text, cnt):
    Class = Cloud(cnt=cnt)
    Class.add_data(text)
    Class.make_cloud(title=title)


class CloudView(APIView):
    def post(self, request, *args, **kwargs):
        target = request.data.get('text')
        length = len(target)
        title = request.data.get('title')
        cnt = request.data.get('count')
        make_cloud(title, target, cnt)
        return Response(data={'length':length,'target':target})