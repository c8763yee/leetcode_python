class Solution:
    def dayOfYear(self, date: str) -> int:
        year, month, day = map(int, date.split('-'))
        m = [0,31,28,31,30,31,30,31,31,30,31,30,31]
        if year%100 and year%4==0 or year%400 == 0:
            m[2] += 1
        date = day
        for i in range(month):
            date += m[i]
        return date