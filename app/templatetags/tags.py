from django import template
from menus.menu_pool import menu_pool

register = template.Library()


@register.inclusion_tag('_footer_menus.html', takes_context=True)
def footer_menus(context):
    request = context['request']
    all_nodes = menu_pool.get_nodes(request, site_id=request.site.id)
    # level 0 is confusingly the home page and second level pages
    nodes = [node for node in all_nodes if node.level == 0]
    context['second_level_nodes'] = nodes[1:]  # chop off home page
    return context


@register.inclusion_tag('_footer_menu.html')
def footer_menu(node):
    return {'root_node': node}
