from rest_framework.views import APIView
from rest_framework.response import Response
from supplier.models import Supplier

class SupplierTestView(APIView):
    def get(self, request):
        suppliers = Supplier.objects.all()
        return Response({"suppliers": list(suppliers.values())})
