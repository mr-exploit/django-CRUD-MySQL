from django.urls import path
from . import views
#create your views
urlpatterns = [
    # path('', views.apiOverview, name = "apiOverview"),
    path('products', views.ShowAllProduct, name = "product-list"),
    path('products/<int:pk>/', views.ShowProductId, name = "product-detail"),
    path('products/create', views.CreateProduct, name = "product-create"),
    path('products/update/<int:pk>', views.UpdateProduct, name = "product-update"),
    path('products/delete/<int:pk>', views.DeleteProduct, name = "product-delete")
]


