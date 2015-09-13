Title: Adding Django Inline Forms with Javascript
Status: published
Tags: Django, Javascript, Python

Using Django formsets on a new section for a project at work I came across something I haven't considered before: adding new inline forms to a formset without reloading the page. Javascript was the obvious choice. Two pages required the functionality: one with six formsets, the other with one, which meant the solution needed to take into account formset prefixes. I found various solutions around the Internet, but all were outdated (lots of table based layouts!) or not generic enough (didn't deal with multiple formsets).

The idea behind the script is pretty simple: duplicate an existing form then update the form counter.

[gist:id=1020463,file=add_inline.js]

Which is setup to work on html that looks like this:

_Note: I'm using [Django UniForm][1] to output the form in `<div>'s`_

[gist:id=1020463,file=forms.html]

### So How Does it Work?
_Skip to [Gotchas][2] if you already understand my javascript_

I start by looping my form class `add-inline` (you can call it anything you like) and then running the regular expression from line 20 to find the form prefix, which is another class on the form. It expects the classes applied to the form in the order `add-inline <formset prefix> add/existing`. The add/existing bit on the end isn't necessary but gives you an example of where to put any other classes that might exist on your form. If you don't want to use it, just remember to remove it from the regex! Inside the `add_inline_form` function I'm grabbing the count from the hidden div and the last form with jQuery's `:last` selector.

When new_form is set I'm using jQuery's [clone][3] method to take a copy of the last form and grab the raw html. The false passed into clone tells it to ignore any triggers and binds. The regex sets the correct count in the element ids. The next line clears the contents of every element in the new form since clone will pull this in with the elements. The new form is hidden then added after the last form with a nice little bit of [slideDown][4] candy for some UI goodness.

Finally increment the form count and return false so the form isn't submitted.

<h2 id="gotchas">Gotchas</h2>
So now you've got your nice little bit of javascript (if I don't say so myself) all setup to grab the last form in each formset, duplicate it and add it below the last form. However there are some caveats to this...

The script grabs the last form in the formset _every_ time so say you want the first form to differ from the rest (as I did) and implement this in the templates then you'll get the non-standard first form duplicated each time. The easiest way around this is to check the count and add an if to look for the first form.

[1]: https://github.com/pydanny/django-uni-form
[2]: #gotchas
[3]: http://api.jquery.com/clone/
[4]: http://api.jquery.com/slideDown/

