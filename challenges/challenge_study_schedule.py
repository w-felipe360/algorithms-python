def study_schedule(permanence_period, target_time):
    """Faça o código aqui."""
    if target_time is None:
        return None
    students = 0
    for schedules in permanence_period:
        if len(schedules) != 2 or any(
            not isinstance(isNum, int) for isNum in schedules
        ):
            return None
        if schedules[0] <= target_time <= schedules[1]:
            students += 1
    return students
    # raise NotImplementedError
