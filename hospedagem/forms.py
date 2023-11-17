from django.forms import ModelForm
from .models import Hospedagem


class HospedagemForm(ModelForm):
    class Meta:
        model = Hospedagem
        fields = '__all__'