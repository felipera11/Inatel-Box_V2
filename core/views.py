# core/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import PrintModel
from .forms import PrintModelForm

@login_required
def home(request):
    return render(request, 'core/home.html')

@login_required
def send_model(request):
    if request.method == 'POST':
        form = PrintModelForm(request.POST, request.FILES)
        if form.is_valid():
            print_model = form.save(commit=False)
            print_model.user = request.user
            print_model.save()
            return redirect('core:print_model_detail', pk=print_model.pk)
    else:
        form = PrintModelForm()
    
    return render(request, 'core/send_model.html', {'form': form})

@login_required
def history(request):
    orders = PrintModel.objects.filter(user=request.user).order_by('-submitted_at')
    return render(request, 'core/history.html', {'orders': orders})

@login_required
def print_model_detail(request, pk):
    print_model = get_object_or_404(PrintModel, pk=pk)
    return render(request, 'core/print_model_detail.html', {'print_model': print_model})
