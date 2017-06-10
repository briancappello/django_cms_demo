from django import template

register = template.Library()


@register.filter
def page_ancestors(page):
    ancestors = []
    while page:
        ancestors.append(page)
        page = page.parent
    return ancestors
