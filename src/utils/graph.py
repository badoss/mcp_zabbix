from datetime import datetime

def _construct_graph(data, item_name):
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    
    graph = Graph(data, plt, item_name)
    result = graph.plot_trend_graph()
    return result

class Graph:
    def __init__(self, data, plt, item_name=None):
        self.data = data
        self.item_name = item_name or "Unknown Item"
        self.timestamps = []
        self.values_min = []
        self.values_avg = []
        self.values_max = []
        self.plt = plt
        self.process_data()
    
    def process_data(self):
        """Process Zabbix trend data into lists for plotting"""
        if not self.data or 'result' not in self.data:
            return
        
        for item in self.data['result']:
            timestamp = int(item['clock'])
            self.timestamps.append(self.time_to_timestamp(timestamp))
            self.values_min.append(float(item['value_min']))
            self.values_avg.append(float(item['value_avg']))
            self.values_max.append(float(item['value_max']))

    def time_to_timestamp(self, time):
        """Convert Unix timestamp to datetime object"""
        return datetime.fromtimestamp(int(time))
    
    def get_item_description(self):
        pass
        return "No description available"

    def plot_trend_graph(self):
        """Plot trend data with min, avg, max values"""
        if not self.timestamps:
            return {"error": "No data to plot"}
        
        self.plt.figure(figsize=(14, 8))
        
        # Plot lines
        self.plt.plot(self.timestamps, self.values_avg, label='Average', 
                color='blue', marker='o', linewidth=2, markersize=4)
        
        self.plt.plot(self.timestamps, self.values_min, label='Minimum', 
                color='green', marker='o', linewidth=2, markersize=4)
        
        self.plt.plot(self.timestamps, self.values_max, label=f'Maximum', 
                color='red', marker='o', linewidth=2, markersize=4)
    
        self.plt.title(f'{self.item_name} - Trend Data Over Time')
        self.plt.xlabel('Time')
        self.plt.ylabel(self.item_name)
        self.plt.xticks(rotation=45)
        self.plt.grid(True, alpha=0.3)
        self.plt.legend()
        self.plt.tight_layout()
        
        return {"status": "Graph created successfully", "data_points": len(self.timestamps)}
