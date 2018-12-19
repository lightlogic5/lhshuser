from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from django.http import Http404
from django.views.generic.base import View
from django.utils import timezone

from pure_pagination import Paginator, EmptyPage, PageNotAnInteger

from .models import PrintForm
from .forms import MyPrintForm


def index(request):
    # return HttpResponse("Hello, world. You're at the polls index.")
    latest_question_list = PrintForm.objects.order_by('-pub_date')[:4]
    # output = ', '.join([q.content for q in latest_question_list])
    # return HttpResponse(output)
    template = loader.get_template('printform/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    # return HttpResponse(template.render(context, request))
    return render(request, 'printform/index.html', context)


def detail(request, question_id):
    # return HttpResponse("You're looking at question %s." % question_id)
    try:
        question = PrintForm.objects.get(pk=question_id)
    except PrintForm.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'printform/detail.html', {'question': question})


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)


class FormView(View):
    def get(self, request):
        return render(request, "printform/uploadform.html", {})

    def post(self, request):
        print_form = MyPrintForm(request.POST)
        if print_form.is_valid():
            # print_form.cleaned_data['pub_date'] = timezone.now()
            # pub_date = timezone.now()
            print(print_form.cleaned_data)
            print_form1 = print_form.save(commit=False)
            print_form1.pub_date = timezone.now()
            print_form1.save()
            return HttpResponse('{"status":"success"}', content_type='application/json')
        else:
            return HttpResponse('{"status":"fail", "msg":"添加出错"}', content_type='application/json')
            # repair_man = request.POST.get("repair_man", "")
            # unit = request.POST.get("unit", "")
            # content = request.POST.get("content", "")
            # telephone = request.POST.get("telephone", "")

class FormListView(View):
    def get(self, request):
        all_forms = PrintForm.objects.all().order_by("-id")
        # 搜索框

        search_keywords = request.GET.get('keywords', "")
        if search_keywords:
            all_forms = all_forms.filter(repair_man__icontains=search_keywords)

        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
        p = Paginator(all_forms, 10,  request=request)

        all_forms1 = p.page(page)
        # print(all_forms)

        return render(request, 'printform/showforms.html', {
            "all_forms": all_forms1
        })
