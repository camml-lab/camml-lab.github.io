---
title: "{{ replace .File.ContentBaseName "-" " " | title }}"
role: "PhD student"       # e.g. Team leader, Postdoctoral researcher, PhD student, Visiting researcher
status: "current"         # current | alumni
weight: 30                # order on the page: lower comes first
start: {{ now.Year }}     # year joined
end:                      # year left (alumni only)
now: ""                   # alumni only: where they are now
photo_anchor: "Center"    # which part of photo.jpg to keep when cropping: Center, Top, Bottom...
email: ""
links:
  github: ""
  scholar: ""
  orcid: ""
  website: ""
---
A short bio (2–3 sentences). Put a square photo named photo.jpg next to this file.
