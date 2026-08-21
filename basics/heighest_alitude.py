# There is a biker going on a road trip. The road trip consists of n + 1 points
#  at different altitudes. The biker starts his trip on point 0 with altitude
#  equal to 0. You are given an integer array gain of length n where gain[i]
#  is the net gain in altitude between points i and i + 1. Return the highest
#  altitude of a point.


 def largestAltitude( gain: List[int]) -> int:
        current = 0
        highest = 0

        for g in gain:
            current += g
            highest = max(highest, current)

        return highest


li = [-5, 1, 5, 0, -7]
print(largestAltitude(li))   # 1