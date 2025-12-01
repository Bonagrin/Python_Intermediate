import sys
import getpass
import logging
import colorama
import termcolor

if __name__ == "__main__":

    logging.basicConfig(
    filename = 'Jelszó.log',
    level = logging.DEBUG,
    format = '%(asctime)s - %(levelname)s - %(message)s'
    )
    colorama.init()

    logging.info('Start Program')

    if (admin := input('Add meg az Admin felhasználót: ')) == 'Admin' and \
        (jsz := getpass.getpass('Add meg az Admin jelszót: ')) == 'Admin':
        logging.debug('Ervenyes Admin')

        user_adatok = {}

        új_azonosító = input('Regisztrálj egy új azonosítót: ')
        új_jelszó = getpass.getpass('Regisztrálj egy új jelszót: ')
        logging.debug(f'Azonosíto: {új_azonosító}, Jelszo: {új_jelszó}')

        # csak a feladat miatt
        user_adatok[új_azonosító] = új_jelszó
        print(user_adatok)

    else:
        logging.debug('Hacker Attacked!!, TERMINATED')
        sys.exit(termcolor.colored('Nice try hacker!', 'blue', 'on_yellow'))

    logging.info('Stop Program')