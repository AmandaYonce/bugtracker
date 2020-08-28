from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView
from .models import *
from .forms import CustomUserCreationForm, CreateTicketForm
from django.shortcuts import render, HttpResponseRedirect, reverse


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'


def Home(request):
    new = Tickets.objects.filter(status="New")
    progress = Tickets.objects.filter(status="In Progress")
    done = Tickets.objects.filter(status="Done")
    invalid = Tickets.objects.filter(status="Invalid")
    return render(request, 'home.html', {"new": new, "progress": progress, "done": done, "invalid": invalid})


def NewTicket(request):
    if request.method == "POST":
        form = CreateTicketForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Tickets.objects.create(
                title=data.get('title'),
                filer=request.user.username,
                description=data.get('description'),
                status='new',
                assignee=None,
                completer=None
            )
            return HttpResponseRedirect(reverse('home'))
    form = CreateTicketForm()
    return render(request, "newticket.html", {'form': form})


def EditTicket(UpdateView):
    model = Tickets
    fields = ['title', 'description', 'status', 'assignee', 'completer']
    template_name_suffix = '_update_form'
    return HttpResponseRedirect(reverse('home'))


def TicketDetail(request, ticket_id):
    ticket = Tickets.objects.filter(id=ticket_id).first()
    return render(request, 'ticketdetail.html', {"ticket": ticket})


def UserTickets(request, user_id):
    filed = Tickets.objects.filter(filer=user_id)
    assigned = Tickets.objects.filter(assignee=user_id)
    completer = Tickets.objects.filter(completer=user_id)
    return render(request, 'usertickets.html', {'filed': filed, 'assigned':assigned, "completer":completer})