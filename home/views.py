from django.shortcuts import render,redirect
from .forms import BookForms,SearchForm
from home.models import Book,Author,Genre
from django.utils import timezone
from django.contrib import messages

# Create your views here.


'''def newform_view(request):
    form=BookForms()
    #book=Book.objects.all()
    context={
        "head":'Custom form created here using Python',
        "forms": form,
        #"books":book
    }
    return render(request,'forms.html',context)'''

def form_view(request):

   msg=' '

   if request.method=='POST':
      form=BookForms(request.POST)
      if form.is_valid():
         book=Book(
            name= form.cleaned_data.get('name'),
            purchase_date=form.cleaned_data.get('purchase_date'),
            genre=form.cleaned_data.get('genre'),
            author=form.cleaned_data.get('author')
         )
         book.save()
         msg='Book Added Successfully!'
      else:
         msg=form.errors
   else:
      form=BookForms()
   return render(request,'forms.html',{"msg":msg, "forms": form})

def html_form(request):
   if request.method=='POST':
      value=request.POST.get('name')
      return render(request,'values.html',{'value':value})
   else:
      return render(request,'login.html')
def booksearch(request):
   if request.method=='POST':
      form=SearchForm(request.POST)
      if form.is_valid():
         q=form.cleaned_data.get('q')
         book=Book.objects.filter(name__contains=q)
         #book=Book.objects.filter(name__contains=q,purchase_date__lte=timezone.now)

         #form=None
         return render(request,'showtables.html',{'book':book,'form':SearchForm()})
   else:
      form=SearchForm()
      book=Book.objects.all()
   return render(request,'showtables.html',{ 'book':book,'form':form})

def deletebook(request,id):
   book=Book.objects.get(id=id)
   book.delete()
   messages.success(request,'Deleted'+str(id)+' Successfully!!')
   return redirect('/')

def editbook(request):
   book=Book.objects.get(id=id)
   if request.method=='POST':
      form=BookForms(request.POST)
      if form.is_valid():
         form.save()
         messages.success(request,'Book Updated Successfully!!')
         return redirect('/')
   else:
         form=BookForms(instance=book)
   return render(request,'editbook.html',{'form':form})
