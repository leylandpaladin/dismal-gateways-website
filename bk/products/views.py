from django.shortcuts import render, get_object_or_404

from .models import Album

# Create your views here.


def album_detail_view(request, aid):
    
    
    obj = get_object_or_404(Album, id=aid)
    
    context = {
            'object':obj
            }
    return render(request, "details.html", context)



def album_list_view(request):

    queryset = Album.objects.all()

    context = {
            'object_list': queryset
            }

    return render(request, 'products.html', context)


