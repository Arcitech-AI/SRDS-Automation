from datetime import datetime


def get_current_date():
    now = datetime.now()
    current_year = now.year
    current_month = now.month
    current_day = now.day

    return current_year, current_month, current_day


if __name__ == "__main__":
    year, month, day = get_current_date()
    print(type(day))
    print(f"Current date: {year}-{month:02d}-{day:02d}")
