import os
import httpx
from dotenv import load_dotenv
from mcp.server.fastmcp import FastMCP
from services.mcp_logic import _api_call
from utils.mail import _send_email

# import func _api_call form src/services/mcp_logic.py
mcp = FastMCP("MCP Zabbix", "1.0.0")

@mcp.tool(title="Get Zabbix Host List")
def get_zabbix_host() -> dict:
    """Fetch hosts from Zabbix API"""
    params = {
        "output": ["hostid", "name", "status", "available", "ip"],
        "selectInterfaces": ["interfaceid", "type", "main", "useip", "ip", "dns", "port"],
        "selectHostGroups": ["groupid", "name"],
        "selectTags": ["tag", "value"]
    }
    return _api_call("host.get", params)

@mcp.tool(title="Get Zabbix Host Group List")
def get_zabbix_host_group() -> dict:
    """Fetch host groups from Zabbix API"""
    params = {        
       "output": "extend",
    }
    return _api_call("hostgroup.get", params)


@mcp.tool(title="Get Zabbix Host by Group ID")
def get_zabbix_host_by_group(group_id: str) -> dict:
    """Fetch hosts by group ID from Zabbix API"""
    params = {
        "groupids": group_id,
        "output": ["hostid", "name"]
    }
    return _api_call("host.get", params)


@mcp.tool(title="Get Zabbix Item by Host ID")
def get_zabbix_item(host_id: str) -> dict:
    """Fetch items for a host from Zabbix API"""
    params = {
        "output": ["itemid", "name", "lastvalue", "description", "units"],
        "filter": {"hostid": [host_id]}
    }
    return _api_call("item.get", params)

@mcp.tool(title="Get Zabbix Problem List")
def get_zabbix_problem() -> dict:
    """Fetch problems from Zabbix API"""
    params = {
        "output": "extend",
        "selectAcknowledges": ["userid", "action" , "message", "clock"],
        "selectTags": "extend",
        "recent": True,
        "sortorder": "DESC"
    }
    return _api_call("problem.get", params)

@mcp.tool(title="Get Zabbix Get Zabbix Problem List by Host ID")
def get_zabbix_problem_by_host(host_id: str) -> dict:
    """Fetch problems by host ID from Zabbix API"""
    params_trigger = {
        "output": ["triggerid"],
        "filter": {"hostid": host_id}
    }
    triggers = _api_call("trigger.get", params_trigger)

    params_problem = {
        "output": "extend",
        "selectAcknowledges": ["userid", "action" , "message", "clock"],
        "selectTags": "extend",
        "recent": True,
        "sortorder": "DESC",
        "objectids": [trigger["triggerid"] for trigger in triggers]
    }
    return _api_call("problem.get", params_problem )

@mcp.tool(title="Get Zabbix Trend Data by Item ID")
def get_zabbix_trend(item_id: str, start_time: int, end_time: int) -> dict:
    """Fetch trend data from Zabbix API"""
    params = {
        "itemids": item_id,
        "time_from": start_time,
        "time_till": end_time
    }
    return _api_call("trend.get", params)

@mcp.tool(title="Get Zabbix User List")
def get_zabbix_user() -> dict:
    """Fetch users from Zabbix API"""
    params = {
        "output": ["userid", "username", "name", "surname", "url"],
        "getAccess": True,
        "selectRole": ["roleid", "name"]
    }
    return _api_call("user.get", params)

@mcp.tool(title="Get Zabbix Proxy List")
def get_zabbix_proxy() -> dict:
    """Fetch proxies from Zabbix API"""
    params = {
        "output": ["proxyid", "name", "local_address", "local_port", "address", "port", "lastaccess" , "version" , "state"],
    }
    return _api_call("proxy.get", params)


@mcp.tool(title="Get Zabbix High availability cluster nodes")
def get_zabbix_ha_cluster_nodes() -> dict:
    """Fetch high availability cluster nodes from Zabbix API"""
    params = {
       "output": ["ha_nodeid", "address", "port" , "lastaccess"],
        "filter": {
            "status": 1
        }
    }
    return _api_call("hanode.get", params)

@mcp.tool(title="Send Email by Gmail")
def send_email(to_email: str, subject: str, body: str) -> None:
    """Send an email using Gmail SMTP server."""
    _send_email(to_email, subject, body)
    return {"status": "Email sent successfully."}

if __name__ == "__main__":
    mcp.run(transport="stdio")
