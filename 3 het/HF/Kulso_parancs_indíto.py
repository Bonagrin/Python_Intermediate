import subprocess
import sys
import logging
import colorama
import termcolor


if __name__ == "__main__":
    
    logging.basicConfig(
    filename = 'Kulso_parancs.log',
    level = logging.DEBUG,
    format = '%(asctime)s - %(levelname)s - %(message)s'
    )
    colorama.init()

    logging.info('Start Program')
    try:
        processz = subprocess.run(['python', 'Kulso_parancs_process.py'], capture_output=True)
        ertek = processz.stdout.decode('utf-8')
        logging.info(f"Kulso parancs eredmenye: {ertek}")
        print(termcolor.colored(ertek, "cyan"))
        
    except Exception as e:
        logging.error(f"Hiba tortent, TERMINATED {e}")
        sys.exit(termcolor.colored(f"Hiba tortent: {e}", "red"))

    logging.info('Stop Program')