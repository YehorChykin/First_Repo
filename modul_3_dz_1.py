from datetime import datetime
def get_days_from_today(date):
    try:
        formated_date=datetime.strptime(date, "%Y-%m-%d")
        date_now=datetime.today()
        difference=(date_now-formated_date).days
        return difference
    except ValueError:
        print("Неправильний формат дати. Використовуйте формат 'yyy-mm-dd'")
        return None

input_date = input("Введіть дату у форматі 'yyyy-mm-dd': ")
result = get_days_from_today(input_date)
if result is not None:

    print(result)


# test

