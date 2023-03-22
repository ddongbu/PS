from datetime import datetime
today = int(datetime.today().strftime('%Y'))

def solution(age):
    return (today-age)