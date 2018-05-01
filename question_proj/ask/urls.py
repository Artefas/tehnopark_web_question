from django.conf.urls import url

from .views import new_question, question_detail, questions_list
from .views import registration
from .views import login_to_site, logout_from_site

urlpatterns = [
    url('questions$', questions_list, name='questions-list'),
    url('questions/(?P<pk>[\d]+)$', question_detail,  name='question-detail'),
    url('questions/new$', new_question,  name='new-question'),
    url('registration$', registration, name='registration' ),
    url('login$', login_to_site, name='login'),
    url('logout$', logout_from_site, name='logout'),
]