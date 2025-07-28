def build_menu_tree(menu_items, current_path):
    items = {item.id: {'item': item, 'children': [], 'open': False, 'active': False} for item in menu_items }

    root_items = []

    active_item_id = None

    for item in menu_items:
        if item.get_absolute_url() == current_path:
            active_item_id = item.id
            break

    for item in menu_items:
        if item.parent_id:
            items[item.parent_id]['children'].append(items[item.id])
        else:
            root_items.append(items[item.id])

    def mark_active_path(item_id):
        while item_id:
            items[item_id]['open'] = True
            if item_id == active_item_id:
                items[item_id]['active'] = True
            item_id = items[item_id]['item'].parent_id

    if active_item_id:
        mark_active_path(active_item_id)

    return root_items
