# MCP Zabbix

A Model Context Protocol (MCP) server that provides seamless integration with Zabbix monitoring system. This tool allows AI assistants to interact with Zabbix API to retrieve monitoring data, manage hosts, check problems, and send email notifications.

## Features

- **Host Management**: Retrieve hosts, host groups, and host-specific information
- **Monitoring Data**: Access items, problems, trends, and historical data
- **User Management**: Fetch user information and roles
- **Proxy Management**: Monitor Zabbix proxy status and information
- **High Availability**: Check HA cluster nodes status
- **Email Notifications**: Send email alerts via Gmail SMTP
- **Real-time Data**: Get current monitoring status and problems

## Available Tools

| Tool | Description |
|------|-------------|
| `get_zabbix_host()` | Fetch all hosts from Zabbix API |
| `get_zabbix_host_group()` | Fetch host groups from Zabbix API |
| `get_zabbix_host_by_group(group_id)` | Fetch hosts by specific group ID |
| `get_zabbix_item(host_id)` | Fetch items for a specific host |
| `get_zabbix_problem()` | Fetch current problems from Zabbix |
| `get_zabbix_problem_by_host(host_id)` | Fetch problems for a specific host |
| `get_zabbix_trend(item_id, start_time, end_time)` | Fetch trend data for an item |
| `get_zabbix_user()` | Fetch users from Zabbix API |
| `get_zabbix_proxy()` | Fetch proxy information |
| `get_zabbix_ha_cluster_nodes()` | Fetch HA cluster nodes |
| `send_email(to_email, subject, body)` | Send email notifications |

## Installation

### Prerequisites

- Python 3.8 or higher
- Zabbix server with API access
- Valid Zabbix API token

### Method 1: Using pip

1. **Clone the repository**:
   ```bash
   git clone https://github.com/badoss/mcp_zabbix.git
   cd mcp_zabbix
   ```

2. **Create and activate virtual environment**:
   ```bash
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

### Method 2: Using uv 

1. **Install uv** (if not already installed):
   ```bash

   ```

2. **Clone and setup**:
   ```bash
   git clone https://github.com/badoss/mcp_zabbix.git
   cd mcp_zabbix
   uv sync
   ```

### Method 3: Using Docker (Not available)

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/mcp_zabbix.git
   cd mcp_zabbix
   ```

2. **Build and run with Docker Compose**:
   ```bash
   docker-compose up --build
   ```

## Configuration

### Environment Variables

1. Copy .env.example variavle and create .env in root directory outside src folder
2. Insert your own Zabbix URL , API Token

### MCP Configuration
### For Cursor

create .cursor folder in your root directory
Add this to your MCP configuration file (typically `mcp_config.json`):

For Pip install users
```json
{

}
```

Example for uv users:
```json
{
  "mcpServers": {
    "mcp-zabbix": {
      "command": "path to UV or UV",
      "args": ["run", "--directory", "src", "main.py","path to this project/mcp_zabbix/src"]
    }
  }
} 
```


### Example Usage with AI Assistant

Once configured, you can use the tools through your AI assistant:

**Get all hosts:**
```
Can you show me all the Zabbix hosts?
```

**Check problems for a specific host:**
```
What problems does host ID 10084 have?
```

**Get trend data:**
```
Show me the trend data for item 12345 from yesterday
```

**Send email notification:**
```
Send an email to admin@company.com about the critical alert
```

### Project Structure

```
mcp_zabbix/
├── src/
│   |── main.py              # Main MCP server entry point
│   |── core/                # Core configuration and utilities
│   |── services/            # Business logic and API calls
│   |── models/              # Data models
│   |── utils/               # Utility functions
|   |── pyproject.toml       # Python Dependencies for UV
├── tests/                   # Unit tests
├── examples/                # Usage examples
├── requirements.txt         # Python dependencies
└── docker-compose.yml       # Docker configuration
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Support

- **Issues**: Report bugs and request features via [GitHub Issues](https://github.com/badoss/mcp_zabbix/issues)
- **Zabbix API**: Refer to [Zabbix API documentation](https://www.zabbix.com/documentation/current/en/manual/api)
