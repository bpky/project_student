from django.shortcuts import render

# Create your views here.
def User_dashboard(request):
    context = {
        "welcome_msg": "welcome to information tracker",
    }
    return render(request, "user/dashboard.html", context)

