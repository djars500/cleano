from django.shortcuts import redirect, render
from .forms import ContactForm, ZayavkaForm
from django.contrib.auth.decorators import login_required
from .models import Zayavka, Courier, Result

def main(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = ContactForm()  

    results = Result.objects.all()
        
    return render(request, 'main.html', {'form': form, 'results': results})


@login_required(login_url="signup")
def myAppView(request):

    if request.method == 'POST':
        form = ZayavkaForm(request.POST)
        
        
        if form.is_valid():
            new = form.save(commit=False)
            new.user = request.user
            new.save()
            print('Success')
            print(request.user)
        else:
            print('Error')

            return redirect('/myapps/')
    else:
        form = ZayavkaForm()

    
    

    couriers = Courier.objects.filter(user=request.user).first()
    requests = Zayavka.objects.filter(courier=couriers)
    clients = Zayavka.objects.filter(user=request.user)

    
    

    

    return render(request, 'courier.html', {'form': form , 'requests': requests, 'clients': clients})




def updateStatusRequest(request, pk):
    rObj = Zayavka.objects.get(id=pk)
    rObj.statuc = request.POST.get('statuc')
    rObj.save()
    print("4")
    return redirect('myapps')
