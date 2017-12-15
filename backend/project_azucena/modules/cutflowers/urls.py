from django.conf.urls import url
from .views import CutflowerRegister

urlpatterns = [
    url(r'^cutflower/', CutflowerRegister ,name = "register"),
]
