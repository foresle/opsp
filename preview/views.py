from django.views.generic import TemplateView


class PreviewView(TemplateView):
    template_name = 'preview/preview.html'
