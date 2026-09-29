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

```python
from django.template.defaultfilters import slugify

@classmethod
def generate_slug(self, name):
    count = 1
    slug = slugify(name)

    def _get_query(slug):
        if MyModel.objects.filter(slug=slug).count():
            return True

    while _get_query(slug):
        slug = slugify(u'{0}-{1}'.format(name, count))
        # make sure the slug is not too long
        while len(slug) > MyModel._meta.get_field('slug').max_length:
            name = name[:-1]
            slug = slugify(u'{0}-{1}'.format(name, count))
        count = count + 1
    return slug
```

*example usage*: `MyModel.objects.create(name='foo', slug=MyModel.generate_slug('foo'))`


## Generic

```python
from django.template.defaultfilters import slugify

def generate_slug(cls, value):
    count = 1
    slug = slugify(value)
    if not isinstance(cls, type):
        cls = cls.__class__

    def _get_query(cls, **kwargs):
        if cls.objects.filter(**kwargs).count():
            return True

    while _get_query(cls, slug=slug):
        slug = slugify(u'{0}-{1}'.format(value, count))
        # make sure the slug is not too long
        while len(slug) > cls._meta.get_field('slug').max_length:
            value = value[:-1]
            slug = slugify(u'{0}-{1}'.format(value, count))
        count = count + 1
    return slug
```

*example usage*: `AnotherModel.objects.create(name='bar', slug=generate_slug(AnotherModel, 'foo'))`

