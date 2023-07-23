from datetime import datetime

n = datetime.now()
summer = [ 6, 7, 8, 9]
winter = [10, 11, 12, 1, 2, 3, 4, 5]
peak_start = 14
peak_end = 18



# n.weekday() mon = 0, use n.isoweekday() mon will = 1
if n.month in summer and n.isoweekday() <6:
    if peak_start >= n.hour <= peak_end: onpeak
    else: offpeak
else:
    if n.month in winter: winter
    else: offpeak
