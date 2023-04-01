from django.conf.urls import url
from . import views

urlpatterns = [
    # 注册 get
    url(r'^zusers/(?P<username>\w{5,20})/(?P<password>\w{6,20})/(?P<mobile>1[3-9]\d{9})', views.UserView.as_view()),
    # 登录 post
    url(r'^users/(?P<username>\w{5,20})/(?P<password>\w{6,20})', views.UserView.as_view()),
]