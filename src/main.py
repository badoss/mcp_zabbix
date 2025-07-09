import os
import httpx
import json
from dotenv import load_dotenv
from mcp.server.fastmcp import FastMCP
from services.mcp_logic import _api_call
from utils.mail import _send_email
from utils.graph import _construct_graph

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

@mcp.tool(title="Construct Graph")
def construct_graph(item_name: str) -> dict:
    """Construct a graph from the data"""

    data = {
    "jsonrpc": "2.0",
    "result": [
        {
            "itemid": "50134",
            "clock": "1750842000",
            "num": "26",
            "value_min": "1.661105",
            "value_avg": "2.033985423076923",
            "value_max": "2.907631"
        },
        {
            "itemid": "50134",
            "clock": "1750845600",
            "num": "60",
            "value_min": "1.449433",
            "value_avg": "2.0194116833333338",
            "value_max": "4.784133"
        },
        {
            "itemid": "50134",
            "clock": "1750849200",
            "num": "60",
            "value_min": "1.497801",
            "value_avg": "2.066933033333333",
            "value_max": "10.613991"
        },
        {
            "itemid": "50134",
            "clock": "1750852800",
            "num": "60",
            "value_min": "1.429875",
            "value_avg": "1.7798675000000002",
            "value_max": "2.159854"
        },
        {
            "itemid": "50134",
            "clock": "1750856400",
            "num": "60",
            "value_min": "1.375525",
            "value_avg": "1.7987132333333333",
            "value_max": "2.282539"
        },
        {
            "itemid": "50134",
            "clock": "1750860000",
            "num": "60",
            "value_min": "1.48093",
            "value_avg": "1.94930165",
            "value_max": "8.280128"
        },
        {
            "itemid": "50134",
            "clock": "1750863600",
            "num": "60",
            "value_min": "1.417314",
            "value_avg": "1.8020279166666668",
            "value_max": "2.398512"
        },
        {
            "itemid": "50134",
            "clock": "1750867200",
            "num": "60",
            "value_min": "1.514085",
            "value_avg": "1.8175866666666671",
            "value_max": "2.466219"
        },
        {
            "itemid": "50134",
            "clock": "1750870800",
            "num": "60",
            "value_min": "1.476906",
            "value_avg": "1.7907370333333332",
            "value_max": "2.609873"
        },
        {
            "itemid": "50134",
            "clock": "1750874400",
            "num": "60",
            "value_min": "1.455132",
            "value_avg": "1.8111600666666674",
            "value_max": "2.890896"
        }
    ],
    "id": 1
}
    return _construct_graph(data, item_name)

if __name__ == "__main__":
    mcp.run(transport="stdio")
