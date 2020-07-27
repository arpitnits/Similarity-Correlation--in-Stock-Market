from ResourceManager import ResourceManager

class StockGateway:
    'Class to fetch stock data from CSV or APIs'
    resource_manager = ResourceManager()


    def fetch_from_csv(self, path=''):
        return self.resource_manager.read_from_csv(path)