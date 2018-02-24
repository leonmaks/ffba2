from django.contrib.auth.models import User
from django.db import models

from misc import models as misc


class OrgUnit(misc.AuditMixin, misc.Root):
    name = models.CharField(max_length=500)
    up = models.ForeignKey('self', on_delete=models.PROTECT, null=True, blank=True)

    def __str__(self):
        return self.name if not self.up else self.name + " \\ " + str(self.up)

    class Meta:
        db_table = "ffba_orgunit"


class Profile(misc.Root):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    orgunit = models.ForeignKey(OrgUnit, on_delete=models.PROTECT)
    position = models.CharField(max_length=500, null=True, blank=True)
    social = models.URLField(null=True, blank=True)

    class Meta:
        db_table = "ffba_profile"
