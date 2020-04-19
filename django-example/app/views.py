from pprint import pformat

from django.views.generic import TemplateView


class HelloWorldView(TemplateView):
    template_name = "helloworld.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["scope"] = pformat(self.request.scope)
        return context
