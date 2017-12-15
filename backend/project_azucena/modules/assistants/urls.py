from django.conf.urls import url
from .views import AssistantRegister #, AssistantDetail

urlpatterns = [
    url(r'^assistant/', AssistantRegister ,name = "register"),
    # url(r'^assistant/search/(?P<id>[0-9a-f-]+)/$', AssistantDetail.as_view() ,name = "details"),
]
