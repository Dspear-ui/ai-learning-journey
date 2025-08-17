def add_time(start, duration, starting_day=None):
    day_of_the_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

    # Parse input
    time_str, period = start.split()
    start_hour, start_min = map(int, time_str.split(':'))
    dur_hour, dur_min = map(int, duration.split(':'))

    # Convert start time to 24-hour format
    if period == 'PM' and start_hour != 12:
        start_hour += 12
    elif period == 'AM' and start_hour == 12:
        start_hour = 0

    # Total minutes
    total_start_minutes = start_hour * 60 + start_min
    total_duration_minutes = dur_hour * 60 + dur_min
    final_minutes = total_start_minutes + total_duration_minutes

    # Compute final time
    final_hour_24 = (final_minutes // 60) % 24
    final_min = final_minutes % 60
    day_count = final_minutes // (24 * 60)

    # Convert back to 12-hour format
    if final_hour_24 == 0:
        final_hour = 12
        final_period = 'AM'
    elif final_hour_24 < 12:
        final_hour = final_hour_24
        final_period = 'AM'
    elif final_hour_24 == 12:
        final_hour = 12
        final_period = 'PM'
    else:
        final_hour = final_hour_24 - 12
        final_period = 'PM'

    # Format minutes
    final_min_str = f"{final_min:02}"

    # Handle day of the week
    new_day = ''
    if starting_day:
        starting_day = starting_day.capitalize()
        if starting_day in day_of_the_week:
            index = (day_of_the_week.index(starting_day) + day_count) % 7
            new_day = f", {day_of_the_week[index]}"

    # Build final string
    result = f"{final_hour}:{final_min_str} {final_period}{new_day}"
    if day_count == 1:
        result += " (next day)"
    elif day_count > 1:
        result += f" ({day_count} days later)"

    print(result)
