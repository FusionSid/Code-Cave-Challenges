hour_degree = lambda hh, mm: hh * (360 / 12) + (mm * 360) // (12 * 60)
minutes_degree = lambda mm: (mm * 360) // 60


def get_angle(time: str) -> str:
    hour, minute = (int(i) for i in time.split(":"))
    h = hour_degree((hour % 12), minute)
    m = minutes_degree(minute)

    angle = abs(h - m)
    angle = 360 - angle if angle > 180 else angle

    return f"{int(angle)}°"


print(get_angle("5:30"))
print(get_angle("21:00"))
print(get_angle("12:00"))
