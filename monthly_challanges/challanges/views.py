from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from google import genai
from django.urls import reverse
monthly_challenges = {
    "january": "Start the year with a 30-day meditation challenge to improve focus and reduce stress.",
    "february": "Take on a 28-day fitness challenge focusing on cardio and strength training.",
    "march": "Challenge yourself to learn a new skill or hobby for 31 days.",
    "april": "Commit to a 30-day healthy eating challenge with meal planning and preparation.",
    "may": "Take on a 31-day reading challenge to expand your knowledge.",
    "june": "Challenge yourself to a 30-day outdoor activity challenge.",
    "july": "Commit to a 31-day gratitude journaling challenge.",
    "august": "Take on a 31-day digital detox challenge to reduce screen time.",
    "september": "Challenge yourself to a 30-day creative writing challenge.",
    "october": "Commit to a 31-day mindfulness and self-care challenge.",
    "november": "Take on a 30-day random acts of kindness challenge.",
    "december": "Challenge yourself to a 31-day reflection and goal-setting challenge for the new year."
}

def home(request):
    my_month_list = list(monthly_challenges.keys())
    my_link_list = list()
    count = 0
    for i in my_month_list:
        count = count + 1
        path = reverse("num",args=[i])
        capitilized = i.capitalize()
        my_link_list.append(f"<a href=\"{path}\"><h1>{count}: {capitilized}</h1></a>")
    return HttpResponse(my_link_list)



def index_num(request, month):
    month = month % 12
    if month == 0:
        month = 12
    my_month_list = list(monthly_challenges.keys())
    path = reverse("num",args=my_month_list[month-1])
    return HttpResponseRedirect(path)

def index(request, month):
    return HttpResponse(monthly_challenges[month])        
# Create your views here.

def realHome(request):
    return HttpResponse("<h1>Welcome: <a href=\"challanges\">Challanges</a></h1>")

