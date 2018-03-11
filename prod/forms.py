from django.forms import ModelForm
from django.forms import inlineformset_factory

from . import models as m


class ProductCompositionForm(ModelForm):

    class Meta:
        model = m.ProductComposition
        fields = ["product", "weight_initial", "note"]


ProductCompositionFormSet = inlineformset_factory(m.Product, m.ProductComposition, form=ProductCompositionForm, fk_name="up")


# class ProductForm(ModelForm):

#     class Meta:
#         model = m.Product
#         fields = ["code", "product_type", "name", "desc"]
