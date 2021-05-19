# parking_rate.py
# from .common import *


class ParkingRate:
    def __init__(self, rate=0.5):
        self.rate = rate

    def payment(self, time):
        amount = time * self.rate
        return amount


class FracParkingRate(ParkingRate):
    def __init__(self, rate=0.5, deduction=1.0):
        super().__init__(rate)
        self.deduction = deduction

    def payment(self, time):
        amount = super().payment(time) - (time//15)*1.0
        return amount


class HourParkingRate(FracParkingRate):
    def __init__(self, rate=0.5, frac_deduction=1.0, hour_deduction=1.0):
        super().__init__(rate, frac_deduction)
        self.hour_deduction = hour_deduction

    def payment(self, time):
        amount = super().payment(time) - (time//60)*1.0
        return amount


class DailyParkingRate(ParkingRate):
    def __init__(self, rate=0.2, fee=110.0,daily_hour=9):
        super().__init__(rate)
        self.fee = fee
        self.daily_hour = daily_hour

    def payment(self, time):
        daily = time//(self.daily_hour*60)
        amount = daily*self.fee + super().payment(time%(self.daily_hour*60))
        return amount


class NightParkingRate(HourParkingRate):
    def __init__(self, rate=0.5, frac_deduction=1.0, hour_deduction=1.0, fee=30.0):
        super().__init__(rate, frac_deduction, hour_deduction)
        self.fee = fee

    def payment(self, time):
        amount = self.fee + super().payment(time)
        return amount


class MonthlyParkingRate():
    def __init__(self, fee=500.0):
        self.fee = fee

    def payment(self, time: None):
        amount = self.fee
        return amount


if __name__ == "__main__":
    ticket = DailyParkingRate()
    print(ticket.payment(9*60 + 500))


