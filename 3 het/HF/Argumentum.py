import sys
import logging
import colorama
import termcolor

if __name__ == "__main__":

    logging.basicConfig(
        filename = 'Argumentum.log',
        level = logging.DEBUG,
        format = '%(asctime)s - %(levelname)s - %(message)s'
    )

    colorama.init()

    total = 0

    logging.info('Start Program')
    for argumentum in sys.argv[1:]:
        try:
            total += int(argumentum)
        
        except ValueError:
            total = 0
            logging.debug(f'Not int argument, TERMINATED: {argumentum}')
            sys.exit(f'Not int argument: {argumentum}')


    print(termcolor.colored(f'Sum: {total} ', 'blue', 'on_yellow'))

    logging.debug(f'Finished with: {total}')
    logging.info('Stop Program')
