def validate_pin(pin: str):
    if len(pin) == 4 or len(pin) == 6:
        for i in pin:
            if not i.isdigit():
                return False
        return True
    return False
