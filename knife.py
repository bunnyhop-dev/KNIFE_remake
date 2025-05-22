#!/usr/bin/env python3

import os, sys
from datetime import datetime
from core.scanner import NetworkScanner
from core.menu import MainMenu
from utils.config import Config
from utils.logger import ScanLogger

def main():
    config = Config()
    logger = ScanLogger()
    scanner = NetworkScanner(config, logger)
    menu = MainMenu(scanner)

    try:
        os.system('clear')
        menu.show()
    except KeyboardInterrupt:
        print("\nExiting...")
        sys.exit(0)
    except Exception as e:
        logger.log_error(e)
        print(f"\nError: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()
