from http.client import HTTPResponse
from django.shortcuts import render
# Create your views here.


def function (request):
    return HTTPResponse("hey")