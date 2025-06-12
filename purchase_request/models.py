import uuid
from django.db import models
from core.models import AuditMixin

# Create your models here.
class PurchaseRequest(AuditMixin):
    pr_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    pr_no = models.CharField(max_length=100, unique=True)
    rfo_no = models.CharField(max_length=100, null=True, blank=True)
    pr_date = models.DateTimeField()
    supplier = models.ForeignKey('supplier.Supplier', on_delete=models.CASCADE)
    pr_documents = models.BinaryField(null=True, blank=True)
    initiated_by = models.CharField(max_length=100)
    remark = models.TextField(null=True, blank=True)

    def __str__(self):
        return str(self.pr_id)