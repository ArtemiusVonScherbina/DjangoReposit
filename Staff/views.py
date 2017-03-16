from django.shortcuts import render
from .models import Staff
# Create your views here.
def main_menu(request):
    staffs = Staff.objects.all()
    print (staffs)
    title = "Main"
    context = {
        "title_docum":title,
        "staff":staffs
    }
    return render(request,"main_menu.html",context)