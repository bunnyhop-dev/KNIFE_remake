from ipaddress import ip_address, ip_network
from typing import Union
import re

class NetworkValidator:
    @staticmethod
    def validate_ip(ip_str: str) -> bool:
        """Validate IP address or hostname"""
        try:
            ip_address(ip_str)
            return True
        except ValueError:
            hostname_pattern = r'^[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\n.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$'
            return bool(re.match(hostname_pattern, ip_str))

    @staticmethod
    def validate_port_range(port_range: str) -> bool:
        """Validate port range string"""
        try:
            if '-' in port_range:
                start, end = map(int, port_range.split('-'))
                return 0 <= start <= end <= 65535
            else:
                port = int(port_range)
                return 0 <= port <= 65535
        except (ValueError, AttributeError):
            return False

    @staticmethod
    def validate_scan_type(scan_type: str) -> bool:
        """Validate scan type"""
        valid_types = {'quick', 'full', 'stealth', 'vuln', 'aggressive'}
        return scan_type in valid_types
