from django.shortcuts import render
from questions.models import Question


def home(request):
    user = request.user
    questions = Question.objects.all()

    context = {
        'user': user,
        'questions': questions,
    }

    return render(request, 'home/home.html', context)
