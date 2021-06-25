from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from rest_framework.views import APIView
# Create your views here.
def index(request):
    return HttpResponse("Hello")

class uploadPhoto(APIView):
    def get(self, request):
        pass

    def post(self, request):
        file = request.FILES['image']
        file_name = file.name
        destination = 'media/'
        output = f'{destination}{file_name}'
        print(file_name)
        fn = open(output, 'wb+')
        for chunk in file.chunks():
            fn.write(chunk)
        fn.close()
        return HttpResponse("%s is upload to the server succesfuly" % file_name)
