from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

# Create your views here.
data="""<body bgcolor=lightblue> <table><tr><th>empname</th><th>empid</th><th>empsal</th></tr>
        <tr><td>rani</td><td>1003</td><td>6789</td></tr>
        <tr><td>vani</td><td>1004</td><td>6789</td></tr>
        <tr><td>shalni</td><td>1005</td><td>2389</td></tr>
        <tr><td>yamni</td><td>1006</td><td>67866</td></tr>
        <tr><td>dhamini</td><td>1007</td><td>62389</td></tr></table>"""
class Htmlview(View):
    def get(self,request):
        return HttpResponse(data,content_type="text/html")
class Excelview(View):
    def get(self,request):
        return HttpResponse(data,content_type="application/vnd.ms_excel")
class Xmlview(View):
    def get(self,request):
        return HttpResponse(data,content_type="application/xml")
