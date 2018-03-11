from django.views.generic.edit import ModelFormMixin, ProcessFormView
from django.views.generic.detail import SingleObjectTemplateResponseMixin
from django.core.exceptions import ImproperlyConfigured


class BaseEditView(ModelFormMixin, ProcessFormView):
    """
    Base view for creating a new or editing exising object instance.

    Using this base class requires subclassing to provide a response mixin.
    Idea: https://stackoverflow.com/a/30948175/1423996
    """

    def get_object(self, queryset=None):
        try:
            return super().get_object(queryset)
        except AttributeError:
            return None

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().post(request, *args, **kwargs)


class EditView(SingleObjectTemplateResponseMixin, BaseEditView):
    """
    View for editing a new or existing object, with a response rendered by a template.
    """
    template_name_suffix = '_edit'


class BaseMasterDetailEditView(ModelFormMixin, ProcessFormView):
    """
    """
    detail_model = None
    detail_formset_class = None
    detail_formset = None
    detail_queryset = None

    def get_object(self, queryset=None):
        try:
            return super().get_object(queryset)
        except AttributeError:
            return None

    def get_context_data(self, **kwargs):
        context_ = super().get_context_data(**kwargs)
        if self.detail_formset:
            context_["detail_formset"] = self.detail_formset
        return context_

    def get_detail_formset_class(self):
        return self.detail_formset_class

    def get_detail_formset(self, detail_formset_class=None):
        from prod import models as m
        if detail_formset_class is None:
            detail_formset_class = self.get_detail_formset_class()
        return detail_formset_class(queryset=m.ProductComposition.objects.filter(up__exact=m.Product(pk=27)))
        # return detail_formset_class(self.get_detail_queryset())

    def get_detail_queryset(self):
        if self.detail_queryset is None:
            if self.detail_model:
                return self.detail_model._default_manager.all()
            else:
                raise ImproperlyConfigured(
                    "%(cls)s is missing a Detail QuerySet. Define "
                    "%(cls)s.detail_model, %(cls)s.detail_queryset, or override "
                    "%(cls)s.get_detail_queryset()." % {
                        'cls': self.__class__.__name__
                    }
                )
        return self.detail_queryset.all()

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.detail_formset = self.get_detail_formset()
        # self.product_composition = f.ProductCompositionFormSet(queryset=m.ProductComposition.objects.filter(composition__exact='O'))
        return super().get(request, *args, **kwargs)

    # def post(self, request, *args, **kwargs):
    #     self.object = self.get_object()
    #     return super().post(request, *args, **kwargs)


class MasterDetailEditView(SingleObjectTemplateResponseMixin, BaseMasterDetailEditView):
    """
    View for editing a new or existing object, with a response rendered by a template.
    """
    template_name_suffix = '_edit'
