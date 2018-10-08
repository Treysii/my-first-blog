from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Publicacion
from .forms import PostForm
from django.shortcuts import redirect


def lista(request):
    pub = Publicacion.objects.filter(fecha_publicacion__lte=timezone.now()).order_by('fecha_publicacion')
    return render(request, 'blog/listar.html', {'pub': pub})

def detalle(request, pk):
    det = get_object_or_404(Publicacion, pk=pk)
    return render(request, 'blog/detalle.html', {'det': det})

def nuevo(request):
        if request.method == "POST":
            form = PostForm(request.POST)
            if form.is_valid():
                p = form.save(commit=False)
                p.autor = request.user
                p.fecha_publicacion = timezone.now()
                p.save()
                return redirect('detalle', pk=p.pk)
        else:
            form = PostForm()
        return render(request, 'blog/editar.html', {'form': form})

def editar(request, pk):
        post = get_object_or_404(Publicacion, pk=pk)
        if request.method == "POST":
            form = PostForm(request.POST, instance=post)
            if form.is_valid():
                post = form.save(commit=False)
                post.autor = request.user
                post.save()
                return redirect('detalle', pk=post.pk)
        else:
            form = PostForm(instance=post)
        return render(request, 'blog/editar.html', {'form': form})
