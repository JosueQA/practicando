from datetime import datetime

def timeUntilTakeOff(from_time: str, take_off_time: str) -> int:
    print(from_time)
    
    fecha = datetime.strptime(from_time, "%Y*%m*%d@%H|%M|%S NP")

    print(from_time)
    return 0


takeoff = '2025*12*25@00|00|00 NP'

timeUntilTakeOff('2025*12*24@23|59|30 NP', takeoff)
