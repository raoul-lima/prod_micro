from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import ProductSerializer
from .models import Product
from django.shortcuts import get_object_or_404

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
import json


class ProductViews(APIView):
    def post(self, request):

        data = json.loads(request.body.decode("utf-8"))
        p_name = data.get('product_name')
        p_price = data.get('product_price')

        product_data = {
            'product_name': p_name,
            'product_price': p_price,
        }

        product = Product.objects.create(**product_data)

        data = {
            "message": f"New item added to Product with id: {product.id}"
        }
        return JsonResponse(data, status=201)

    def get(self, request, id=None):
        if id:
            item = Product.objects.get(id=id)
            serializer = ProductSerializer(item)
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

        items = Product.objects.all()
        serializer = ProductSerializer(items, many=True)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

    def patch(self, request, id=None):
        item = Product.objects.get(id=id)
        serializer = ProductSerializer(item, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data})
        else:
            return Response({"status": "error", "data": serializer.errors})

    def delete(self, request, id=None):
        item = get_object_or_404(Product, id=id)
        item.delete()
        return Response({"status": "success", "data": "Produit Supprimé avec succes"})