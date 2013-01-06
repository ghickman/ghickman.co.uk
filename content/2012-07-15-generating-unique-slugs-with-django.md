Title: Generating unique slugs with Django
Tags: Django

This is something I've come across a couple of times over the last few months and each time ended up acking through various projects so putting this up here to save myself the pain next time!

There are two versions to this method - model specific and a more generic one intended for a `utils` module if you're going to use it on more than one model.

Neither of these methods is built to scale, but since I've never worked at scale this hasn't been an issue. However you've been warned!

The functions make the slug unique by appending a count to the end and checking the length is still valid for the slug field.

## Model Specific

{{ 3116929 | gist: 'specific.py' }}

*example usage*: `MyModel.objects.create(name='foo', slug=MyModel.generate_slug('foo'))`


## Generic

{{ 3116929 | gist: 'generic.py' }}

*example usage*: `AnotherModel.objects.create(name='bar', slug=generate_slug(AnotherModel, 'foo'))`

