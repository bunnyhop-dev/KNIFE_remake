import os, sys, asyncio
from datetime import datetime
from typing import Dict, Callable
from .scanner import NetworkScanner

class MainMenu:
    def __init__(self, scanner: NetworkScanner):
        self.scanner = scanner
        self.options = {
                '1': ('What\'s my IP address?', self._show_ip),
                '2': ('Scan with script for vulnerabilities', self._vuln_scan),
                '3': ('Ping Scan', self._ping_scan),
                '4': ('Port Scan', self._port_scan),
                '5': ('Host Scan', self._host_scan),
                '6': ('OS Detection', self._os_detection),
                '7': ('Stealth Scanning', self._stealth_scan),
                '8': ('IPv6 Scanning', self._ipv6_scan),
                '0': ('Exit', self._exit)
                }

    def show(self):
        """Displayer the main menu"""
        while True:
            self._display_header()
            self._display_options()
            choice = input("\n> ").strip()

            if choice in self.options:
                func = self.options[choice][1]
                os.system('clear')
                func()
            else:
                print("\nERROR: Invalid Choice")
                input("Press Enter to continue...")

    def _display_header(self):
        version = "1.3.5"
        """Display the application header"""
        os.system('clear')
        print("""
        ██ ▄█▀ ███▄    █  ██▓  █████▒▓█████
        ██▄█▒  ██ ▀█   █ ▓██▒▓██   ▒ ▓█   ▀
        ▓███▄░ ▓██  ▀█ ██▒▒██▒▒████ ░ ▒███
        ▓██ █▄ ▓██▒  ▐▌██▒░██░░▓█▒  ░ ▒▓█  ▄
        ▒██▒ █▄▒██░   ▓██░░██░░▒█░    ░▒████▒
        ▒ ▒▒ ▓▒░ ▒░   ▒ ▒ ░▓   ▒ ░    ░░ ▒░ ░
        ░ ░▒ ▒░░ ░░   ░ ▒░ ▒ ░ ░       ░ ░  ░
        ░ ░░ ░    ░   ░ ░  ▒ ░ ░ ░       ░
        ░  ░            ░  ░             ░  ░
        """)
        print(f"Current Time (UTC): {datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"User: {os.getenv('USER', 'unknow')}")
        print(f"Version: {version}")
        print("\nDescription: Network scanning and reconnaissance tool\n")

    def _display_options(self):
        """Display menu options"""
        for key, (description, _) in self.options.items():
            print(f"[{key}] {description}")

    def _show_ip(self):
        os.system('ip addr')
        input("\nPress Enter to continue...")

    def _vuln_scan(self):
        target = input("Enter target IP/URL: ")
        asyncio.run(self.scanner.scan_target(target, 'vuln'))
        input("\nPress Enter to continue...")

    def _ping_scan(self):
        target = input("Enter target IP/URL: ")
        asyncio.run(self.scanner.scan_target(target, 'quick'))
        input("\nPress Enter to continue...")

    def _port_scan(self):
        target = input("Enter target IP/URL: ")
        ports = input("Enter ports (e.g., 80 443 ir 1-1000): ")
        if self.scanner.validator.validate_port_range(ports):
            asyncio.run(self.scanner.scan_target(target, ports=ports.split(',')))
        input("\nPress Enter to continue...")

    def _host_scan(self):
        target = input("Enter target network (e.g., 192.168.1.0/24): ")
        asyncio.run(self.scanner.scan_target(target, 'quick'))
        input("\nPress Enter to continue...")

    def _os_detection(self):
        target = input("Enter target IP/URL: ")
        asyncio.run(self.scanner.scan_target(target, 'full'))
        input("\nPress Enter to continue...")

    def _stealth_scan(self):
        target = input("Enter target IP/URL: ")
        asyncio.run(self.scanner.scan_target(target, 'stealth'))
        input("\nPress Enter to continue...")

    def _ipv6_scan(self):
        target = input("Enter IPV6 address: ")
        command = ['nmap', '-6'] + [target]
        input("\nPress Enter to continue...")

    def _exit(self):
        print("\nExiting...")
        sys.exit(0)
