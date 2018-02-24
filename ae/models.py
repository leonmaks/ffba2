from django.db import models

from misc import models as misc
from org import models as org


class CashRegister(misc.AuditMixin, misc.Root):
    name = models.CharField(max_length=200)
    org_unit = models.ForeignKey(org.OrgUnit, on_delete=models.PROTECT, related_name="cash_registers")
    show_order = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "ffba_cash_register"
        unique_together = ('name', 'org_unit')
        ordering = ['show_order']


class CashRecord(misc.RecordDateMixin, misc.AuditMixin, misc.Root):
    cash_register = models.ForeignKey(CashRegister, on_delete=models.PROTECT, unique_for_date="record_date", related_name="cash_records")
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    checks = models.IntegerField(null=True, blank=True)
    url = models.URLField(max_length=1000, null=True, blank=True)


#	def save(self, *args, **kwargs):
#		# Check how the current values differ from ._loaded_values. For example,
#		# prevent changing the creator_id of the model. (This example doesn't
#		# support cases where 'creator_id' is deferred).
#		#if not self._state.adding and (
#		#		self.creator_id != self._loaded_values['creator_id']):
#		#	raise ValueError("Updating the value of creator isn't allowed")
#		self.created_by = etc_models.Root.thread.request.user
#		#print("created_by_id=%s" % etc_models.Root.thread.request.user.id)
#		super(CashRecord, self).save(*args, **kwargs)

    #def __str__(self):
    #	return unicode(self.record_date)

    class Meta:
        db_table = "ffba_cash_record"
        ordering = ['record_date', 'cash_register']

        permissions = (
            ("cash_record_create", "cashrecord / create"),
            ("cash_record_create_any", "cashrecord / createany"),
            ("cash_record_update", "cashrecord / update"),
            ("cash_record_update_any", "cashrecord / updateany"),
            ("cash_record_list", "cashrecord / list"),
            ("cash_record_list_all", "cashrecord / listall"),
        )


#class Expense(etc_models.RecDateTimeMixin, etc_models.RootAu):
#
#	UNDEFINED = 'UNDEF'
#	PRODUCT_PURCHASE = 'PROD_PURCHASE'
#
#	EXPENSE_TYPE_CHOICES = (
#		(UNDEFINED, "Undefined"),
#		(PRODUCT_PURCHASE, "Product Purchase"),
#	)
#
#	type = models.CharField(max_length=30, choices=EXPENSE_TYPE_CHOICES, default=UNDEFINED)
#	unit_price = models.DecimalField(max_digits=15, decimal_places=5, null=True, blank=True)
#	units = models.IntegerField(null=True, blank=True)
#	amount = models.DecimalField(max_digits=15, decimal_places=5)
#
#	def save(self, *args, **kwargs):
#
#		if self.amount is None and self.unit_price and self.units:
#			self.amount = self.unit_price * self.units
#
#		super(Expense, self).save(*args, **kwargs)
#
#	def __str__(self):
#		return self.type + "; unitprice=" + str(self.unit_price) + "; units=" + str(self.units) + "; amount=" + #str(self.amount)
#
#	class Meta:
#		db_table = "ffba_expense"
