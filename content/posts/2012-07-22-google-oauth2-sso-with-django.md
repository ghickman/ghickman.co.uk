---
date: 2012-07-22T00:00:00+00:00
draft: false
title: Setup Single Sign On in Django using Google OAuth2
tags:
 - Django
 - Python
aliases:
 - /2012/07/22/google-oauth2-sso-with-django
---
We recently had our second Incuna Hack Day where [Charlie](https://github.com/meshy) and I made the decision to start breaking up the main internal site, our venerable Dashboard. It was well on its way to becoming a monolithic beast and the only thing that had stopped me breaking it up before was an easy way to add Single Sign On to the many apps it would become.

Enter [Django Social Auth](https://django-social-auth.readthedocs.org/en/latest/index.html). A cover-all-the-bases authentication app that provides backends for pretty much every service you can think of.

This write-up is based on my experience setting up a few internal apps so it's fairly opinionated towards that goal, but hopefully it's still adaptable to other situations!

## Setup your App in Google's API Console
In Google's [API Console](https://code.google.com/apis/console) create a new project.

![Create Project](https://f.cl.ly/items/1i353P2Q162K3G440o0R/Screen%20Shot%202012-07-15%20at%2021.11.02.png)

You don't need to turn on any extra services, so go directly to `API Access` and hit the giant blue button to get started.

![Create OAuth 2.0 Client ID](https://f.cl.ly/items/323j183V3n0j0s1H1A2p/Screen%20Shot%202012-07-15%20at%2021.12.26.png)

Enter your Product name and the URL to a logo if you have one. These are the details users will see when they authenticate via Google. Click `Next`.

Now set up the credentials for your application (this is per environment due to the redirect URI). The example below is for development, but only the hostname needs to change between environments.

![Enter Local Hostname](https://f.cl.ly/items/3f2M0e0r0z3D120X1f2z/Screen%20Shot%202012-07-15%20at%2021.16.47.png)

Click `more options` to set the callback path. The default Social Auth URL for this is `/complete/google-oauth2/`.

![Enter your redirect URI](https://f.cl.ly/items/3q2P0j173i2Q000r3i24/Screen%20Shot%202012-07-15%20at%2021.21.40.png)

Click `Create client id` and grab your `Client ID`/`Client secret` combo for the next step.


## Setup Django Social Auth
Add `social_auth` to your `INSTALLED_APPS` and the other settings below:

```python
AUTHENTICATION_BACKENDS = (
    'social_auth.backends.google.GoogleOAuth2Backend',
    'django.contrib.auth.backends.ModelBackend',
)
LOGIN_REDIRECT_URL = '/'

GOOGLE_OAUTH2_CLIENT_ID = os.environ['GOOGLE_OAUTH2_CLIENT_ID']
GOOGLE_OAUTH2_CLIENT_SECRET = os.environ['GOOGLE_OAUTH2_CLIENT_SECRET']
GOOGLE_WHITE_LISTED_DOMAINS = ['incuna.com']
SOCIAL_AUTH_USER_MODEL = 'auth.User'
```

Here I whitelist our Google Apps domain to only allow authentication by users from work email addresses and tell Social Auth to use the `auth.User` model when creating new users which it will do by default (I believe you can turn this off with another setting). This lets met forget about registration completely which is perfect for internal applications.

Make sure you've set `GOOGLE_OAUTH2_CLIENT_ID` and `GOOGLE_OAUTH2_CLIENT_SECRET` in your environment when you do `runserver` or you'll get the crappy settings error message `Unknown command: 'runserver'`. You can avoid this using `.get()` instead of square braces notation when getting the Google credentials however the error may be more archaic. I'm currently favouring square braces notation and getting used to fixing my environment!



## Create Some Basic Views

```python
from django.core.urlresolvers import reverse
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic.base import View
from social_auth.backends.exceptions import AuthFailed
from social_auth.views import complete



class AuthComplete(View):
    def get(self, request, *args, **kwargs):
        backend = kwargs.pop('backend')
        try:
            return complete(request, backend, *args, **kwargs)
        except AuthFailed:
            messages.error(request, "Your Google Apps domain isn't authorized for this app")
            return HttpResponseRedirect(reverse('login'))


class LoginError(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse(status=401)
```

Social Auth requires you add a view for when login fails. So far this hasn't been an issue for me so I've done the pure basics here with `LoginError`.

The second view was to cope with the whitelisting of domains which, pleasingly, raises an `AuthFailed` exception when you try to authenticate with a domain not in the whitelist.

Now all we need is to plumb this in with some URLs:

```python
from django.conf.urls import *
from django.contrib import admin

from .views import AuthComplete, LoginError


admin.autodiscover()

urlpatterns = patterns('',
    # some other urls

    url(r'^admin/', include(admin.site.urls)),
    url(r'^complete/(?P<backend>[^/]+)/$', AuthComplete.as_view()),
    url(r'^login-error/$', LoginError.as_view()),
    url(r'', include('social_auth.urls')),
)
```


## Profit
I usually put `login_required` on the whole site with a little piece of middleware (like [this](https://djangosnippets.org/snippets/1179/) or [this](https://djangosnippets.org/snippets/1220/)) but otherwise that's it!

