def add_time(start, duration, day_of_week=None):
    # Parse start time
    start = start.split(" ")
    start_list = [float(i) for i in start[0].split(":")]
    if start[1]=="PM":
        start_list[0] += 12
    start_time = start_list[0]*60+start_list[1]
    # Parse duration
    duration = [float(i) for i in duration.split(":")]
    duration = duration[0]*60+duration[1]
    # Parse day of week
    week_days = {
        0: None,
        1: "Saturday",
        2: "Sunday",
        3: "Monday",
        4: "Tuesday",
        5: "Wednesday",
        6: "Thursday",
        7: "Friday"
    }
    if isinstance(day_of_week, str):
        day_of_week = day_of_week.title()
    day_of_week = [i for i in week_days if week_days[i]==day_of_week][0]
    # Add time
    new_time = start_time + duration
    minutes = int(new_time % 60)
    hours = int((new_time // 60) % 24)
    days = int((new_time // 60) // 24)
    # Get the result in parts
    if hours > 12:
        time = f"{hours-12}:{minutes:02} PM"
    elif hours == 12:
        time = f"{hours}:{minutes:02} PM"
    elif hours == 0:
        time = f"12:{minutes:02} AM"
    else:
        time = f"{hours}:{minutes:02} AM"
    
    if day_of_week==0:
        day = ""
    elif day_of_week>0:
        day_of_week = (day_of_week+days)%7
        if day_of_week==0:
            day_of_week = 7
        day = f", {week_days[day_of_week]}"
    
    if days>1:
        lapsed = f" ({days} days later)"
    elif days==1:
        lapsed = " (next day)"
    elif days==0:
        lapsed = ""
    
    final_new_time = time+day+lapsed
    return final_new_time


print(add_time("11:59 PM", "24:05", "Wednesday"))