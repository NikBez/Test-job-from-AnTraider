from django import template
from django.utils.safestring import mark_safe

from tree_menu.models import MenuItem


register = template.Library()

@register.simple_tag(takes_context=True)
def draw_menu(context, menu_name):
    root_items = MenuItem.objects.filter(parent__isnull=True, menu__name=menu_name)

    if not root_items:
        return ''

    def render_menu_items(menu_items):
        res = '<ul>'
        for item in menu_items:
            active = ''
            if context['request'].path.startswith(item.url):
                active = 'active'
            res += f'<li class="{active}"><a href="/{item.url}">{item.name}</a>'
            if item.children.exists() and item.url in context['request'].path:
                res += render_menu_items(item.children.all())
            res += '</li>'
        res += '</ul>'
        return mark_safe(res)

    return render_menu_items(root_items)


