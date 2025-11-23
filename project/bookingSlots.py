from datetime import datetime, time, timedelta

def get_next_7_days(startHour=9, endHour=17, intervalMinutes=30):
    finalData = []

    now = datetime.now()

    for i in range(7):
        dayDate = now + timedelta(days=i)

        slots = []
        currentTime = time(startHour, 0)
        endTime = time(endHour, 0)

        while currentTime < endTime:
            slotDateTime = datetime.combine(dayDate.date(), currentTime)

             # Check if slot time is passed
            isAvailable = slotDateTime > now 

            slots.append({
                "time": currentTime.strftime("%I:%M %p"),
                "availabel": isAvailable
            })

            # increase time interval
            hours = currentTime.hour
            minutes = currentTime.minute + intervalMinutes 

            if minutes >= 60:
                hours += 1
                minutes -= 60

            currentTime = time(hours, minutes)

        finalData.append({
            "dayName": dayDate.strftime("%a"),
            "day": dayDate.strftime("%d"),
            "fullDate": dayDate.strftime("%Y-%M-%d"),
            "slots": slots
        })

    print(finalData)
get_next_7_days()