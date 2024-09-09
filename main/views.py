from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'title': 'Toko-ya',
        'name': 'Fathurrahman Kesuma Ridwan',
        'class': 'PBP E'
    }

    return render(request, "main.html", context)