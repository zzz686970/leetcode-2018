from datetime import datetime

def daysBetweenDates(date1, date2):
    date1, date2 = datetime.strptime(date1, '%Y-%m-%d'), datetime.strptime(date2, '%Y-%m-%d')
    return (date2 - date1).days if date2 > date1 else (date1 - date2).days


from datetime import date
def daysBetweenDates(date1: str, date2: str) -> int:
    s1, s2 = date1.split("-"), date2.split("-")
    d1, d2 = date(*map(int, s1)), date(*map(int, s2))
    return abs((d1-d2).days)