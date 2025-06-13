# views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from .serializers import PurchaseRequestSerializer

class PurchaseRequestCreateView(APIView):
    permission_classes = [permissions.AllowAny]  # change as needed

    def post(self, request):
        serializer = PurchaseRequestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Purchase Request created successfully'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
