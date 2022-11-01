import argparse
import textwrap

from config import setup_logging

setup_logging()
import logging

from calc import calculate_unit_price
from inputs import csv_input, user_input
from outputs import to_word

log = logging.getLogger(__name__)


def main():
    log.info(' program start '.center(80, '-'))

    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description=textwrap.dedent(
            """
            Label maker
            ----------------------
                default to user input from console
                if you wish, you may specify input and template file
                input must be a csv file, output then a jinja formatted docx
            """
        ))

    args = parser.parse_args()

    data_input = "user"
    data = []

    if data_input == "user":
        data = user_input()
    elif data_input == "csv":
        # TODO: vyměnit za argument od argparse
        file_path = "input/sample_data.csv"
        data = csv_input(file_path)
    else:
        log.warning(f"neznám možnost vstupu: {data_input}")
        exit()
        # print("neznám")


    calculated_data = calculate_unit_price(data)
    to_word(calculated_data, 'templates/labels_template.docx')
    log.info(' program end '.center(80, '-'))


if __name__ == '__main__':
    main()
