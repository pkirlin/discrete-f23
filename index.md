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
- Office hours: Mon & Tue 3:30-5, Wed 10-11, Thu 11-12.  Also available by appointment and over Slack.
- [Canvas page](https://rhodes.instructure.com/courses/4911): Use for grades, online assignment submissions, and assignment solutions.
- [Syllabus](syllabus/syllabus-ml-s23.pdf) and [additional policies](syllabus/additional-policies.pdf).
- Rescheduled midterm 1 date: Tue, Feb 28, in class.

## Resources
     

## Calendar
{% for module in site.modules %}
{{ module }}
{% endfor %}

