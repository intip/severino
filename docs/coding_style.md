# Coding Style

## PEP 8

PEP 8 is the official style guide for Python. We advise reading it in detail and learn to follow the
PEP 8 coding conventions: http://www.python.org/dev/peps/pep-0008/
PEP 8 describes coding conventions such as:

+ “Use 4 spaces per indentation level.”
+ “Separate top-level function and class de nitions with two blank lines.”
+ “Method de nitions inside a class are separated by a single blank line.”
       
All the Python les in your Django projects should follow PEP 8. If you have trouble remembering
the PEP 8 guidelines, nd a plugin for your code editor that checks your code as you type.

When an experienced Python developer sees gross violations of PEP 8 in a Django project, even if
they don’t say something mean, they are probably thinking bad things. Trust us on this one.

## The Word on Imports

PEP 8 suggests that imports should be grouped in the following order:

1. Standard library imports
2. Related third-party imports
3. Local application or library speci c imports

``
Example 1

# Stdlib imports
from math import sqrt
from os.path import abspath

# Core Django imports
from django.db import models

from django.utils.translation import ugettext_lazy as _

# Third-party app imports
from django_extensions.db.models import TimeStampedModel

# Imports from your apps
from splits.models import BananaSplit

``

Note: you don’t actually need to comment your imports like this; the comments are just here to
explain the example.)

The import order here is:

1. Standard library imports.

2. Imports from core Django.

3. Imports from third-party apps.

4. Imports from the apps that you created as part of your Django project. (You’ll read more about apps in chapter 4, Fundamentals of App Design.)


## Use Explicit Relative Imports

When writing code, it’s important to do so in such a way that it’s easier to move, rename, and version
your work. In Python, explicit relative imports remove the need for hardcoding a module’s package,
separating individual modules from being tightly coupled to the architecture around them. Since
Django apps are simply Python packages, the same rules apply.

To illustrate the bene ts of explicit relative imports, let’s explore an example.

Imagine that the following snippet is from a Django project that you created to track your ice cream
consumption, including all of the waffle/sugar/cake cones that you have ever eaten.


``
Example 1.2

# cones/views.py

from django.views.generic import CreateView

# Relative imports of the 'cones' package
from .models import WaffleCone
from .forms import WaffleConeForm
from core.views import FoodMixin

class WaffleConeCreateView(FoodMixin, CreateView):
    model = WaffleCone
    form_class = WaffleConeForm
``
