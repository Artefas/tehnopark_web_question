from django.shortcuts import render



def questions_list(request):
    return render(request, 'index.html')

def question_detail(request, pk):
    return render(request)

def registration(request):
    return render(request)

def new_question(request):
    return render(request)

def login_to_site(request):
    return render(request)

def logout_from_site(request):
    return render(request)