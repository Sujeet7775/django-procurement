import uuid
from django.db import models
from common_models.models import AuditMixin
from supplier.models import Supplier  # ✅ Direct import
# from core.models import BaseModel

class PurchaseRequest(AuditMixin):
    pr_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    pr_req_no = models.CharField(max_length=100, unique=True,read_only=True)
    rfo_no = models.CharField(max_length=100, null=True, blank=True)
    pr_date = models.DateTimeField()
    
    # Storing only the UUID of the supplier instead of using a ForeignKey
    supplier_id = models.UUIDField()  # ✅ Just store UUID

    pr_documents = models.FilePathField(null=True, blank=True)
    initiated_by = models.CharField(max_length=100)
    remark = models.TextField(null=True, blank=True)
    
    
    def save(self, *args, **kwargs):
        if not self.pr_req_no:
            last_pr = PurchaseRequest.objects.order_by('-id').first()
            next_number = 1
            if last_pr and last_pr.pr_req_no:
                try:
                    last_number = int(last_pr.pr_req_no.split('-')[-1].strip())
                    next_number = last_number + 1
                except:
                    pass  # If parsing fails, keep next_number as 1

            self.pr_req_no = f"PR - {next_number}"

        super().save(*args, **kwargs)

    def __str__(self):
        return str(self.pr_id)
    
    class Meta:
        verbose_name = "Purchase Request"
        verbose_name_plural = "Purchase Requests"
        ordering = ['-created_at']  # Order by creation date, descending
        unique_together = (('pr_no', 'supplier_id'),)
