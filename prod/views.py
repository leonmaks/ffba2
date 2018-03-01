from django.views.generic import ListView, CreateView, UpdateView, FormView
from django.views.generic.edit import SingleObjectMixin
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy

from misc.edit import MasterDetailEditView
from . import forms as f
from . import models as m


class ProductTypeList(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    permission_required = ("prod.product_type_list")
    model = m.ProductType
    template_name = "prod/product_type_list.html"

    def get_queryset(self):
        return m.ProductType.objects.order_by("code")


class ProductTypeCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    permission_required = ("prod.product_type_create")
    model = m.ProductType
    fields = ["code", "name", "show_order"]
    template_name = "prod/product_type.html"


class ProductTypeUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    permission_required = ("prod.product_type_update")
    model = m.ProductType
    fields = ["code", "name", "show_order"]
    template_name = "prod/product_type.html"


class ProductList(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    permission_required = ("prod.product_list")
    model = m.Product
    template_name = "prod/product_list.html"

    def get_queryset(self):
        return m.Product.objects.prefetch_related("product_type").order_by("name")


class ProductCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    permission_required = ("prod.product_create")
    model = m.Product
    fields = ["name", "desc", "product_type", "code"]
    template_name = "prod/product.html"


class ProductUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    permission_required = ("prod.product_update")
    model = m.Product
    fields = ["name", "desc", "product_type", "code"]
    template_name = "prod/product.html"


class ProductCompositionEdit(LoginRequiredMixin, PermissionRequiredMixin, MasterDetailEditView):
    permission_required = ("prod.product_composition_list")
    model = m.Product
    fields = ["name", "desc", "product_type", "code"]
    detail_formset_class = f.ProductCompositionFormSet
    detail_queryset = m.ProductComposition.objects.filter(composition__exact=27)
    template_name = "prod/product_composition_edit.html"
    success_url = reverse_lazy("prod:product-composition-edit")
    product_composition = None

    def get_success_url(self):
        url_ = super(ProductCompositionEdit, self).get_success_url()
        if self.object:
            url_ += str(self.object.pk)
        return url_

    # def get_context_data(self, **kwargs):
    #     context_ = super(ProductCompositionEdit, self).get_context_data(**kwargs)
    #     if self.product_composition:
    #         context_["product_composition"] = self.product_composition
    #     return context_

    # def get(self, request, *args, **kwargs):
    #     response_ = super().get(request, *args, **kwargs)
    #     self.product_composition = f.ProductCompositionFormSet()
    #     return response_

    # def post(self, request, *args, **kwargs):
    #     self.product_composition = f.ProductCompositionFormSet(queryset=m.ProductComposition.objects.filter(composition__exact='O'))
    #     return super(ProductCompositionEdit, self).get(request, *args, **kwargs)


    # def form_valid(self, form):

    #     self.object = form.save()

    #     return super(ProductCompositionEdit, self).form_valid(form)

    # def get(self, request, *args, **kwargs):
    #     return HttpResponse("Hello, World!")


# class ProductCompositionEdit(EditView):
#     # class ProductCompositionUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
#     #	permission_required = ("prod.product_composition_update")
#     model = m.ProductComposition
#     fields = ["product", "name", "note", "weight_initial", "weight_final"]

# template_name = "prod/product_composition_edit.html"


#	formset = None
#
#	def get_object(self, queryset=None):
#		obj_ = super(ProductCompositionUpdate, self).get_object(queryset)
#		print("".join(["X: get_object-01: obj=", str(obj_)]))
#
#		self.formset = f.ProductRelFormSet(instance=obj_)
#		print("".join(["X: get_object-02: formset=", str(self.formset)]))
#
#		return obj_
#
#	def get_context_data(self, **kwargs):
#		ctx_ = super(ProductCompositionUpdate, self).get_context_data(**kwargs)
#		ctx_["formset"] = self.formset
#		return ctx_

#	def get_form_kwargs(self):
#		print("".join(["X: get_form_kwargs-01: self=", str(self)]))
#		kwargs_ = super(ProductCompositionUpdate, self).get_form_kwargs()
#		kwargs_.update(self.kwargs)
#		print("".join(["X: get_form_kwargs-02: kwargs=", str(kwargs_)]))
#		return kwargs_



# class ProductCompositionUpdate(FormView):
#	form_class = inlineformset_factory(m.Product, m.ProductRelation, fk_name="up", extra=1, fields=["link"])
#	template_name = "product_compositon_update"
#
#	def form_valid(self, formset):
#		cnt_ = len(formset.save())
#		if cnt_ == 0:
#			messages.success(self.request, "%s compositions have been updated" % cnt_)
#
#		return redirect("#", self.up_id)
#
#	def get_context_data(self, **kwargs):
#		print(" ".join(["X: get_context_data-01:", "self=", str(self), "kwargs=", str(**kwargs)]))
#		ctx_ = super(ProductCompositionUpdate, self).get_context_data(**kwargs)
#		print(" ".join(["X: get_context_data-02:", "ctx=", str(ctx_)]))
#		ctx_ = ctx_.update({"col3":"Delete?"})
#		return ctx_
#
#	def get_form_kwargs(self):
#		print(" ".join(["X: get_form_kwargs-01:", "self=", str(self)]))
#		self.up_id = self.kwargs["up_id"]
#		self.up = get_object_or_404(Product, pk=self.up_id)
#		kwargs_ = super(ProductCompositionUpdate, self).get_form_kwargs()
#		kwargs_.update({"instance":self.up})
#		return kwargs_



# class ProductPurchaseList(LoginRequiredMixin, PermissionRequiredMixin, ListView):
#	permission_required = ("prod.product_purchase_list")
#	model = m.ProductPurchase
#
#
# class ProductPurchaseCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
#	permission_required = ("prod.product_purchase_create")
#	template_name = "prod/productpurchase_form.html"
#	form_class = forms.ProductPurchaseMultiForm
#	success_url = reverse_lazy("home")
#
#	def form_valid(self, form):
#		expense = form["expense"].save()
#		product_purchase = form["product_purchase"].save(commit=False)
#		product_purchase.expense = expense
#		product_purchase.save()
#		return redirect(self.get_success_url())
