from django.shortcuts import render, redirect
from bboard.models import Bboard
from .models import Account
from django.contrib.auth.decorators import login_required
from .forms import RegistrationForm, PostForm
from django.views.generic.edit import FormView, CreateView
from django.urls import reverse_lazy


def index(request, pk):
    posts = Bboard.objects.filter(author_id=pk)
    acc = Account.objects.filter(id=pk)
    context = {'posts': posts, 'acc': acc}
    return render(request, 'account/account.html', context)


@login_required
def auth(request):
    acc = Account.objects.filter(id=request.user.id)
    posts = Bboard.objects.filter(author_id=request.user.id)
    data = {'posts': posts, "acc": acc}
    return render(request, "account/myacc.html", data)


class RegistrationView(FormView):
    form_class = RegistrationForm
    template_name = 'registration/reg.html'
    success_url = reverse_lazy('myacc')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class Newpost(CreateView):
    model = Bboard
    form_class = PostForm
    template_name = 'account/newpost.html'
    success_url = reverse_lazy('myacc')

    def form_valid(self, form):
        advertisement = form.save(commit=False)
        advertisement.author = Account.objects.get(username=self.request.user)
        advertisement.save()
        return redirect('myacc')