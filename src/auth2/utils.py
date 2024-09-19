def has_level_permissions(request, demand_level) -> bool:
    department, level = request.user.main_department
    if level > demand_level:
        return False
    return True
