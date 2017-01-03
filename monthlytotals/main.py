import os
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
        '-o', '--output', type=str, help='Output directory',
        default=os.getcwd())
    args = parser.parse_args()
    save_name = 'Totals Report {} {}.pdf'.format(args.year, args.month)
    if args.output.strip() == '.':
        output_path = os.path.join(os.getcwd(), save_name)
    else:
        output_path = os.path.join(args.output, save_name)
    date = datetime.datetime(year=args.year, month=args.month, day=1)
    report = TotalsReport(date)
    daily_data, totals = report.make_report()
    variables = {
        'date': date,
        'currencies': CURRENCIES,
        'daily_data': daily_data,
        'totals': totals}
    template_to_pdf.save_pdf_from_tamplate(
        TEMPLATE_PATH, variables, output_path)

if __name__ == "__main__":
    main()
