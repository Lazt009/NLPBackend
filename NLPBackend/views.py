from django.http import HttpResponse

from NLPBackend import textProcessor

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(['POST'])
def home(request):
    # ans = textProcessor.process_text("Input here")
    # print(ans)
    if request.method == 'POST':
        print(request.data)
        ans = "None"
        if "data" in request.data.keys():
            ans = textProcessor.process_text(request.data["data"])
        return HttpResponse(ans)
