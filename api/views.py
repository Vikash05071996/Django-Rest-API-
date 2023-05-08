from django.http import HttpResponse
def home_page(request):
    print("hello home page")
    return HttpResponse("this is home page")
    