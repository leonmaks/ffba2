import datetime
from django.views import generic
from django.utils import timezone
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy

from . import models as m
from . import forms as f


class CashRecordList(LoginRequiredMixin, PermissionRequiredMixin, generic.ListView):
    permission_required = ("ae.cash_record_list")
    template_name = "ae/cash_record_list.html"
    context_object_name = "cash_records"

    def get_queryset(self):
        # list = m.CashRecord.objects.order_by("-record_date")
        l_ = m.CashRecord.objects.prefetch_related("cash_register", "create_user", "modify_user").order_by("-record_date", "cash_register__org_unit", "cash_register__show_order")
        if not self.request.user.has_perm("ae.cash_record_list_all"):
            l_ = l_.exclude(record_date__lt=(timezone.now()-datetime.timedelta(days=7))).filter(create_user=self.request.user)
        return l_


class CashRecordCreate(LoginRequiredMixin, PermissionRequiredMixin, generic.edit.CreateView):
    permission_required = ("ae.cash_record_create")
    form_class = f.CashRecordForm
    template_name = "ae/cash_record.html"
    success_url = reverse_lazy("ae:cash-record-list")

    def form_valid(self, form):
        form.instance.create_user = self.request.user
        return super(CashRecordCreate, self).form_valid(form)


class CashRecordUpdate(LoginRequiredMixin, generic.edit.UpdateView):
    permission_required = ("ae.cash_record_update")
    model = m.CashRecord
    form_class = f.CashRecordForm
    template_name = "ae/cash_record.html"
    success_url = reverse_lazy("ae:cash-record-list")
