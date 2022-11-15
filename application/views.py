from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from application.serializer import kbzRequestSerializer
from django.http import HttpResponse
# Create your views here.


class callback(APIView):
    def post(self, request):
        kbs = kbzRequestSerializer(data=request.data)
        if kbs.is_valid():
            kbs.save()
            # return Response("success", content_type="text/plain")
            return Response("success", content_type="text/plain")

        return Response(kbs.errors)


def index(request):
    return render(request, "index.html")



def home(request):
    return HttpResponse("success")