from django.urls import path
from .views import SupplierTestView

urlpatterns = [
    path('test-suppliers/', SupplierTestView.as_view()),
]
