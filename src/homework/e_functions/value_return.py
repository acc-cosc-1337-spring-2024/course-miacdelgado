def get_seconds(epoch_seconds):
    remaining_seconds = epoch_seconds // (24 * 3600)
    total_seconds_left = int(remaining_seconds % 60)

    return total_seconds_left

def get_minutes(epoch_seconds):
    remaining_minutes = epoch_seconds // 60
    total_minutes_left = int(remaining_minutes % 60)

    return total_minutes_left

def get_hours(epoch_seconds):
    seconds_to_hours = epoch_seconds // 3600
    total_hours_left = int(seconds_to_hours % 24)

    return total_hours_left