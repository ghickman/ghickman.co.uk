Title: Accessing Google APIs with an Offline Application
Tags: Python


Google distinguishes between applications that require user interaction and those that don't using the terminology of "online" and "offline" respectively. Offline applications cover things like scheduled jobs on a web application or command line scripts where the application is accessing Google's API with a user's consent but without their interaction.

## Set Up Your Application
Just like setting up an application to use [Google for SSO](http://ghickman.co.uk/2012/07/22/setup-single-sign-on-in-django-using-google-oauth2.html) you need to create an "API Application" using Google's [API Console](https://code.google.com/apis/console).

![Create a Project](http://f.cl.ly/items/1i353P2Q162K3G440o0R/Screen%20Shot%202012-07-15%20at%2021.11.02.png)

Unlike using Google for SSO you'll need to activate the service(s) you want to access with your application. In this post I'll be using the Calendar API as an example:

![Activate a Service](https://s3.amazonaws.com/f.cl.ly/items/2H2Z1m3M251c260j3l03/Image%202013.07.21%2011%3A37%3A03.png)

Now select "API Access" from the side menu:

![Select API Access Menu Item](https://s3.amazonaws.com/f.cl.ly/items/1F2W231F3u1e3b3T080l/Image%202013.07.21%2011%3A37%3A45.png)

Hit the big blue button get started:

![Big Blue Create an OAuth 2.0 Client ID](https://s3.amazonaws.com/f.cl.ly/items/372I35272l150m3s3B3f/Image%202013.07.21%2011%3A39%3A05.png)

Fill in the branding information with your Application's details. This information will be presented to users when asked to authorise your application with Google. On the next screen fill in your application's hostname, if your application doesn't have one (ie a CLI app) then just use something like `localhost`.

**Note:** If the Redirect URI is used by your application you'll need to create a set of credentials for each deployment of your application.

After clicking "Create client ID" you'll now have a Client ID and a Client Secret.


## Build the Consent URL
The second step in getting access to Google APIs is getting consent from a user. To do this you'll need to work out the scope of your access. Handily Google provides the required scope in their endpoint documentation, e.g. [retrieving a calendar](https://developers.google.com/google-apps/calendar/v3/reference/calendars/get#auth).

The consent URL can then be created using the correct options:

* `scope`: Whatever scope you decided on.
* `state`: An identifying string for your application.
* `redirect_uri`: URI Google will send the response to.
* `response_type`: Use `code`.
* `client_id`: Your Client ID from the API Console.
* `approval_prompt`: Use `force`.
* `access_type`: Use `offline`.

Urlencode these parameters and add them to `https://accounts.google.com/o/oauth2/auth?` to get your consent URL.

**Note:** Google only provides a refresh token once. If you lose this token you have to generate a new one using the above URL. Setting the `approval_prompt` to `force` means you will get a new refresh token (instead of *not* getting one) if the user has already authenticated your application, which is likely to happen during development.

Once you've authorized your application with Google you'll be redirected to your `redirect_uri` value and see the `code` parameter. Grab the value of that for use in the next step.


## Retrieve a Refresh Token


Setup API application in console (https://code.google.com/apis/console)
Build URL (.py) to get auth code
Open browser with URL, user accepts the application's access
Hit API with this code and oauth creds to get access & refresh token
Explain what each give you
Explain using a refresh token
Point to docs on refresh token

