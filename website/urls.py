from unicodedata import name
from django.urls import path, re_path
from .views import careers, child_page, home, about, gallery, contact, newsletter, page, apply


urlpatterns = [
    path('', home, name="home"),
    re_path(r'^about/?$', about, name="about"),
    re_path(r'^gallery/?$', gallery, name="gallery"),
    re_path(r'^contact/?$', contact, name="contact"),
    re_path(r'^careers/?$', careers, name="careers"),
    re_path(r'^careers/apply/?$', apply, name="apply"),
    re_path(r'^newsletter/?$', newsletter, name="newsletter"),
    # path("<slug>/", page, name="page")
    # path(r'^(?P<path>.+)/(?P<slug>[\w-]+)/$', page, name='page')
    re_path(r'^(?P<parent_slug>[\w-]+)$', page),
    re_path(r'^(?P<parent_slug>[\w-]+)/(?P<child_slug>[\w-]+)/$', child_page),

]
