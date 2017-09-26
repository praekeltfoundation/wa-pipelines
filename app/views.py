from django.conf import settings
from django.contrib import messages
from django.contrib.auth import logout as django_logout
from django.shortcuts import render, redirect
from django.views.generic import TemplateView


def login(request):  # pragma: nocover
    return render(request, 'login.html')


def logout(request):  # pragma: nocover
    django_logout(request)
    messages.info(
        request,
        'You have logged out. '
        'You will need to log in again to continue using Pipelines')
    return redirect(settings.LOGIN_REDIRECT_URL)


def login_error(request):  # pragma: nocover
    messages.error(
        request, 'Unable to log you in, domain restrictions in place.')
    return redirect(settings.LOGIN_REDIRECT_URL)


class ProfileView(TemplateView):

    template_name = 'profile.html'

    def get_context_data(self, *args, **kwargs):
        context = super(ProfileView, self).get_context_data(*args, **kwargs)
        context['user'] = self.request.user
        return context
