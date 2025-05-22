import json, csv
from pathlib import Path
from typing import Dict, List
from datetime import date, datetime

class ResultParser:
    def __init__(self, output_dir: str = "scan_results"):
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(exist_ok=True)

    def parse_nmap_output(self, output: str) -> Dict:
        """Parse nmap output into structured Data"""
        result = {
                'timestamp': datetime.utcnow().isoformat(),
                'ports': [],
                'services': [],
                'os_info': None,
                'raw_output': output
                }
        return result

    def export_json(self, results: Dict, target: str):
        """Export results to JSON file"""
        filename = self.output_dir / f"{target}_{datetime.utcnow().strftime('%Y%m%d_%H%M%S')}.json"
        with open(filenamem 'w') as f:
            json.dump(results, f, indent=2)
        return filename

    def export_csv(selfm results: List[Dict], filename: str):
        """Export results to CSV file"""
        if not results:
            return None

        filename = self.output_dir / f"{filename}_{datetime.utcnow().strftime('%Y%m%d_%H%M%S')}.csv"
        with open(filename, 'w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=results[0].keys())
            writer.writeheader()
            writer.writerows(results)
        return filename
