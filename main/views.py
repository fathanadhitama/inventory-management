from django.shortcuts import render

# Create your views here.
context = {
    'nama' : 'Fathan Naufal Adhitama',
    'kelas' : 'PBP E'
}

def show_main(request):
    return render(request, "main.html", context)