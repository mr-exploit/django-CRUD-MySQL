from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination
# from rest_framework.authentication import SessionAuthentication, BasicAuthentication
# from rest_framework.permissions import IsAuthenticated
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
# authentication_classes = [SessionAuthentication, BasicAuthentication]
# permission_classes = [IsAuthenticated]
    
@api_view(['GET'])
def ShowAllProduct(request):
    products = Product.objects.all()
    if not products:
        return Response({'messagetype' : 'E', 'message' : 'data Product is not found'}, status=status.HTTP_404_NOT_FOUND)
    
    paginator = LimitOffsetPagination()
    paginator.page_size = 2
    result_page = paginator.paginate_queryset(products, request)
    serializer = ProductSerializer(result_page, many=True)
    print("Response data:", serializer.data)
    return paginator.get_paginated_response(serializer.data)

@api_view(['GET'])
# @authentication_classes([SessionAuthentication, BasicAuthentication])
# @permission_classes([IsAuthenticated])
def ShowProductId(request, pk):
    try:
        product = Product.objects.get(id=pk)
    except Product.DoesNotExist:
        return Response({'messagetype' : 'E', 'message': 'data Product is not found'}, status=status.HTTP_404_NOT_FOUND)
    
    serializer = ProductSerializer(product, many=False)
    return Response({'messagetype' : 'S', 'message' : 'success', 'data' : serializer.data, }, status=status.HTTP_200_OK)

@api_view(['POST'])
def CreateProduct(request):
    serializer = ProductSerializer(data=request.data)
    print("data Serializer", serializer)
    if serializer.is_valid():
        serializer.save()
        return Response({'messagetype' : 'S', 'message' : 'create Product Successfully', 'data' :serializer.data}, status=status.HTTP_201_CREATED)
    return Response({'messagetype' : 'E', 'message':serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def UpdateProduct(request, pk):
    try:
        product = Product.objects.get(id=pk)
    except Product.DoesNotExist:
        return Response({'messagetype' : 'E', 'message': 'data Product is not found'}, status=status.HTTP_404_NOT_FOUND)
    
    serializer = ProductSerializer(instance=product, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'messagetype' : 'S', 'message' : 'Update Success', 'data' : serializer.data}, status=status.HTTP_200_OK)
    return Response({'messagetype' : 'E', 'message': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def DeleteProduct(request, pk):
    try:
        product = Product.objects.get(id=pk)
    except Product.DoesNotExist:
        return Response({'messagetype': 'E', 'message' : 'data Product is not found', }, status=status.HTTP_404_NOT_FOUND)

    product.delete()
    
    return Response({'messagetype' : 'S', 'message' : 'Delete Success',  'data' : 'Product Deleted'}, status=status.HTTP_200_OK)