
from django.contrib import admin
from django.urls import path, include

from skaters.views import SkatersAPIList, SkatersAPIUpdate, SkatersAPIDestroy

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/skaters/', SkatersAPIList.as_view()),
    path('api/v1/skaters/<int:pk>/', SkatersAPIUpdate.as_view()),
    path('api/v1/skatersdelete/<int:pk>/', SkatersAPIDestroy.as_view()),
    path('api/v1/drf-auth/', include('rest_framework.urls')),
]
