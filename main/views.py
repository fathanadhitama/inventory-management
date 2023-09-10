from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'nama' : 'Fathan Naufal Adhitama',
        'kelas' : 'PBP E'
    }

    return render(request, "main.html", context)