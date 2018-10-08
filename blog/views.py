from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Publicacion

def lista(request):
    pub = Publicacion.objects.filter(fecha_publicacion__lte=timezone.now()).order_by('fecha_publicacion')
    return render(request, 'blog/listar.html', {'pub': pub})

def detalle(request, pk):
    det = get_object_or_404(Publicacion, pk=pk)
    return render(request, 'blog/detalle.html', {'det': det})
