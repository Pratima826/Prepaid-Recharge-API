from django.urls import path
from paytm_app .views import *
urlpatterns = [
    path("get-plans/", ShowAllPlans.as_view(), name="get-all-plans"),
    path("do-recharge/", RechargeView.as_view(), name="do-rechger-specific-plans")
]
