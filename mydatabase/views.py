from django.shortcuts import render, redirect
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy
from mydatabase.models import EmailObject
from mydatabase.forms import EmailForm, SendForm
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
# Create your views here.

@login_required(login_url='home:homepage')
def index(request):
    mydb = EmailObject.objects.filter(user=request.user)
    return render(request, 'mydatabase/index.html', {'mydb': mydb})

@login_required(login_url='home:homepage')
def detail(request,pk):
    mydb = EmailObject.objects.get(pk=pk)
    sendform = SendForm()
    if request.method == 'POST':
        title = request.POST['title']
        body = request.POST['body']
        fromemail = request.POST['fromemail']
        toemail = request.POST['toemail']
        yourpassword = request.POST['yourpassword']
        send_mail(title,body,fromemail,[toemail],auth_password=yourpassword)
        return redirect('mydatabase:mydb_detail', pk=pk)
    return render(request, 'mydatabase/detail.html', {'mydb': mydb, 'form' : sendform})

@login_required(login_url='home:homepage')
def list_email(request):
    result = EmailObject.objects.filter(change=True,user=request.user)
    return render(request, 'mydatabase/listemail.html', {'result': result})

@login_required(login_url='home:homepage')
def add_new_email(request):
    form = EmailForm()
    return render(request, 'mydatabase/newdb.html', {'form': form})

@login_required(login_url='home:homepage')
def update_change(request, pk):
    EmailObject.objects.filter(pk=pk).update(change=True,user=request.user)
    return redirect('mydatabase:mydb_index')

@login_required(login_url='home:homepage')
def delete_change(request,pk):
    EmailObject.objects.filter(pk=pk).update(change=False,user=request.user)
    return redirect('mydatabase:email_list')

@login_required(login_url='home:homepage')
def add_new_email_post(request):
    if request.method == 'POST':
        emailform = EmailForm(request.POST)
        if emailform.is_valid():
            name = request.POST['name']
            description = request.POST['description']
            email = request.POST['email']
            newemail = EmailObject(user=request.user, name=name, description=description, email=email)
            newemail.save()
            return redirect('mydatabase:mydb_index')


class EmailDelete(DeleteView):
    model = EmailObject
    success_url = reverse_lazy('mydatabase:mydb_index')
