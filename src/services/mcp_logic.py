import os
import httpx
from dotenv import load_dotenv
load_dotenv()

ZABBIX_API_URL = os.getenv("ZABBIX_API_URL")
ZABBIX_API_TOKEN = os.getenv("ZABBIX_API_TOKEN")


def _api_call(method: str, params: dict = None) -> dict:
    """Make API call to Zabbix"""
    headers = {
        "Content-Type": "application/json-rpc",
        "Authorization": f"Bearer {ZABBIX_API_TOKEN}"
    }
    payload = {
        "jsonrpc": "2.0",
        "method": method,
        "params": params or {},
        "id": 1
    }
    response = httpx.post(ZABBIX_API_URL, headers=headers, json=payload)
    return response.json()


def _api_create_host(hostname: str, ip: str, templates: list , groups: list , tags: list , type_interface: str) -> dict:
    """Create a host in Zabbix"""

    if type_interface not in ["agent", "snmp", "ipmi", "jmx"]:
        raise ValueError(f"Invalid interface type: {type_interface}")
    # Map interface type to Zabbix type
    interface_type_map = {
        "agent": 1,  # Zabbix agent
        "snmp": 2,   # SNMP
        "ipmi": 3,   # IPMI
        "jmx": 4     # JMX
    }
    type_interface = interface_type_map[type_interface]
    
    headers = {
        "Content-Type": "application/json-rpc",
        "Authorization": f"Bearer {ZABBIX_API_TOKEN}"
    }
    payload = {
        "jsonrpc": "2.0",           
        "method": "host.create",
        "params": {
            "host": hostname,
            "interfaces": [
                {
                    "type": 1,
                    "main": 1,
                    "useip": 1,
                    "ip": ip,
                    "dns": "",
                    "port": "10050"
                }
            ],
            "groups": [{"groupid": group} for group in groups],
            "templates": [{"templateid": template} for template in templates]
        },
        "id": 1
    }
    response = httpx.post(ZABBIX_API_URL, headers=headers, json=payload)
    return response.json()