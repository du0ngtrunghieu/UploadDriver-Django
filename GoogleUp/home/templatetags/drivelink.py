from django import template

register = template.Library()

@register.filter(name="convert_drivelink")
def convert_drivelink(url):
    return url.split("/")[5]