---
layout: post
title: How we use GitHub Flow at Incuna
extended: === read more ===
categories:
  - git
---

Our team at Incuna has been growing rapidly of late and like most businesses at this stage of growth we've had to come up with some development flows to cope with the influx of new [Incunanuts](http://twitter.com/incuna/incunanauts). Currently we have three (technical) teams: Design, Front End and Back End with work flowing through them in roughly that order. (Technically we have an Ops team, but really that's just me part time).

We currently use GitHub to host our code, track issues and do pull requests with [hub]() for extra features like attaching code to an issue to make a pull request.

=== read more ===

## Branching
When do we branch?

![](http://f.cl.ly/items/3F0H2q0P41091O162b3N/Image%202012.07.21%2000:17:22.png)

Anything other than a trivial change goes on a branch so it can be pull requested (more on this later). Following GitHub Flow we try to keep a project's master branch production ready which branching allows us to do easily. However, sometimes we have a large, long running, feature to implement which requires it's own feature master branch. This is a bit more involved as you have to make sure you pull request onto the right branch but otherwise works well.

The most common problem I've seen with this style of branching (as with all programming) is "What do I call my branches". We try to name our branches directly around the piece of work, even if it isn't immediately obvious to every developer, that's what [git log](http://www.kernel.org/pub/software/scm/git/docs/git-log.html) is for.


## Pull Requests
As an extension of our branching we try to use pull requests as our main area of code review. When we first started using this as a formal method it worked quite well but more recently we've started to see the benefit of using the pull request as the main area of conversation around a bug/feature. We're still slowly moving Designers and Account Managers onto this flow but it seems to work well once they get into it.


## Code Review
While pull requests are great it's been important for us to avoid hard rules for this sort of work flow. Even if the code has been done on a branch it's quite feasible for someone to have migrations that break the database or a block of code that everyone else needs ASAP to carry on. In this situation we bring in the Master Code Reviewers [read: the nearest developer who is ideally not on your project, thus fresh set of eyes].

The most important part of this for us is to have more than one set of eyes look at new code, ideally someone who isn't familiar with it. This way we're more likely to avoid obvious bugs and create maintainable code.


## Testing
Always a sticky subject, but we're slowly getting better at it. [Charlie](http://github.com/meshy) & Marc have made great headway in setting up our large internal libraries with proper test suites and a general purge of all fixture based unit tests in favour of factories using the very awesome [Factory Boy](https://github.com/dnerdy/factory_boy). I'm hoping [travis](http://travis-ci.org) bring out pro/private accounts soon as their testing suite would suit our pull request flow perfectly and we're already moving our open source projects to them.


## What Can We Do Better?
### Deployments.
Our current situation is sharded across three different service but unfortunately this is due to the nature of our business as customers have differing needs. Currently I do the majority of the deployments. However, it *can* be easier. Eventually I want any technical person to be both capable and willing to deploy an existing site.


### Testing Culture
I think this is something that will come over time and is really a social problem, especially as we begin to firm up the ways in which we actually test projects, it should become second nature.

The Front End team has been talking about setting up testing for our Javascript projects for a while along with Selenium which I'd really like to see in action.


## Conclusion
Our workflow is centred around being social and avoiding project specialists (i.e. only one person knows about a project). I think the current situation is very good and we're improving upon it all the time, but it can always be better. Hopefully time and [new](http://henryblyth.tumblr.com/) Incunanauts will show we're on the right track!


## TL;DR
Be social, use good tools and don't have rules just best practices.


Incuna is [hiring](http://incuna.com/jobs)!

