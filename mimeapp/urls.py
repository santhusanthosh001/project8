from django.contrib import admin
from mimeapp import views
from django.urls import path
urlpatterns=[
    path('admin/',admin.site.urls),
    path('html',views.Htmlview.as_view(), name="Htmlview"),
    path('excel',views.Excelview.as_view(),name="Excelview"),
    path('xml',views.Xmlview.as_view(),name="Xmlviews"),

]