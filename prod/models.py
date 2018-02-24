from django.db import models
from django.urls import reverse_lazy
# from mptt.models import MPTTModel, TreeForeignKey

from misc import models as m


class ProductType(m.AuditMixin, m.Root):
    code = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=500, unique=True)
    show_order = models.CharField(max_length=50, null=True, blank=True)

    def get_absolute_url(self):
        return reverse_lazy("prod:product-type-list")

    def __str__(self):
        return self.name

    class Meta:
        db_table = "ffba_product_type"


class Product(m.AuditMixin, m.Root):
    code = models.CharField(max_length=20, unique=True, null=True, blank=True)
    # type = models.ForeignKey(ProductType, related_name="products")
    product_type = models.ForeignKey(ProductType, on_delete=models.PROTECT, to_field="code", db_column="product_type_code")
    name = models.CharField(max_length=500)
    desc = models.CharField(max_length=5000, null=True, blank=True)

    def get_absolute_url(self):
        return reverse_lazy("prod:product-list")

    def __str__(self):
        return self.name

    class Meta:
        db_table = "ffba_product"


class ProductComposition(m.AuditMixin, m.Root):
    composition = models.ForeignKey(Product, on_delete=models.PROTECT, to_field="code", db_column="composition_code", related_name="composition")
    product = models.ForeignKey(Product, on_delete=models.PROTECT, to_field="code", db_column="product_code", related_name="product")
    note = models.TextField(null=True, blank=True)
    weight_initial = models.DecimalField(max_digits=11, decimal_places=5, null=True, blank=True)
    # weight_final = models.DecimalField(max_digits=11, decimal_places=5, null=True, blank=True)
    # weight_reduction = models.DecimalField(max_digits=6, decimal_places=4, null=True, blank=True)
    # weight_initial_per_gram = models.DecimalField(max_digits=11, decimal_places=5, null=True, blank=True)
    # weight_final_per_gram = models.DecimalField(max_digits=11, decimal_places=5, null=True, blank=True)

    class Meta:
        db_table = "ffba_product_composition"

#
#	#def get_absolute_url(self):
#	#	return reverse_lazy("prod:product-link")

	# def __str__(self):
	# 	return " ".join([self.up.name, " >-- ", self.entry.name])


# class ProductPurchase(m.Root):
#	expense = models.OneToOneField(acc_models.Expense, on_delete=models.PROTECT, related_name="product_purchase")
#	product = models.ForeignKey(Product, related_name="products_purchases", null=True, blank=True)
#	product_text = models.CharField(max_length=500, null=True, blank=True)
#	#+ provider
#	provider_text = models.CharField(max_length=500, null=True, blank=True)
#
#	history = HistoricalRecords(table_name="ffba_product_purchase_history")
#
#	def get_absolute_url(self):
#		return reverse_lazy("prod:product-purchase-list")
#
#	#def __str__(self):
#		#return self.name
#
#	class Meta:
#		db_table = "ffba_product_purchase"
