# -*- coding:utf-8 -*-

# Stdlib imports

# Core Django imports
from django.shortcuts import render_to_response
from django.template import RequestContext

# Third-party app imports

# Imports from your apps


def hello(request):
    """
    Doc string
    """

    return render_to_response(
        'hello.html',
        context_instance=RequestContext(request)
    )
