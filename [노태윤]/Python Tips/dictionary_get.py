WEEKDAY = {
    1: 'Sunday',
    2: 'Monday',
    3: 'Tuesday',
    4: 'Wednesday',
    5: 'Thursday',
    6: 'Friday',
    7: 'Saturday' }
ERROR = 'Wrong, please enter a number between 1 and 7'


def whatday(n):
    return WEEKDAY.get(n, ERROR)
  
# ========================================================
# 만약 dictionary key 에 없으면 get 을 활용하면 된다
