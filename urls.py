from django.contrib import admin
from django.urls import path, include

urlpatterns = [
path('admin/', admin.site.urls),
path('', include('elections.urls')), #elections app을 include 해주는것임.
]
