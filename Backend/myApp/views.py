
from rest_framework import viewsets,generics, permissions,status,serializers
from rest_framework.parsers import MultiPartParser
from rest_framework.decorators import action
from rest_framework.response import Response
from django.http import Http404
from django.shortcuts import render
from .models import *
from .serializer import UserSerializer,CategorySerializer,ArticleSerializer,SubscriberSerializer, DetailSubscriberSerializer
from .paginator import BasePagination



class UserViewSet(viewsets.ViewSet,
                  generics.ListAPIView,
                  generics.RetrieveAPIView,
                  generics.UpdateAPIView):
    queryset = User.objects.filter(is_active = True)
    serializer_class = UserSerializer
    parser_classes = [MultiPartParser, ]

    # def get_permissions(self):
    #     if self.action == 'list':
    #         return [permissions.IsAuthenticated()]

    #     return [permissions.AllowAny()]
    
    


class CategoryViewSet(viewsets.ViewSet,
                      generics.ListAPIView,
                      generics.UpdateAPIView,
                      generics.RetrieveAPIView):
    queryset = Category.objects.filter(active = True)
    serializer_class = CategorySerializer

    # def get_permissions(self):
    #     if self.action == 'list':
    #         return [permissions.AllowAny()]
    #     return [permissions.IsAuthenticated()]
    @action(methods=['get'],detail=True,url_path="articles")
    def get_articles(self,request,pk):
        articles = Category.objects.get(pk=pk).articles.filter(active = True)
        #articles = self.get_object().articles.filter(active = True)
        
        q = request.query_params.get('q')

        if q is not None:
            articles = articles.filter(title__icontains=q)

        return Response(ArticleSerializer(articles,many=True).data, status = status.HTTP_200_OK)


class ArticleViewSet(viewsets.ViewSet, generics.ListAPIView, generics.CreateAPIView,generics.RetrieveAPIView):   
    
    serializer_class = ArticleSerializer
    pagination_class = BasePagination    

    def get_queryset(self):
        Articles = Article.objects.filter(active=True)

        q = self.request.query_params.get('q')

        if q is not None:
            Articles = Articles.filter(title__icontains=q)        
        return Articles

    @action(methods=['post'],detail=True)
    #/article/{pk}/active_article
    def active_article(self,request,pk):
        try:    
            a = Article.objects.get(pk = pk)
            a.active = True
            a.save()
        except Article.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        return Response(ArticleSerializer(a).data,status = status.HTTP_200_OK)

    @action(methods=['post'],detail=True)
    #/article/{pk}/hide_article
    def hide_article(self,request,pk):
        try:
            a = Article.objects.get(pk = pk)
            a.active = False
            a.save()
        except Article.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        return Response(ArticleSerializer(a).data,status = status.HTTP_200_OK)

class SubscriberViewSet(viewsets.ViewSet,
                        generics.ListAPIView,
                        generics.CreateAPIView,
                        generics.RetrieveAPIView):
    
    queryset = Subscriber.objects.filter(active = True)
    pagination_class = BasePagination
    serializer_class = DetailSubscriberSerializer
    def get_serializer_class(self):
        if self.action == 'list':
            serializer_class = SubscriberSerializer
        else:
            serializer_class = DetailSubscriberSerializer
        return serializer_class
    @action(methods=['post'],detail=True)
    def add_category(self,request,pk):
        try:
            subscriber = self.get_object()
        except Http404:
            return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            categories = request.data.get("categories")
            if categories is not None:
                for cat in categories:
                    if Category.objects.filter(name=cat).exists():
                        subscriber.categories.add(Category.objects.get(name=cat))
                    else:
                        return Response("Category is not existed")

                subscriber.save()

                return Response(self.serializer_class(subscriber).data,
                                status = status.HTTP_201_CREATED)
            else:
                return Response("Categories field is required")

    @action(methods=['post'],detail=True)
    def delete_category(self,request,pk):
        try:
            subscriber = self.get_object()
        except Http404:
            return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            categories = request.data.get("categories")
            if categories is not None:
                for cat in categories:
                    if Category.objects.filter(name=cat).exists():
                        subscriber.categories.remove(Category.objects.get(name=cat))
                    else:
                        return Response("Category is not existed")

                subscriber.save()

                return Response(self.serializer_class(subscriber).data,
                                status = status.HTTP_201_CREATED)
            else:
                return Response("Categories field is required")

    @action(methods=['post'],detail=True,url_path = 'delete')
    def delete_subscriber(self,request,pk):
        try:
            a = Subscriber.objects.get(pk = pk)
            a.active = False
            a.save()
        except Subscriber.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        return Response(SubscriberSerializer(a).data,status = status.HTTP_200_OK)
            







    
