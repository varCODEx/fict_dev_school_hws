#

def get_min_max(arr: list[str]) -> (str, str):
    min = int(arr[0])
    max = int(arr[0])

    for d in arr:
        if (_ := int(d)) < min:
            min = _
        if (_ := int(d)) > max:
            max = _

    return min, max


def highAndLow(s: str) -> str:
    min, max = get_min_max(s.split(" "))
    return f"{max} {min}"
