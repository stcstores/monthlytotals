from . settings import CURRENCIES


class DailyTotals:
    currencies = CURRENCIES
    fields = CURRENCIES + ['Total', 'EPOS']

    def __init__(self, day):
        self.day = day
        self.data = {field: 0 for field in self.fields}

    def __getitem__(self, key):
        return self.data[key]

    def __setitem__(self, key, value):
        self.data[key] = value
        self.data['Total'] = sum(
            (self.data[currency] for currency in self.currencies))

    def get_data(self):
        data = self.data
        data['Day'] = self.day
        return data
