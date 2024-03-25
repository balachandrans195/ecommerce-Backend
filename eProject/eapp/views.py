from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Customer, Rating, Category, Product, Cart
from .serializers import CustomerSerializer, CartSerializer
from django.shortcuts import get_object_or_404

from .serializers import RatingSerializer, CategorySerializer, ProductSerializer

class CustomerAPIView(APIView):

    def get(self, request, customer_id=None, *args, **kwargs):
        if customer_id is not None:
            try:
                customer = Customer.objects.get(customerId=customer_id)
                serializer = CustomerSerializer(customer)
                return Response(serializer.data)
            except Customer.DoesNotExist:
                return Response({'error': 'Customer not found'}, status=status.HTTP_404_NOT_FOUND)
        else:
            customers = Customer.objects.all()
            serializer = CustomerSerializer(customers, many=True)
            return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Customer created successfully'}, status=status.HTTP_201_CREATED)
        return Response({'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, customer_id, *args, **kwargs):
        try:
            customer = Customer.objects.get(customerId=customer_id)
            customer.delete()
            return Response({'message': 'Customer deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
        except Customer.DoesNotExist:
            return Response({'error': 'Customer not found'}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, customer_id, *args, **kwargs):
        try:
            customer = Customer.objects.get(customerId=customer_id)
            serializer = CustomerSerializer(customer, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'message': 'Customer updated successfully'}, status=status.HTTP_200_OK)
            return Response({'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        except Customer.DoesNotExist:
            return Response({'error': 'Customer not found'}, status=status.HTTP_404_NOT_FOUND)




class RatingListAPIView(APIView):
    def get(self, request):
        ratings = Rating.objects.all()
        serializer = RatingSerializer(ratings, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = RatingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RatingDetailAPIView(APIView):
    def get_object(self, rating_id):
        try:
            return Rating.objects.get(ratingId=rating_id)
        except Rating.DoesNotExist:
            raise Http404

    def get(self, request, rating_id):
        rating = self.get_object(rating_id)
        serializer = RatingSerializer(rating)
        return Response(serializer.data)

    def put(self, request, rating_id):
        rating = self.get_object(rating_id)
        serializer = RatingSerializer(rating, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, rating_id):
        rating = self.get_object(rating_id)
        rating.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Similar adjustments for Category and Product views

class CategoryListAPIView(APIView):
    def get(self, request):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CategoryDetailAPIView(APIView):
    def get_object(self, category_id):
        try:
            return Category.objects.get(categoryId=category_id)
        except Category.DoesNotExist:
            raise Http404

    def get(self, request, category_id):
        category = self.get_object(category_id)
        serializer = CategorySerializer(category)
        return Response(serializer.data)

    def put(self, request, category_id):
        category = self.get_object(category_id)
        serializer = CategorySerializer(category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, category_id):
        category = self.get_object(category_id)
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ProductListAPIView(APIView):
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProductDetailAPIView(APIView):
    def get_object(self, product_id):
        try:
            return Product.objects.get(productId=product_id)
        except Product.DoesNotExist:
            raise Http404

    def get(self, request, product_id):
        product = self.get_object(product_id)
        serializer = ProductSerializer(product)
        return Response(serializer.data)

    def put(self, request, product_id):
        product = self.get_object(product_id)
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, product_id):
        product = self.get_object(product_id)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)




class CartListAPIView(APIView):
    def get(self, request, customer_id):
        customer = get_object_or_404(Customer, customerId=customer_id)
        carts = Cart.objects.filter(customerId=customer)
        serializer = CartSerializer(carts, many=True)
        return Response(serializer.data)

    def post(self, request, customer_id):
        customer = get_object_or_404(Customer, customerId=customer_id)
        serializer = CartSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(customerId=customer)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CartDetailAPIView(APIView):
    def get(self, request, cart_id):
        cart = get_object_or_404(Cart, cartId=cart_id)
        serializer = CartSerializer(cart)
        return Response(serializer.data)

    def put(self, request, cart_id):
        cart = get_object_or_404(Cart, cartId=cart_id)
        serializer = CartSerializer(cart, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, cart_id):
        cart = get_object_or_404(Cart, cartId=cart_id)
        cart.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
