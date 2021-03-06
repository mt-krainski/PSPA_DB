from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from django.template import loader

from django.shortcuts import render
from django.shortcuts import get_object_or_404

from .models import Question
from .models import Member


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]

    # template = loader.get_template('display/index.html')
    # context = {
    #     'latest_question_list' : latest_question_list,
    # }
    # return HttpResponse(template.render(context, request))

    return render(
        request,
        'display/index.html',
        {'latest_question_list': latest_question_list}
    )


def details(request, question_id):
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404("Question does not exist")

    question = get_object_or_404(Question, pk=question_id)

    return render(
        request,
        'display/detail.html',
        {'question': question}
    )


def results(request, question_id):
    return HttpResponse(f"You're looking at the results for question {question_id}")


def vote(request, question_id):
    return HttpResponse(f"You're voting for question {question_id}")


def display_member(request, member_id):
    member = Member.objects.get(pk=member_id)

    return render(
        request,
        'display/member_display.html',
        {'member':member}
    )


def display_members_list(request):

    members = Member.objects.all()
    jobs = [member.jobdescription_set.all()[0].workplace_str for member in members]

    return render(
        request,
        'display/list_members.html',
        {
            'members': members,
            'jobs': jobs
        }
    )