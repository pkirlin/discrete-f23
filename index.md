---
layout: home
title: Home
nav_exclude: false
nav_order: 0
seo:
  type: Course
  name: Just the Class
---

# {{ site.tagline }}
{: .mb-2 }
{{ site.description }}
{: .fs-6 .fw-300 }

{% if site.announcements %}
{{ site.announcements.last }}
[Announcements](announcements.md){: .btn .btn-outline .fs-3 }
{% endif %}

## Administrivia
- Instructor: Phillip Kirlin
- Office hours: Mondays 1-2, Tuesdays 12:30-2, Wednesdays 3-4:30, Thursdays 2-3.  Also available by appointment and over Slack.
- [Canvas page](https://rhodes.instructure.com/courses/5968): Use for grades, online assignment submissions, and assignment solutions.
- [Syllabus](syllabus/syllabus-172-f23.pdf) and [additional policies](syllabus/additional-policies.pdf).

## Resources

- [Logic reference sheet](https://www.cs.rhodes.edu/~kirlinp/courses/discrete/f17/handouts/cheatsheet.pdf)
     

## Calendar
{% for module in site.modules %}
{{ module }}
{% endfor %}

