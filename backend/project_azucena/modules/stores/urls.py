from django.conf.urls import url
from .views import StoreList, StoreDetail, StoreAssistantList, StoreSearch, StoreRegister

urlpatterns = [
    url(r'^api/v1/stores/$', StoreList.as_view(), name="ListStore"),
    url(r'^api/v1/stores/(?P<id>[0-9a-f-]+)/$', StoreDetail.as_view(), name="DetailStore"),
    url(r'^api/v1/stores/details/$', StoreAssistantList.as_view(), name="StoreAssistantCutflowersList"),
    url(r'^api/v1/stores/search/(?P<state>[\w]+)/$', StoreSearch.as_view(), name="StoreSearch"),
    
    url(r'^stores/', StoreRegister ,name = "register"),
]
