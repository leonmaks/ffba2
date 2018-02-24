from django import forms
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from . import models
from misc import models as misc
#from etc import forms as etc_forms


class CashRecordForm(forms.ModelForm):

    def clean_record_date(self):
        record_date = self.cleaned_data['record_date']
        user = misc.Root.thread.request.user
        if not user.has_perm("acc.cash_record_create_any"):
            date_diff = (record_date-timezone.now().date()).days
            if date_diff > 0:
                self._errors["record_date"] = [_("Cash record in the future is not permitted")]
            if date_diff < -7:
                self._errors["record_date"] = [_("Cash record older than 7 days is not permitted")]
        return record_date

    #def get_queryset(self):
    #	return super(CashRecordForm, self).get_queryset().select_related('cash_register')

    class Meta:
        model = models.CashRecord
        fields = ["cash_register", "record_date", "amount", "checks"]
        # widgets = {
        #     "cash_register": forms.Select(attrs={"class": "form-control"}),
        #     "record_date": forms.DateInput(attrs={"class": "form-control"}),
        #     "amount": forms.NumberInput(attrs={"class": "form-control"}),
        #     "checks": forms.NumberInput(attrs={"class": "form-control"}),
        #     # "url": forms.URLInput(attrs={"class": "form-control"}),
        # }
        help_texts = {
            "cash_register": _("Money receiving terminal"),
            "record_date": _("Reporting Date"),
            "amount": _("Total sales per day"),
            "checks": _("Number of checks per day"),
        }
