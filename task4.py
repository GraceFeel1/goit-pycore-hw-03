
from datetime import datetime, timedelta


def get_upcoming_birthdays(users):
    today = datetime.today().date()
    upcoming_birthdays = []

    for user in users:
        try:
            birthday = datetime.strptime(
                user["birthday"], "%Y.%m.%d"
            ).date()

            birthday_this_year = birthday.replace(year=today.year)

        except (ValueError, TypeError, KeyError):
            continue

        if birthday_this_year < today:
            try:
                birthday_this_year = birthday.replace(
                    year=today.year + 1
                )
            except ValueError:
                birthday_this_year = datetime(
                    today.year + 1, 2, 28
                ).date()

        days_until_birthday = (birthday_this_year - today).days

        if 0 <= days_until_birthday <= 6:
            congratulation_date = birthday_this_year

            if congratulation_date.weekday() == 5:
                congratulation_date += timedelta(days=2)
            elif congratulation_date.weekday() == 6:
                congratulation_date += timedelta(days=1)

            upcoming_birthdays.append({
                "name": user["name"],
                "congratulation_date": congratulation_date.strftime(
                    "%Y.%m.%d"
                )
            })

    return upcoming_birthdays


users = [
    {"name": "John Doe", "birthday": "1995.10.30"},
    {"name": "Jane Smith", "birthday": "1998.11.02"},
    {"name": "Alex Brown", "birthday": "2000.12.15"}
]

upcoming_birthdays = get_upcoming_birthdays(users)

print("Список привітань на цьому тижні:", upcoming_birthdays)
