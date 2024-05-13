---
date: 2012-07-15T00:00:00+00:00
draft: false
title: Generating unique slugs with Django
tags:
 - Django
aliases:
 - /2012/07/15/generating-unique-slugs-with-django
---
This is something I've come across a couple of times over the last few months and each time ended up acking through various projects so putting this up here to save myself the pain next time!

There are two versions to this method - model specific and a more generic one intended for a `utils` module if you're going to use it on more than one model.

Neither of these methods is built to scale, but since I've never worked at scale this hasn't been an issue. However you've been warned!

The functions make the slug unique by appending a count to the end and checking the length is still valid for the slug field.

## Model Specific

{{< gist ghickman 3116929 "specific.py" >}}

*example usage*: `MyModel.objects.create(name='foo', slug=MyModel.generate_slug('foo'))`


## Generic

{{< gist ghickman 3116929 "generic.py" >}}

*example usage*: `AnotherModel.objects.create(name='bar', slug=generate_slug(AnotherModel, 'foo'))`

