from django.http import HttpResponse

tax_rate = 0.15
def default(request):
    return HttpResponse("<html><body><h1> this is a site to calculate tax </html></body></h1>")

def calculate(request, num):
    return HttpResponse(request,"tax_app/calculate.html", {"number": num , "tax": tax_rate , "after_tax": ((num*tax_rate)) + num})

def tax(request):
    return HttpResponse(request,"tax_app/tax.html", {"tax": tax_rate})