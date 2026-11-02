class Solution:
    def numberOfRounds(self, loginTime: str, logoutTime: str) -> int:
        login_hour, login_minute = map(int, loginTime.split(":"))
        logout_hour, logout_minute = map(int, logoutTime.split(":"))

        login_minute = login_hour * 60 + login_minute
        logout_minute = logout_hour * 60 + logout_minute

        login_round = (login_minute + 14) // 15
        logout_round = logout_minute // 15

        if logout_minute < login_minute:  # If logout time is on the next day
            logout_round += 24 * 60 // 15  # whole day

        return max(0, logout_round - login_round)
