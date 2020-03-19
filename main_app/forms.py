from django.forms import ModelForm
from .models import Feeding, Toy

class FeedingForm(ModelForm):
    class Meta:
        model = Feeding
        fields = ['date', 'meal']


class ToyForm(ModelForm):
    class Meta:
        model = Toy
        fields = '__all__'
