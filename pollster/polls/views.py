from django.http.response import Http404
from django.shortcuts import render
from .models import Question, Choice

# Create your views here.


# Get questions and display them
def index(request):

    # Getting latest 5 questions, ordering in descending order according to pub_date
    latest_question_list = Question.objects.order_by("-pub_date")[:5]

    # Storing the questions in a dictionary
    context = {"latest_question_list": latest_question_list}

    # rendering index templating and passing the data to template
    return render(request, "polls/index.html", context)


# Show specific question and choices
def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question doesn't exist")

    return render(request, "polls/results.html", {"question": question})

