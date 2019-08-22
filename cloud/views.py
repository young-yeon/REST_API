
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import POST
from .WordCloud.MakeCloud import Cloud


def make_cloud(title, text, cnt):
    Class = Cloud(cnt=cnt)
    try:
        Class.add_data(text)
        Class.make_cloud(title=title)
    except:
        Class.add_all_data(text)
        Class.make_cloud(title=title)
    del Class



class CloudView(APIView):
    def post(self, request, *args, **kwargs):
        try:
            target = request.data.get('text').replace('\n','')
            length = len(target)
            title = request.data.get('title')
            cnt = 50
        except:
            return Response(data={'length':0,'target':'ERROR','url':'NO~'})
        make_cloud(title, target, cnt)
        url = 'http://cachi.ga/images/' + title + '.png'
        return Response(data={'length':length,'target':target, 'url':url})

