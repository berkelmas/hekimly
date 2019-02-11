from django.shortcuts import render, redirect
from .models import Contact, Makaleler

from django.core.paginator import Paginator

# Create your views here.
def index(request):
    return render(request, 'hekimlysite/index.html', {'nbar' : 'index'})


def about(request):
    return render(request, 'hekimlysite/hakkimizda.html', {'nbar' : 'about'})


def services(request):
    return render(request, 'hekimlysite/hizmetlerimiz.html', {'nbar' : 'services'})

def process(request):
    return render(request, 'hekimlysite/surec.html', {'nbar' : 'process'})

def faq(request):
    return render(request, 'hekimlysite/faq.html', {'nbar' : 'faq'})

def contact(request):
    if request.method == "POST":
        adsoyad = request.POST.get('adsoyad')
        email = request.POST.get('email')
        mesaj = request.POST.get('mesaj')

        iletisim = Contact(iletisim_adsoyad=adsoyad, iletisim_ulasim=email, iletisim_mesaj=mesaj)
        iletisim.save()

        return redirect('/?gonder=ok')

    return render(request, 'hekimlysite/iletisim.html', {'nbar' : 'contact'})



def articles(request):
    makale_list = Makaleler.objects.all()   ## sonra bi sn kapı caldı geliyom
    paginator = Paginator(makale_list, 6)  # Her Sayfada 1 Makale Gösterilecek.

    page = request.GET.get('page')
    articles = paginator.get_page(page)

    return render(request, 'hekimlysite/makaleler.html', {'articles' : articles, 'nbar' : 'articles'})




def articledetay(request, makaleslug):

    makale = Makaleler.objects.get(makale_slug=makaleslug)

    return render(request, 'hekimlysite/makaledetay.html', {'makale' : makale, 'nbar' : 'articledetail'})


def not_found(request):
    return render(request, 'hekimlysite/404.html')
