from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .serializers import ProductSerializer
from .models import Product

# create your views
# @api_view(['GET'])
# def apiOverview(request):
#     api_urls = {
#         'List': '/product-list/',
#         'Detail View': '/product-detail/<int:id>/',
#         'Create': '/product-create/',
#         'Update' : '/product-update/<int:id>',
#         'Delete' : '/product-delete/<int:id>'
#     }
#     return Response(api_urls)

@api_view(['GET'])
def ShowAllProduct(request):
    print("Request received")
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    print("Response data:", serializer.data)
    return Response(serializer.data)

@api_view(['GET'])
def ShowProductId(request, pk):
    try:
        product = Product.objects.get(id=pk)
    except Product.DoesNotExist:
        return Response({'error': 'data Product is not found'}, status=status.HTTP_404_NOT_FOUND)
    serializer = ProductSerializer(product, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def CreateProduct(request):
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['PUT'])
def UpdateProduct(request, pk):
    try:
        product = Product.objects.get(id=pk)
    except Product.DoesNotExist:
        return Response({'error': 'data Product is not found'}, status=status.HTTP_404_NOT_FOUND)
    
    serializer = ProductSerializer(instance=product, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def DeleteProduct(request, pk):
    try:
        product = Product.objects.get(id=pk)
    except Product.DoesNotExist:
        return Response({'error': 'data Product is not found'}, status=status.HTTP_404_NOT_FOUND)
    
    product.delete()
    
    return Response('Items delete Successfully')