from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect

from portfolio.models import Hobby, PortfolioItem
from .forms import ContactForm, PortfolioForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

# Create your views here.

def home(request):
    return render(request, 'home.html')

def hobbies(request):
    hobby = Hobby.objects.all()
    return render(request, 'hobbies.html', {'hobbies': hobby})

def portfolio(request):
    portfolios = PortfolioItem.objects.all()
    return render(request, 'portfolio.html', {'portfolios': portfolios})

def contact(request):
    return render(request, 'contact.html')

def hobby_details(request, pk):
    hobby = get_object_or_404(Hobby,pk=pk)
    return render(request, "hobby_details.html", {"hobby": hobby})

def portfolio_details(request, pk):
    portfolios = get_object_or_404(PortfolioItem, pk=pk)
    return render(request, "portfolio_details.html", {"portfolio": portfolios})

def contact_view (request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('contact_success')
    return render(request, 'contact.html', {'form': form})

def contact_success(request):
    return render(request, 'contact_success.html')

@login_required
def portfolio_add(request):
    form = PortfolioForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('portfolio')
    return render(request, 'portfolio_form.html', {'form': form})

@login_required
def portfolio_edit(request, pk):
    item = get_object_or_404(PortfolioItem, pk=pk)
    form = PortfolioForm(request.POST or None, request.FILES or None, instance=item)
    if form.is_valid():
        form.save()
        return redirect('portfolio_details', pk=pk)
    return render(request, 'portfolio_form.html', {'form': form})

@login_required
def portfolio_delete(request, pk):
    item = get_object_or_404(PortfolioItem, pk=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('portfolio')
    return render(request, 'portfolio_confirm_delete.html', {'portfolio': item})

def logout_view(request):
    logout(request)
    return redirect('home')
