def final_grade(exam, projects):
    if exam >= 90 or projects >= 10:
        return 100
    elif exam >= 75 or projects >= 5:
        return 90
    elif exam >= 50 or projects >= 2:
        return 75
    return 0
