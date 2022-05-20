from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from .models import Clients, Gallery, Page, Settings, Slider, Team
from .forms import ContactForm, NewsletterForm
# Create your views here.


def home(request):
    context = {}
    # query = Settings.objects.get(key="home_background_video")
    slider = Slider.objects.all()
    team = Team.objects.all()
    # try:
    #     context['home_background_video'] = query.file.url
    # except ValueError:
    #     context['home_background_video'] = ""
    # try:
    #     context['home_background_image'] = query.image.url
    # except ValueError:
    #     context['home_background_image'] = ""

    clients = Clients.objects.all()
    context['clients'] = clients
    context['slider'] = slider
    context['team'] = team
    return render(request, "pages/home.html", context)


def about(request):
    context = {}
    query = Settings.objects.get(key="about_background")
    team = Team.objects.all()
    context['page_heading'] = "About TMC"
    context['parent_page'] = "Home"
    context['child_page'] = "About"
    context['team'] = team
    try:
        context['about_background'] = query.image.url
    except ValueError:
        context['about_background'] = ""
    return render(request, "pages/about.html", context)


def gallery(request):
    context = {}
    context['page_heading'] = "Check our memories"
    context['parent_page'] = "Home"
    context['child_page'] = "Gallery"
    gallery = Gallery.objects.all()

    context['gallery'] = gallery

    return render(request, "pages/gallery.html", context)


def careers(request):
    context = {}
    context['page_heading'] = "Join TMC to Success"
    context['parent_page'] = "Home"
    context['child_page'] = "Careers"

    return render(request, "pages/careers.html", context)


def contact(request):

    context = {}

    context['page_heading'] = "Get in Touch"
    context['parent_page'] = "Home"
    context['child_page'] = "Contact"

    context['form'] = ContactForm

    if request.method == "POST":

        form = ContactForm(request.POST)

        print(form.data)
        if form.is_valid():
            form.save()
            messages.success(
                request, 'Thanks for contacting us we will respond you soon!!')

            return redirect("contact")
        else:
            messages.error(request, 'Sorry please check your form again!')

            return redirect("contact")

    return render(request, "pages/contact.html", context)


def newsletter(request):

    if request.method == "POST":

        form = NewsletterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thanks for submitting your Email!')

    return redirect("home")


def page(request, parent_slug):
    context = {}
    page = get_object_or_404(Page, slug=parent_slug)
    context['page'] = page
    context['page_heading'] = page.name
    context['parent_page'] = "Home"
    context['child_page'] = page.name

    return render(request, "pages/page.html", context)


def child_page(request, parent_slug, child_slug):

    context = {}
    page = get_object_or_404(Page, slug=child_slug)
    context['page'] = page
    context['page_heading'] = page.name
    context['parent_page'] = page.parent.name
    context['child_page'] = page.name

    return render(request, "pages/page.html", context)
