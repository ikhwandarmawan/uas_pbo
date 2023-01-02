from django.contrib import admin
from django.urls import path
from webgis.views import *
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name="homepage"),
    path('login/', LoginView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(next_page='/'), name="logout"),
    path('tambahpeta/', tambahLokasi, name="tambahpeta"),
    path('editpeta/<int:id>/', editLokasi, name="editpeta"),
    path('hapuspeta/<int:id>/', hapusPeta, name="hapuspeta"),
    path('tambahtips/', tambahTips, name="tambahtips"),
    path('edittips/<int:id>/', editTips, name="edittips"),
    path('hapustipsa/<int:id>/', hapusTips, name="hapustips"),
]
