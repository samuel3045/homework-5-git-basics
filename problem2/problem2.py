def date_format(date: str) -> str:
    month, day, year = date.split('/')
    return f"{year}-{month}-{day}"