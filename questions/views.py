from django.shortcuts import render,redirect
from users.forms import QuestionCreateForm
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    UserPassesTestMixin
)
from django.views.generic import (
    ListView,
    UpdateView,
    DeleteView,
    CreateView
)
from .models import Question, Comment
from django.contrib.auth.decorators import login_required

# Class Based View
class CreateQuestion(LoginRequiredMixin, CreateView):
    model = Question
    context_object_name = 'form'
    template_name = 'questions/question_create.html'

    fields = ['title', 'description', 'image']

    def form_valid(self, form):
        form.instance.user_id = self.request.user
        
        return super().form_valid(form)
    
class QuestionList(ListView):
    model = Question
    context_object_name = 'questions'

class UpdateQuestion(UpdateView):
    model = Question
    fields = ['title', 'description', 'image']

    def test_func(self):
        question = self.get_object()
        return self.request.user == question.user_id

    def get_initial(self):
        initial = super().get_initial()
        question = self.get_object()
        initial['title'] = question.title
        initial['description'] = question.description
        return initial

class DeleteQuestion(DeleteView):
    model = Question
    success_url = '/'

    def test_func(self):
        question = self.get_object()

        if self.request.user == question.user_id:
            return True
        return False


class CreateAnswer(LoginRequiredMixin,CreateView):
    model = Comment
    fields = ['content', 'image_comment']
    template_name = 'questions/question_answer.html'
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['question_id'] = self.kwargs['question_id']
        return context

    def form_valid(self, form):
        form.instance.question_id = self.kwargs['question_id']
        form.instance.user = self.request.user
        return super().form_valid(form)


# Function based view
def comments(request, pk):
    
    question = Question.objects.get(id=pk)
    question_answer = Comment.objects.all()

    answers = []

    for ans in question_answer:
        if question.id == ans.question.id:
            answers.append(ans)  

    print(answers)

    context = {
        'answers': answers,
        'question': question,
    }

    return render(request, 'questions/comment.html', context)



