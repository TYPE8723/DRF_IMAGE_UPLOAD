from django.urls import path,include
from rest_framework.routers import SimpleRouter
from user.views import EmployeeViewSet

router = SimpleRouter()

router.register(r"employee",EmployeeViewSet)
urlpatterns = [
    path(r"",include(router.urls)),
]