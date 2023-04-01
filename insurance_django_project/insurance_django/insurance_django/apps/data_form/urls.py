from django.conf.urls import url
from . import views

urlpatterns = [
    # get 获取表单数据
    url(r'^commitForm/(?P<name_id>[0-2]{1,2})/(?P<token>.{100,200})', views.ComForm.as_view()),
    # post提交表单数据
    url(r'^dataForm/(?P<name_id>[0-2]{1,2})/(?P<token>.{100,200})', views.DataComForm.as_view()),
    # 获取历史表单
    url(r'^historyForm/(?P<token>.{100,200})', views.GethistoryForm.as_view()),
    # 获取图片接口
    url(r'^image_url', views.Image.as_view()),
]