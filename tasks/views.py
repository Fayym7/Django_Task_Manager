from django.shortcuts import render,  redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.http import HttpResponseRedirect
from tasks.models import Task, OAuthKey
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from .models import UserInvitation


def register_with_token(request, token):
    try:
        invitation = UserInvitation.objects.get(token=token, is_used=False)
    except UserInvitation.DoesNotExist:
        return render(request, 'invalid_token.html')  # Show an error page if the token is invalid

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.email = invitation.email
            user.save()
            invitation.is_used = True
            invitation.save()
            return redirect('login')  # Redirect to login page after registration
    else:
        form = UserCreationForm()

    return render(request, 'register_with_token.html', {'form': form, 'email': invitation.email})


class GenericTaskView(LoginRequiredMixin, ListView):
    template_name = "tasks.html"
    context_object_name = "tasks"
    paginate_by = 5

    def get_queryset(self):
        search_query = self.request.GET.get("search", "")
        tasks = Task.objects.filter(user=self.request.user, deleted=False)
        if search_query:
            tasks = tasks.filter(title__icontains=search_query)
        return tasks


class GenericTaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    fields = ['title', 'description']
    template_name = "task_create.html"
    success_url = reverse_lazy('task_list')  # Redirect to the task list view after creating a task

    def form_valid(self, form):
        form.instance.user = self.request.user  # Assign the logged-in user to the task
        return super().form_valid(form)

    def form_invalid(self, form):
        print(form.errors)  # Debugging: Print form errors if the form is invalid
        return self.render_to_response(self.get_context_data(form=form))


class GenericTaskUpdateView(LoginRequiredMixin, UpdateView):
    model = Task
    fields = ['title', 'description', 'completed']
    template_name = "task_update.html"
    success_url = reverse_lazy('task_list')  # Use the URL name for better flexibility

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user) 


class GenericTaskDeleteView(LoginRequiredMixin, DeleteView):
    model = Task
    template_name = "task_delete.html"
    success_url = reverse_lazy('task_list')  # Use URL name instead of hardcoding

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)  # Ensure only the task owner can delete



