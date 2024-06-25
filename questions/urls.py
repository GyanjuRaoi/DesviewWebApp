from django.urls import path
from .views import (

    CreateQuestion,
    QuestionList,
    UpdateQuestion,
    DeleteQuestion,
    CreateAnswer,
    comments,
)

urlpatterns = [
    path('list/', QuestionList.as_view(), name='question-list'),
    path('create/', CreateQuestion.as_view(), name='question-create'),
    path('<int:pk>/update/', UpdateQuestion.as_view(), name='question-update'),
    path('<int:pk>/delete/', DeleteQuestion.as_view(), name='question-delete'),
    path('<int:question_id>/answer/', CreateAnswer.as_view(), name='answer-question'),
    path('<int:pk>/comment/', comments, name='comment-view'),
]