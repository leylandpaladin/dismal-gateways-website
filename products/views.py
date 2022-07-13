from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Album
from .serializers import AlbumSerializer
from rest_framework import viewsets


# Create your views here.



def album_detail_view(request, aid):
    
    
    obj = get_object_or_404(Album, id=aid)
    
    context = {
            'object':obj
            }
    return render(request, "details.html", context)

class ProductDetailView(DetailView):

    model = Album
    template_name = 'details.html'


class ProductsView(ListView):
    model = Album
    template_name = 'products.html'


class AlbumViewAPI(viewsets.ModelViewSet):

    serializer_class = AlbumSerializer
    queryset = Album.objects.all()

     

