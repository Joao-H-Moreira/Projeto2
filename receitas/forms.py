from django import from .forms import 


class ContatoForm(forms.Form):
    nome = forms.CharField(
        label = 'Nome',
        max_length = 100,
        widget = forms.TextInput(attrs={
            'class': 'mt-1 block w-full p-2 bg-gray-700 border border border-gray-600 '
        })
    )