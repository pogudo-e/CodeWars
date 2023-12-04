def set_alarm(employed, vacation):
    if employed:
        if not vacation:
            return True
    return False


print(set_alarm(True, True))
