from django.shortcuts import render
def base(request):
    title = "Base"
    context = {
        "title_docum":title,
    }
    return render(request,"base.html",context)