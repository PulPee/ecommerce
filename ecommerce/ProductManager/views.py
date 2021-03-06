from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from .models import Category, FeaturedProduct, Product
from .serializers import CategorySerializer, ProductSerializer, ProductListItemSerializer

class CategoryList(APIView):
    def get(self, request):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return JsonResponse(serializer.data, safe=False)

class CategoryDetails(APIView):
    def get(self, request, pk):
        category = Category.objects.get(pk=pk)
        serializer = CategorySerializer(category)
        return JsonResponse(serializer.data, safe=False)

    def post(self, request, format=None):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)# add status 201
        return Response(serializer.errors)# add status

class FeaturedProducts(APIView):
    def get(self, request):
        featuredFk = FeaturedProduct.objects.all()
        featuredProducts = Product.objects.get(pk=featuredFk)
        serializer = ProductSerializer(featuredProducts, many=True)
        return JsonResponse(serializer.data, safe=False)

class ProductDetails(APIView):
    def get(self, request, pk):
        try:
            product = Product.objects.get(pk=pk)
        except ObjectDoesNotExist:
            return redirect('mainPage')

        return render(request, 'ProductManager/productDetails.html', {'product': product})

# class SearchProduct(APIView):
#     def post(self, request, query):
#         product_list = Product.objects.raw('''SELECT id
#             FROM ProductManager_product
#             WHERE name LIKE '%\%s%'
#             ''', [query])
#         print('PRODUCT LIST:\n' + str(product_list))

class ProductList(APIView):
    def post(self, request, format=None):
        query = '%' + request.POST["query"] + '%'
        product_list = Product.objects.raw("SELECT id, name, price FROM ProductManager_product WHERE name LIKE %s",
            [query],
        )

        return render(request, 'ProductManager/productList.html', {'products': product_list})
