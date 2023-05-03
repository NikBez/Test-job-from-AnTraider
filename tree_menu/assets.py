from .models import MenuItem


def get_items(active):
    parents = []
    childs = []

    if not active:
        return parents, childs

    menu_items = MenuItem.objects.filter(menu=active.menu).prefech_related('children')

    for item in menu_items:
        if item.parent == active:
            childs.append(item)

    while active.parent:
        parents.append(active.parent)
        active = active.parent

    return parents, childs

















