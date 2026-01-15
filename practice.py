from datetime import datetime

def timeUntilTakeOff(from_time: str, take_off_time: str) -> int:
    
    tot = datetime.strptime(take_off_time, "%Y*%m*%d@%H|%M|%S NP")
    fecha = datetime.strptime(from_time, "%Y*%m*%d@%H|%M|%S NP")

    resul = tot - fecha

    return int(resul.total_seconds())


takeoff = '2025*12*25@00|00|00 NP'

timeUntilTakeOff('2025*12*24@23|59|30 NP', takeoff)
