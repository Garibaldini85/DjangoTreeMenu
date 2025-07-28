from django import template
from django.urls import resolve
from tree_menu.models import Menu, MenuItem
from tree_menu.utils import build_menu_tree

register = template.Library()


@register.inclusion_tag('tree_menu/menu.html', takes_context=True)
def draw_menu(context, menu_name):
    try:
        menu = Menu.objects.get(name=menu_name)
    except Menu.DoesNotExist:
        return {'menu_tree': []}

    path = context['request'].path
    menu_items = MenuItem.objects.filter(menu=menu).select_related('parent')
    tree = build_menu_tree(menu_items, path)
    return {'menu_tree': tree}
