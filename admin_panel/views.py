from django.shortcuts import render, get_object_or_404, redirect
from core.models import PrintModel

def admin_model_list(request):
    models = PrintModel.objects.all().order_by('-submitted_at')
    return render(request, 'admin_panel/model_list.html', {'models': models})

def admin_model_detail(request, pk):
    print_model = get_object_or_404(PrintModel, pk=pk)
    if request.method == 'POST':
        # Calculate and update the budget logic
        print_model.budget = calculate_budget(print_model)  # Placeholder for your logic
        print_model.save()
        return redirect('admin_panel:model_detail', pk=print_model.pk)
    return render(request, 'admin_panel/model_detail.html', {'print_model': print_model})

def calculate_budget(print_model):
    # Logic to calculate the budget based on model details
    return 50.00  # Replace this with actual calculation logic
