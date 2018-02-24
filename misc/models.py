import threading
from datetime import date

from django.contrib.auth import models as auth_models
from django.db import models


class Root(models.Model):
    thread = threading.local()

    class Meta:
        abstract = True


class AuditMixin(models.Model):
    create_user = models.ForeignKey(auth_models.User, on_delete=models.PROTECT, related_name="%(class)s_created_by")
    create_dt = models.DateTimeField("Datetime Created", auto_now_add=True)
    modify_user = models.ForeignKey(auth_models.User, on_delete=models.PROTECT, related_name="%(class)s_modify_user", null=True, blank=True)
    modify_dt = models.DateTimeField("Datetime Modified", null=True, blank=True, auto_now=True)

    def save(self, *args, **kwargs):

        if hasattr(Root.thread, 'request'): user_ = Root.thread.request.user
        else: user_ = auth_models.User.objects.get(id=1)

        if self.pk is None: self.create_user = user_
        else: self.modify_user = user_

        super(AuditMixin, self).save(*args, **kwargs)

    class Meta:
        abstract = True


class FdTdMixin(models.Model):
    fd = models.DateTimeField("From Datetime", null=True, blank=True, auto_now=True)
    td = models.DateTimeField("To Datetime", null=True, blank=True, auto_now=True)

    class Meta:
        abstract = True


class RecordDateMixin(models.Model):
    record_date = models.DateField("Date", default=date.today)

    class Meta:
        abstract = True
