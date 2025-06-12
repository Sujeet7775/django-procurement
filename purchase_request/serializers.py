# serializers.py
from rest_framework import serializers
from .models import PurchaseRequest, PRDocument

class PRDocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = PRDocument
        fields = ['file']

class PurchaseRequestSerializer(serializers.ModelSerializer):
    documents = PRDocumentSerializer(many=True, write_only=True)

    class Meta:
        model = PurchaseRequest
        fields = ['pr_date', 'supplier_id', 'rfo_no', 'initiated_by', 'remark', 'documents']

    def create(self, validated_data):
        documents_data = validated_data.pop('documents', [])
        pr = PurchaseRequest.objects.create(**validated_data)
        for doc in documents_data:
            PRDocument.objects.create(purchase_request=pr, file=doc['file'])
        return pr
