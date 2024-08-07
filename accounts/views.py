from django.contrib.auth.decorators import login_required
from django.contrib.auth import login as auth_login
from django.contrib.auth import get_user_model
from django.contrib.auth.views import LoginView
from django.urls import reverse
from django.template.response import TemplateResponse
from django.http import HttpRequest, HttpResponse
from django.utils.html import format_html
from django.views.decorators.http import require_http_methods
from django_htmx.http import HttpResponseClientRedirect
from django.contrib.auth import authenticate

from .forms import UserRegisterForm

User_model = get_user_model()


class LoginCustomView(LoginView):
    template_name = "registration/login.html"
    redirect_authenticated_user = True

    def post(self, request, *args, **kwargs):

        form = self.get_form()
        if form.is_valid():
            authenticate(
                request, username=form.cleaned_data["username"], password=form.cleaned_data["password"]
            )
            return self.form_valid(form)

        return self.form_invalid(form)

    def form_valid(self, form):
        auth_login(self.request, form.get_user())
        return HttpResponseClientRedirect(reverse("list_users"))


@require_http_methods(["GET", "POST"])
def register(request: HttpRequest) -> HttpResponse:
    if request.method == "GET":
        return TemplateResponse(
            request, "registration/register.html", {"form": UserRegisterForm()}
        )

    if (form := UserRegisterForm(request.POST)).is_valid():
        user = form.save()
        auth_login(request, user)
        return HttpResponseClientRedirect(reverse("list_users"))

    return TemplateResponse(request, "registration/_register.html", {"form": form})


@require_http_methods(["GET"])
@login_required
def list_users(request: HttpRequest) -> HttpResponse:
    return TemplateResponse(
        request=request,
        template="accounts/list_users.html",
        context={"users": User_model.objects.filter(is_active=True, is_superuser=False)},
    )


@require_http_methods(["GET"])
def check_email(request: HttpRequest) -> HttpResponse:
    if (email := request.GET.get("email")) and User_model.objects.filter(
            email__iexact=email
    ).exists():
        return HttpResponse(
            format_html(
                """<ul class="error-messages"><li>This email is in use.</li></ul>"""
            )
        )
    return HttpResponse()

