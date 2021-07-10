from django.forms.models import ModelForm

from house.models import House


class HouseCreateForm(ModelForm):
    class Meta:
        model = House
        exclude = ['owner', ]
