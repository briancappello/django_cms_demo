from django import template

register = template.Library()


@register.filter
def reversed(list):
    return list[::-1]


@register.filter
def is_active(node):
    if node.selected:
        return True
    for child in node.children:
        if is_active(child):
            return True
    return False


@register.filter
def page_ancestors(page):
    ancestors = []
    while page:
        ancestors.append(page)
        page = page.parent
    return ancestors
