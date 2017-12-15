from django.forms import ModelForm, ModelChoiceField
from .models import Cutflowers
from django.utils.translation import ugettext_lazy as _
from modules.stores.models import Store

# Create the form class.
class CutflowerForm(ModelForm):
    class Meta:
        model = Cutflowers
        fields = ['image_cutflower','name_cutflower','weight_cutflower','description_cutflower','price_cutflower','pricesend_cutflower','fkstore']
        widget = {
            'fkstore': ModelChoiceField(queryset=Store.objects.all())
            }
        labels = {
            'fkstore': _('Store'),
        }