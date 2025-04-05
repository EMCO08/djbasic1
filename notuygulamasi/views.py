from django.shortcuts import render, redirect
from .models import Not

def ana_sayfa(request):
    if request.method == 'POST':
        icerik = request.POST.get('icerik')
        if icerik:
            Not.objects.create(icerik=icerik)
        return redirect('ana_sayfa')
    
    notlar = Not.objects.all().order_by('-olusturulma_tarihi')
    return render(request, 'ana_sayfa.html', {'notlar': notlar})
