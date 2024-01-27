from datetime import datetime, timedelta

users = [
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Jane Smith", "birthday": "1990.01.27"}
]

def get_upcoming_birthdays(user):
    user_date_b_date = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
    date_now = datetime.today().date()
    user_date_birthdays_in_this_year = user_date_b_date.replace(year=datetime.now().year)
    difference_day = (user_date_birthdays_in_this_year - date_now).days
    day_of_week = user_date_birthdays_in_this_year.weekday()

    if difference_day < 0:
        user_date_birthdays_in_this_year = user_date_b_date.replace(year=(user_date_birthdays_in_this_year.year + 1))
        print(f"{user['name']}'s birthday is in the next year.")

    elif day_of_week >= 5:
        days_until_monday = 8 - day_of_week
        user_date_birthdays_in_this_year += timedelta(days=days_until_monday)
        print(f"{user['name']}'s birthday is moved to Monday.")
    
    return {"name": user["name"], "congratulation_date": user_date_birthdays_in_this_year.strftime("%Y.%m.%d")}

upcoming_birthdays = [get_upcoming_birthdays(user) for user in users]
print("Список привітань на цьому тижні:", upcoming_birthdays)