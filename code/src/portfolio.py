class Portfolio(object):

    def __init__(self, assets):
        self.assets = assets

    def set_weights(self, weights):
        self.weights = weights

    def get_return(self, returns, date):
        return sum(
            self.weights[asset] * returns[asset][date]
            for asset in self.assets
        )

    def get_returns(self, returns):
        return sum(
            self.weights[asset] * returns[asset]
            for asset in self.assets
        )
