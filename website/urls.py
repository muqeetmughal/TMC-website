from unicodedata import name
from django.urls import path, re_path
from .views import careers, child_page, home, about, gallery, contact, newsletter, page


urlpatterns = [
    path('', home, name="home"),
    path('about/', about, name="about"),
    path('gallery/', gallery, name="gallery"),
    path('contact/', contact, name="contact"),
    path('careers/', careers, name="careers"),
    path('newsletter/', newsletter, name="newsletter"),
    # path("<slug>/", page, name="page")
    # path(r'^(?P<path>.+)/(?P<slug>[\w-]+)/$', page, name='page')
    re_path(r'^(?P<parent_slug>[\w-]+)$', page),
    re_path(r'^(?P<parent_slug>[\w-]+)/(?P<child_slug>[\w-]+)/$', child_page),

]
