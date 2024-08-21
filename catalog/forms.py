from django import forms

from catalog.models import Product
class ProductForm(forms.ModelForm):
    dirty_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']
    class Meta:
        model = Product
        fields = '__all__'

    def clean_name(self):
        cleaned_data = self.cleaned_data['name']

        for word in ProductForm.dirty_words:
            if word in cleaned_data:
                raise forms.ValidationError('В названии использовано запрещенное слово')

        return cleaned_data

    def clean_description(self):
        cleaned_data = self.cleaned_data['description']

        for word in ProductForm.dirty_words:
            if word in cleaned_data:
                raise forms.ValidationError('В описании использовано запрещенное слово')

        return cleaned_data
