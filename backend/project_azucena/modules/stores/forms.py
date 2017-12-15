from django.forms import ModelForm, TextInput
from .models import Store
from django.utils.translation import ugettext_lazy as _

# Create the form class.
class StoreForm(ModelForm):
    class Meta:
        model = Store
        fields = ['username','name_store', 'address_store', 'city_store', 'state_store', 'postal_store', 'country_store', 'phone_store', 'send_box', 'clabe']
        labels = {
            'username': _('Username'),
        }
        widgets = {
            'username': TextInput(
                    attrs={'readonly':'readonly'}
                ),
        }
