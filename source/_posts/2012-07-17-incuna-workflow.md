---
layout: post
title: How we use GitHub Flow at Incuna
extended: === read more ===
categories:
  - git
---

Our team at Incuna has been growing rapidly of late and like most businesses at this stage of growth we've had to come up with some development flows to cope with the influx of new [Incunanuts](http://twitter.com/incuna/incunanauts). Currently we have a three teams: Design, Front End and Back End with work flowing through them in roughly that order. (Technically we have an Ops team, but really that's just me part time).

We currently use GitHub to host our code, track issues and do pull requests with [hub]() for extra features like attaching code to an issue to make a pull request.

=== read more ===

## Branching
When do we branch?

![](http://f.cl.ly/items/3F0H2q0P41091O162b3N/Image%202012.07.21%2000:17:22.png)

Anything other than a trivial change goes on a branch so it can be pull requested (more on this later). Following GitHub Flow we try to keep a project's master branch production ready which branching allows us to do easily. Sometimes we have a large, long running, feature to implement which requires it's own feature master branch. This is a bit more involved as you have to make sure you pull-request onto the right branch but otherwise works well.

The most common problem I've seen with this style of branching (as with all programming) is "What do I call my branches". We try to name our branches directly around the piece of work, even if it isn't immediately obvious to every developer, that's what [git log](http://www.kernel.org/pub/software/scm/git/docs/git-log.html) is for.



treat them like old light bulbs -they're cheap, but bad for the environment if they hang around too long.


## Pull Requests

## Code Review

testing

social with good tools, no rules just best practices

What can we do better?

What's in the future?
deployments
 * current situation is sharded
 * realistically can't use one service due to customer needs/cloud uptime
 * can be easier
 * ideal is anyone can deploy

