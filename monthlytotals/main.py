import argparse
import datetime

import template_to_pdf

from . totalsreport import TotalsReport
from . settings import CURRENCIES, TEMPLATE_PATH


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-y', '--year', type=int, help='Four digit year', required=True)
    parser.add_argument(
        '-m', '--month', type=int, help='Two digit month', required=True)
    parser.add_argument(
        '-o', '--output', type=str, help='Output path', required=True)
    args = parser.parse_args()
    date = datetime.datetime(year=args.year, month=args.month, day=1)
    report = TotalsReport(date)
    daily_data, totals = report.make_report()
    variables = {
        'date': date,
        'currencies': CURRENCIES,
        'daily_data': daily_data,
        'totals': totals}
    table_html = template_to_pdf.get_html(TEMPLATE_PATH, variables)
    with open('report.html', 'w') as outfile:
        outfile.write(table_html)
    template_to_pdf.save_pdf_from_tamplate(
        TEMPLATE_PATH, variables, args.output)

if __name__ == "__main__":
    main()
