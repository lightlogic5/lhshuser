from django.shortcuts import render
from django.views.generic.base import View
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.backends import ModelBackend
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.db.models import Q

from .forms import LoginForm
from .models import UserProfile
# Create your views here.
from .models import Employee
from .forms import UserForm


class CustomBackend(ModelBackend):
    def authenticate(self,request, username=None, password=None, **kwargs):
        try:
            user = UserProfile.objects.get(Q(employee_id=username),Q(password=password))
            # if user.check_password(password):
            return user
        except Exception as e:
            return None


class LogoutView(View):
    """
    用户登出
    """
    def get(self, request):
        logout(request)
        return HttpResponseRedirect(reverse("index"))

class LoginView(View):
    def get(self, request):
        return render(request, "login.html", {})
    def post(self, request):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            user_name = request.POST.get("username", "")
            pass_word = request.POST.get("password", "")
            user = authenticate(username=user_name, password=pass_word)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect(reverse("index"))
                else:
                    return render(request, "login.html", {"msg":"用户未激活！"})
            else:
                return render(request, "login.html", {"msg":"用户名或密码错误！"})
        else:
            return render(request, "login.html", {"login_form":login_form})


# 用户信息维护
class UserView(View):
    def get(self, request):
        # 用户信息onetoone有错
        default_data = {'user': user.username,}
        form = UserForm(default_data)

        return render(request, "employee.html", default_data)

    def post(self, request):
        user_form = UserForm(request.POST)
        if user_form.is_valid():
            # print_form.cleaned_data['pub_date'] = timezone.now()
            # pub_date = timezone.now()
            print(user_form.cleaned_data)
            print_form1 = user_form.save(commit=False)
            print_form1.user = request.user
            print_form1.save()
            return HttpResponse('{"status":"success"}', content_type='application/json')
        else:
            return HttpResponse('{"status":"fail", "msg":"添加出错"}', content_type='application/json')