from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic import (
    ListView,
    DetailView,
    FormView,
)
from django.views.generic.detail import SingleObjectMixin
from main.models import Choice,Question,Answer
from main.forms import AnswerForm

# Create your views here.
class Index(ListView):
    model = Question
    template_name = 'main/index.html'

class Question(PermissionRequiredMixin ,SingleObjectMixin, FormView):
    model = Question
    template_name = 'main/question.html'
    form_class = AnswerForm
    permission_required = 'add_answer'
    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['answer'] = Answer.objects.get(
            question = self.get_object(),
            user = self.request.user
        )
        return data

    def form_valid(self,form):
        obj = form.save(commit=False)
        obj.question = self.get_object() 
        obj.user = self.request.user
        obj.save()
        return HttpResponseRedirect('/')

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().post(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        context = self.get_context_data(object = self.object)
        return self.render_to_response(context)