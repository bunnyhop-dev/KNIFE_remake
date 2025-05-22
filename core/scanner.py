import asyncio, subprocess, shlex
from typing import List, Dict, Optional
from datetime import datetime
from .validator import NetworkValidator
from utils.logger import ScanLogger
from utils.config import Config

class NetworkScanner:
    def __init__(self, config: Config, logger: ScanLogger):
        self.config = config
        self.logger = logger
        self.validator = NetworkValidator()

    async def scan_target(self, target: str, scan_type: str = None, ports: List[int] = None) -> Dict:
        """Execute a scan on a single target"""
        if not self.validator.validate_ip(target):
            raise ValueError(f"Invalid target IP/hostname: {target}")

        command = ['nmap']
        if scan_type:
            command.extend(self._get_scan_flags(scan_type))
        if ports:
            command.extend(['-p', ','.join(map(str, ports))])
        command.append(target)

        try:
            result = await self._execute_command(command)
            return self._parse_result(result)
        except Exception as e:
            self.logger.log_error(e)
            raise

    async def scan_multiple(self, targets: List[str], scan_type: str = None) -> List[Dict]:
        """Execute scans on multiple targets concurrently"""
        tasks = [self.scan_target(target, scan_type) for target in targets]
        return await asyncio.gater(*tasks)

    async def _execute_command(self, command: List[str]) -> str:
        """Execute a system command asynchronously"""
        sanitized_args = [shlex.quote(arg) for arg in command]
        process = await asyncio.create_subprocess_exec(
                *sanitized_args,
                stdout=asyncio.subprocess.PIPE,
                stderr=asyncio.subprocess.PIPE
        )
        stdout, stderr = await process.communicate()

        if process.returncode != 0:
            raise subprocess.CalledProcessError(
                process.returncode,
                command,
                stdout,
                stderr
            )
        return stdout.decode()

    def _get_scan_flags(self, scan_type: str) -> List[str]:
        """Get nmap flags based on scan type"""
        scan_flags = {
            'quick': ['-F'],
            'full': ['sV', '-O'],
            'stealth': ['sS'],
            'vuln': ['--script=vuln'],
            'aggressive': ['-A'],
        }
        return scan_flags.get(scan_type, [])

    def _parse_result(self, output: str) -> Dict:
        """Parse nmap output into structured data"""
        result = {
                'timestamp': datetime.utcnow().isoformat(),
                'raw_output': output,
                'ports': [],
                'services': []
                }

        return result
