from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home, name="home"),
    path('newticket/', views.NewTicket),
    path('editticket/', views.EditTicket),
    path('ticketdetail/<int:ticket_id>/', views.TicketDetail),
    path('usertickets/<int:user_id>/', views.UserTickets),
    path('changestatus/<int:ticket_id>/', views.ChangeStatus),
    path('changeassigned/<int:ticket_id>/', views.ChangeAssigned)
]