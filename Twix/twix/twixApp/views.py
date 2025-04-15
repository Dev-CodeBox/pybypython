from django.shortcuts import render
from .models import Twix
from .forms import TwixForm
from django.shortcuts import get_object_or_404, redirect

# Create your views here.

def home(request):
    return render(request, 'website/twixApp.home.html')

def all_twix(request):
    tweeks = Twix.objects.all()
    return render(request, 'website/twixApp.all_twix.html', {'tweeks': tweeks})

def create_twix(request):
    if request.method == 'POST':
        form = TwixForm(request.POST, request.FILES)
        if form.is_valid():
            twix = form.save(commit=False)
            twix.user = request.user
            twix.save()
            return redirect('all_twix')
    else:
        form = TwixForm()
    return render(request, 'website/twixApp.create_twix.html', {'form': form})

def edit_twix(request, twix_id):
    twix = get_object_or_404(Twix, pk=twix_id, user = request.user)
    if request.method == 'POST':
        form = TwixForm(request.POST, request.FILES, instance=twix)
        if form.is_valid():
            twix = form.save(commit=False)
            twix.user = request.user
            twix.save()
            return redirect('all_twix')
    else:
        form = TwixForm(instance=twix)
    return render(request, 'website/twixApp.edit_twix.html', {'form': form, 'twix': twix})

def delete_twix(request, twix_id):
    twix = get_object_or_404(Twix, pk=twix_id, user = request.user)
    if request.method == 'POST':
        twix.delete()
        return redirect('all_twix')
    return render(request, 'website/twixApp.delete_twix.html', {'twix': twix})