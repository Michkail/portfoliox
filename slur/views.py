from django.shortcuts import render
from .forms import ContactForm
from django.core.mail import message, send_mail, BadHeaderError
from django.http import HttpResponse

def homey(request):
  return render(request, 'homey.html')

def contactly(request):
  """
  if request.method == 'POST':
    form = ContactForm(request.POST)
    if form.is_valid():
      subject = "cuma ttttttest"
      body = {
        'first_name': form.cleaned_data['first_name'],
        'last_name': form.cleaned_data['last_name'],
        'email': form.cleaned_data['email_address'],
        'message': form.cleaned_data['message']
      }
      message = "\n".join(body.values())
      try:
        send_mail(subject, message, 'test@example.com', ['example@test.com'])
      except BadHeaderError:
        return HttpResponse('Invalid header found.')
      return redirect ("main:homey")
  form = ContactForm()
  """
  return render(request, 'contact.html')#, {'form': form})

def aboutly(request):
  return render(request, 'about.html')