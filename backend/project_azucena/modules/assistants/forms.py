from django.forms import ModelForm, ModelChoiceField
from .models import Assistants
from modules.stores.models import Store
from django.utils.translation import ugettext_lazy as _


# Create the form class.
class AssistantForm(ModelForm):
    class Meta:
        model = Assistants
        fields = ['name_assistants','phone_assistants','email_assistants','address_assistants','fkstore']
        widget = {
            'fkstore': ModelChoiceField(queryset=Store.objects.all())
            }
        labels = {
            'fkstore': _('Store'),
        }