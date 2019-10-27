from django.forms import forms

from propmanager.models import Property, Owner


class PropertyForm(forms.ModelForm):
    class Meta:
        model = Property
        fields = ('address', 'value', 'location', 'property_type', 'owner')


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['owner'].queryset = Owner.objects.none()