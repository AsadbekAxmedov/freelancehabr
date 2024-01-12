from django.urls import path
from .views import *


urlpatterns = [
    path("", home, name="home"),
    path("order", order, name="order"),
    path("order/<int:pk>/", order_detail, name="order_detail"),
    path("order-req/<int:pk>", order_req, name="order_req"),
    path("base", base, name="base"),
    path("services", services, name="services"),
    path("projects", projects, name="projects"),
    path("klub", klub, name="klub"),
    path("introduction", introduction, name="introduction"),
    path("personal", personal, name="personal.html"),
    path("person", person, name="person.html"),
    path("plus", plus, name="plus.html"),
    path("add_order", add_order, name="add_order"),
    path("specialization", specialization, name="specialization.html"),
    path("offer_delete/<int:order>/<int:offer>", offer_delete, name="delete_offer"),
    path("new", new, name="new"),
    path("design", design, name="design"),
    path("asad", asad, name="asad"),
    path("change-role/", change_role, name="change_role"),
    path("download/", download_file, name="download_file"),
]
