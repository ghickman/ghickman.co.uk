---
date: 2013-06-20T00:00:00+00:00
draft: false
title: "Inspect's Hidden Gem: classify_class_attrs"
tags:
 - Python
aliases:
 - /2013/06/20/classify-class-attrs
---
Inspect provides a wealth of functionality for inspecting code, however one of it's most useful features is undocumented. Say hello to `classify_class_attrs`.

`classify_class_attrs` takes a class and returns a list of Attribute objects, each containing useful information about a member of the class. An Attribute object looks something like this:

```python
Attribute(name='bar', kind='method', defining_class=<class 'path.to.Foo'>, object=<function bar at 0x10b1b4e60>)
```

This output gives you a lot of useful information to work with and does the useful thing of returning objects instead of their repr.

It does have it's drawbacks, namely it doesn't give you methods called up the MRO tree by super but this can be worked around with some MRO walking and use of `filter`.
