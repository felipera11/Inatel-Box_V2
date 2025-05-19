from django.core.exceptions import ValidationError
from django import forms
from .models import PrintModel

class PrintModelForm(forms.ModelForm):
    MATERIAL_CHOICES = [
        ('ABS', 'ABS'),
        ('PLA', 'PLA'),
        ('TPU', 'TPU'),
        ('PETG', 'PETG'),
    ]

    material = forms.ChoiceField(choices=MATERIAL_CHOICES)

    class Meta:
        model = PrintModel
        fields = ['model_name', 'stl_file', 'material', 'infill_percentage', 'layer_height']
    
    def clean_stl_file(self):
        file = self.cleaned_data.get('stl_file')
        if file:
            if not file.name.endswith('.stl'):
                raise ValidationError("Only STL files are allowed.")
        return file

    def clean_infill_percentage(self):
        infill_percentage = self.cleaned_data.get('infill_percentage')
        if infill_percentage is not None:
            if not (0 <= infill_percentage <= 100):
                raise ValidationError("Infill percentage must be between 0 and 100.")
        return infill_percentage

    def clean_layer_height(self):
        layer_height = self.cleaned_data.get('layer_height')
        if layer_height is not None:
            if not (0.08 <= layer_height <= 0.4):
                raise ValidationError("Layer height must be between 0.08 mm and 0.4 mm.")
        return layer_height
