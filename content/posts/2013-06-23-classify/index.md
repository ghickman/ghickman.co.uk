---
date: 2013-06-23T00:00:00+00:00
draft: false
title: "Classify: Python API Reference Tool"
tags:
 - Python
aliases:
 - /2013/06/23/classify
---
Not too long ago some colleagues of mine created ccbv.co.uk, a documentation tool for Django's Class Based Views. CCBV differs from Django's usual documentation by being providing users with an API reference to the members of each Class, including any inherited ones. This is especially useful when you need to see what code you're overriding or calling when working in a subclass.

My one concern with CCBV has always been how spoilt it makes me when working with Django CBVs. Even within Django's own code base there are other areas with complex Class inheritance that I'd like to generate a reference doc for. So, as any good programmer does, [I built one](https://pypi.python.org/pypi/classify).

Classify takes a python path and outputs the generated class, defaulting to the terminal and your shells's pager. However it will also generate an HTML file (using the ccbv.co.uk layout) with the `--html` option and even serve it with `--serve`.

Thanks to [Charlie Denton](https://meshy.co.uk/) (meshy) for jokingly suggesting I google pydoc which, apart from already existing, ended up being the basis for much of Classify's internals.

EDIT: Here's some example output from running `classify django.views.generic.UpdateView`

![classify django.views.generic.UpdateView](./classify.png "classify django.views.generic.UpdateView")
