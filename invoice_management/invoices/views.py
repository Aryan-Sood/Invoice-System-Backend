from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import InvoiceSerializer
from .models import Invoice
from rest_framework.generics import RetrieveAPIView

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

class InvoiceListView(APIView):
    def get(self, request):
        print("List called")
        invoices = Invoice.objects.all()
        serializer = InvoiceSerializer(invoices, many = True)
        return Response(serializer.data)

class InvoiceDetailView(RetrieveAPIView):
    def post(self, request):
        print("called")
        invoice_id = request.data.get("id")
        if not invoice_id:
            return Response({"error": "ID is required"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            invoice = Invoice.objects.get(id=invoice_id)
            serializer = InvoiceSerializer(invoice)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Invoice.DoesNotExist:
            return Response({"error": "Invoice not found"}, status=status.HTTP_404_NOT_FOUND)