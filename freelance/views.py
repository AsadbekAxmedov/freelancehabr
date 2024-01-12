from django.shortcuts import render, redirect
from .models import *
from users.models import *
from django.db.models import Q
from django.contrib import messages
from django.utils import timezone
from .forms import OrderForm
import mimetypes
import os
from django.http.response import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, "home.html")


def order(request):
    orders = Order.objects.all()
    search = request.GET.get("search")
    orders = (
        Order.objects.filter(
            Q(title__icontains=search) | Q(description__icontains=search)
        )
        if search
        else orders
    )
    return render(request, "order.html", {"orders": orders})


def order_detail(request, pk):
    order = Order.objects.get(pk=pk)
    response = (
        Response.objects.filter(order__id=pk).last()
        if request.user is not None
        else None
    )

    print(order.file.name, "------------------")
    return render(request, "order_detail.html", {"order": order, "response": response})


def offer_delete(request, order, offer):
    Response.objects.get(pk=offer).delete()
    return redirect(order_detail, order)


def order_req(request, pk):
    data = request.POST
    order_id = Order.objects.filter(id=pk).first()
    if request.method == "POST":
        response = Response.objects.create(
            user=request.user, order=order_id, offer=data.get("offer")
        )
        return redirect("order_detail", pk)

    return redirect("home")


def base(request):
    return render(request, "base.html")


def services(request):
    return render(request, "services.html")


def projects(request):
    return render(request, "projects.html")


def klub(request):
    return render(request, "klub.html")


def introduction(request):
    return render(request, "introduction.html")


def asad(request):
    return render(request, "asad.html")


def personal(request):
    data = request.POST
    if request.method == "POST":
        user = User.objects.filter(username=request.user).first()
        if user:
            print(request.FILES)
            print(request.FILES.get("resume"))
            user.avatar = request.FILES.get("resume")
            user.first_name = data.get("first_name")
            user.last_name = data.get("last_name")
            user.save()
            return redirect("personal.html")
    return render(request, "personal.html")


def person(request):
    return render(request, "person.html")


def plus(request):
    if request.method == "POST":
        return redirect("add_order")
    return render(request, "plus.html")


def add_order(request):
    data = request.POST
    technologs = Technology.objects.all()[:10]

    if data.get("price_type") == "NEGOTIABLE":
        price_type = NEGOTIABLE
    elif data.get("price_type") == "PROJECT":
        price_type = PROJECT
    else:
        price_type = HOUR

    if data.get("python"):
        python = Technology.objects.filter(name="Python").first()
    if data.get("django"):
        django = Technology.objects.filter(name="Django").first()
    if data.get("js"):
        js = Technology.objects.filter(name="Java Script").first()
    if data.get("go"):
        go = Technology.objects.filter(name="Go").first()
    if data.get("react"):
        react = Technology.objects.filter(name="React Js").first()
    if data.get("postgres"):
        postgres = Technology.objects.filter(name="PostgreSQL").first()
    if data.get("docker"):
        docker = Technology.objects.filter(name="Docker").first()

    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.title = data.get("title")
            # order.technology = set([python, django, js, go, react, postgres, docker])
            order.price = data.get("price", 0)
            order.price_type = price_type
            order.advertising = "300 кр. На 30 дней"
            order.views = len(User.objects.all())
            order.user = request.user
            order.file = request.FILES.get("resume")
            order.save()

            order.technology.add(python, django, go, js, react, docker, postgres)
            order.save()
        
        return redirect("add_order")
    form = OrderForm()

    return render(request, "add_order.html", {"form": form, "technologs": technologs})


def specialization(request):
    return render(request, "specialization.html")


def new(request):
    return render(request, "new.html")


def design(request):
    return render(request, "design.html")


def change_role(request):
    user = User.objects.filter(username=request.user).first()
    data = request.GET.get("action")
    if data == "customer":
        user.role = FREELANCER
        user.save()
        return redirect("home")
    else:
        user.role = CUSTOMER
        user.save()
        return redirect("home")





# Define function to download pdf file using template
def download_file(request):
    filename = request.GET.get("filename")
    if filename != "":
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        filepath = BASE_DIR + '/media/' + filename
        path = open(filepath, "rb")
        mime_type, _ = mimetypes.guess_type(filepath)
        response = HttpResponse(path, content_type=mime_type)
        response["Content-Disposition"] = "attachment; filename=%s" % filename
        return response
    else:
        return render(request, "file.html")
