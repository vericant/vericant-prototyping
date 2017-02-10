from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import HttpResponseRedirect, redirect


class BookingShellView():
    template_name = 'design/booking/scheduler.html'
    # title = _('Vericant Scheduling System')

    def dispatch(self, *args, **kwargs):
        resp = super(BookingShellView, self).dispatch(*args, **kwargs)
        return resp

booking_shell = BookingShellView.as_view()
