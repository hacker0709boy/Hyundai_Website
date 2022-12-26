from django.shortcuts import render
from django.http import HttpResponse
from .models import *


from django.core.mail import send_mail
from django.conf import settings
# Create your views here.






###############################---  Main Page  ---################################################
def index(request):
	banner = MainPageBanner.objects.all()
	stocks = StockCars.objects.all()
	context = {'banner': banner, 'stocks':stocks}
	return render(request, 'index.html', context)
###############################---  About Page  ---################################################
def about(request):
	context = {}
	return render(request, 'about.html', context)
###############################---  Contact Page  ---################################################
def contact(request):
	if request.method == 'POST':
		name = request.POST.get('name')
		email = request.POST.get('email')
		subject = request.POST.get('subject')
		message = request.POST.get('message')
		print(f'Name:\t{name}\nE-mail:\t{email}\nSubject:\t{subject}\nMessage:\t{message}')

		data = {
			'name': name,
			'subject': subject,
			'email': email,
			'message': message
		}
		message = '''
		Name: {}

		Subject: {}

		New Message: {}

		From: {}
		'''.format(data['name'],data['subject'],data['message'], data['email'])

		send_mail(
			data['subject'], 
			message, 
			'', 
			['nury.jumanazarov@gmail.com'], 
			# fail_silently = False,
		)
	context = {}
	return render(request, 'contact.html', context)
###############################---  Models Page  ---################################################
def models(request):
	models = ModelsCars.objects.all()
	context = {'models':models}
	return render(request,'models.html', context)
###############################---  Service's Page  ---################################################
def service(request):
	context = {}
	return render(request, 'service.html', context)
###############################---  Auto in Stock Page  ---################################################
def stock(request):
	stocks = StockCars.objects.all()
	context = {'stocks': stocks}
	return render(request,'stock.html', context)
###############################---  Test Drive Page  ---################################################
def testdrive(request):
	if request.method == 'POST':
		name = request.POST.get('name')
		gmail = request.POST.get('gmail')
		types = request.POST.get('type')
		number = request.POST.get('number')
		message = request.POST.get('message')
		print(f'Name:\t{name}\nE-mail:\t{gmail}\nNumber:\t{number}\nTypes:\t{types}\nMessage:\t{message}')

		data = {
			'name': name,
			'type': types,
			'number': number,
			'gmail': gmail,
			'message': message
		}

		message = '''
		Name: {}

		Number: {}

		New Message: {}

		From: {}
		'''.format(data['name'],data['number'],data['message'], data['gmail'])

		send_mail(
			data['type'], 
			message, 
			'', 
			['nury.jumanazarov@gmail.com'], 
			# fail_silently = False,
		)
		context = {}
		return render(request, 'testdrive.html', context)

	else:
		context = {}
		return render(request, 'testdrive.html', context)





#########################################################################################################





###############################---  Main Page  ---################################################
def ru_index(request):
	banner = MainPageBanner.objects.all()
	stocks = StockCars.objects.all()
	context = {'banner': banner, 'stocks':stocks}
	return render(request, 'ru/index.html', context)
###############################---  About Page  ---################################################
def ru_about(request):
	context = {}
	return render(request, 'ru/about.html', context)
###############################---  Contact Page  ---################################################
def ru_contact(request):
	if request.method == 'POST':
		name = request.POST.get('name')
		email = request.POST.get('email')
		subject = request.POST.get('subject')
		message = request.POST.get('message')
		print(f'Name:\t{name}\nE-mail:\t{email}\nSubject:\t{subject}\nMessage:\t{message}')

		data = {
			'name': name,
			'subject': subject,
			'email': email,
			'message': message
		}
		message = '''
		Name: {}

		Subject: {}

		New Message: {}

		From: {}
		'''.format(data['name'],data['subject'],data['message'], data['email'])

		send_mail(
			data['subject'], 
			message, 
			'', 
			['nury.jumanazarov@gmail.com'], 
			# fail_silently = False,
		)
	context = {}
	return render(request, 'ru/contact.html', context)
###############################---  Models Page  ---################################################
def ru_models(request):
	models = ModelsCars.objects.all()
	context = {'models':models}
	return render(request,'ru/models.html', context)
###############################---  Service's Page  ---################################################
def ru_service(request):
	context = {}
	return render(request, 'ru/service.html', context)
###############################---  Auto in Stock Page  ---################################################
def ru_stock(request):
	stocks = StockCars.objects.all()
	context = {'stocks': stocks}
	return render(request,'ru/stock.html', context)
###############################---  Test Drive Page  ---################################################
def ru_testdrive(request):
	if request.method == 'POST':
		name = request.POST.get('name')
		gmail = request.POST.get('gmail')
		types = request.POST.get('type')
		number = request.POST.get('number')
		message = request.POST.get('message')
		print(f'Name:\t{name}\nE-mail:\t{gmail}\nNumber:\t{number}\nTypes:\t{types}\nMessage:\t{message}')

		data = {
			'name': name,
			'type': types,
			'number': number,
			'gmail': gmail,
			'message': message
		}

		message = '''
		Name: {}

		Number: {}

		New Message: {}

		From: {}
		'''.format(data['name'],data['number'],data['message'], data['gmail'])

		send_mail(
			data['type'], 
			message, 
			'', 
			['nury.jumanazarov@gmail.com'], 
			# fail_silently = False,
		)
		context = {}
		return render(request, 'ru/testdrive.html', context)

	else:
		context = {}
		return render(request, 'ru/testdrive.html', context)






