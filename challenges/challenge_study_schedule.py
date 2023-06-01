def study_schedule(permanence_period, target_time):
    """Faça o código aqui."""
    if target_time is None:
        return None
    students = 0
    try:
        for schedules in permanence_period:
            if schedules[0] <= target_time <= schedules[1]:
                students += 1
        return students
    except:
        return None
    # raise NotImplementedError
