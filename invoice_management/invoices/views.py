from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import InvoiceSerializer

# def index(request):
#     return HttpResponse('Home Page')

class InvoiceCreateView(APIView):
    def post(self, request):
        print('request received:', request)
        serializer = InvoiceSerializer(data = request.data)
        print('serializer:', serializer)
        if serializer.is_valid():
            print('saving serializer')
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        print('serializer failed')
        print(serializer)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)