import datetime
import calendar

from stclocal import PyLinnworks
import exchange_rates

from . dailytotals import DailyTotals
from . settings import CURRENCIES


class TotalsReport:
    currencies = CURRENCIES

    def __init__(self, date):
        self.processed_orders = PyLinnworks.ProcessedOrders()
        self.date = date
        self.year = date.year
        self.month = date.month
        month_length = calendar.monthrange(self.year, self.month)[1]
        self.date_list = [
            datetime.date(day=x, month=self.month, year=self.year) for x in
            range(1, month_length + 1)]

    def get_totals_for_date(self, day):
        orders = self.processed_orders.get_all_processed_orders_for_day(
            day, 'RECEIVED')
        totals = DailyTotals(day)
        for order in orders:
            source = order.source
            currency = order.currency
            total = order.total_charge
            if source == 'EPOS':
                totals['EPOS'] += total
            else:
                if currency in self.currencies:
                    totals[currency] += total
        return totals

    def get_exchange_rate(self, day, currency):
        return exchange_rates.get_rates(
            day=day, base=currency, symbols=['GBP'])

    def make_report(self):
        header = ['Date'] + self.currencies + ['Total', 'EPOS']
        daily_data = []
        totals = {head: 0 for head in header if head != 'Date'}
        for day in self.date_list:
            print('Retrieving Data for ' + day.strftime('%Y-%m-%d'))
            daily_total = self.get_totals_for_date(day)
            daily_data.append(daily_total.get_data())
            for field in daily_total.fields:
                totals[field] += daily_total[field]
        total_row = [totals[field] for field in daily_total.fields]
        return daily_data, total_row
