from django.urls import path
from .views import PurchaseRequestCreateView

urlpatterns = [
    path('purchase-request/', PurchaseRequestCreateView.as_view(), name='purchase-request-create'),
]
