from django.urls import path

from . import views as v


app_name = "ae"

urlpatterns = [
    #url(r"daily-cash-record/$", cash_records.daily_cash_record, name="daily_cash_record"),
    path(r"cash-record-list/", v.CashRecordList.as_view(), name="cash-record-list"),
    path(r"cash-record-create/", v.CashRecordCreate.as_view(), name="cash-record-create"),
    path(r"cash-record-update/<int:pk>/", v.CashRecordUpdate.as_view(), name="cash-record-update"),
]
