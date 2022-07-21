from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Album
from .serializers import AlbumSerializer, UserSerializer 
from rest_framework import viewsets
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth.models import User

# Create your views here.

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    
    def validate(self, attrs):
         data = super().validate(attrs)
         data['username'] = self.user.username
         data['email'] = self.user.email

         return data

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


#Dead function below, keeping for example
###########################################
def album_detail_view(request, aid):
    
    
    obj = get_object_or_404(Album, id=aid)
    
    context = {
            'object':obj
            }
    return render(request, "details.html", context)


##################################################

class ProductDetailView(DetailView):

    model = Album
    template_name = 'details.html'


class ProductsView(ListView):
    model = Album
    template_name = 'products.html'


class AlbumViewAPI(viewsets.ModelViewSet):

    serializer_class = AlbumSerializer
    queryset = Album.objects.all()
    lookup_field = 'slug'

class UserViewAPI(viewsets.ModelViewSet):

    serializer_class = UserSerializer
    queryset = User.objects.all()

