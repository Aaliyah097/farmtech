def has_level_permissions(request, demand_level) -> bool:
    if request.user.is_superuser:
        return True
    department, level = request.user.main_department
    if level > demand_level:
        return False
    return True
