from sys import platform as sys_pf

import plotly as py
import plotly.graph_objs as go

from Alice import Alice
from StockGateway import StockGateway

if sys_pf == 'darwin':
    import matplotlib
    matplotlib.use("TkAgg")

# Init constants
crm_stock_name = 'CRM'
spot_stock_name = 'SPOT'
aapl_stock_name = 'AAPL'
riot_stock_name = 'RIOT'

crm_path = '../resources/CRM.csv'
spot_path = '../resources/SPOT.csv'
aapl_path = '../resources/AAPL.csv'
riot_path = '../resources/RIOT.csv'

stocks = [
    crm_stock_name,
    spot_stock_name,
    aapl_stock_name,
    riot_stock_name
]

paths = {
    crm_stock_name: crm_path,
    spot_stock_name: spot_path,
    aapl_stock_name: aapl_path,
    riot_stock_name: riot_path
}


def main():
    alice = Alice()
    stock_gateway = StockGateway()

    # Load stocks
    load_stocks(alice, stock_gateway)

    draw_stocks(alice)


def draw_stocks(alice):
    data = []
    normalized_data = []
    distance_data = []
    r2_distance_data = []
    normalized_r2_distance_data = []
    i = 1
    for stock in stocks:
        df = alice.get_company(stock)
        from sklearn.preprocessing import MinMaxScaler
        y_stock = MinMaxScaler().fit_transform(df['close'].values.reshape(-1, 1))

        data.append(
            go.Scatter(
                x=df['date'],
                y=df['close'],
                name=stock
            )
        )
        normalized_data.append(
            go.Scatter(
                x=df['date'],
                y=y_stock.reshape(y_stock.shape[0]),
                name=stock
            )
        )

        distance_data.append(
            go.Bar(
                x=(0, i),
                y=(0, alice.compare(crm_stock_name, stock)[0][0]),
                name='CRM to ' + stock
            )
        )
        r2_distance_data.append(
            go.Bar(
                x=(0, i),
                y=(0, alice.compare(crm_stock_name, stock, strategy='r2-score')),
                name='CRM to ' + stock
            )
        )
        normalized_r2_distance_data.append(
            go.Bar(
                x=(0, i),
                y=(0, alice.compare(crm_stock_name, stock, strategy='normalized-r2-score')),
                name='CRM to ' + stock
            )
        )
        i = i + 1

    stocks_layout = go.Layout(title='Stocks')
    normalized_stocks_layout = go.Layout(title='Normalized Stocks')
    cosine_layout = go.Layout(title='Cosine distance')
    r2score_layout = go.Layout(title='R2 score')
    normalized_r2score_layout = go.Layout(title='Normalized R2 score')

    stocks_fig = go.Figure(data=data, layout=stocks_layout)
    normalized_stocks_fig = go.Figure(data=normalized_data, layout=normalized_stocks_layout)
    cosine_fig = go.Figure(data=distance_data, layout=cosine_layout)
    r2score_fig = go.Figure(data=r2_distance_data, layout=r2score_layout)
    normalized_r2score_fig = go.Figure(data=normalized_r2_distance_data, layout=normalized_r2score_layout)

    url = py.offline.plot(stocks_fig, filename='stocks.html')
    url5 = py.offline.plot(normalized_stocks_fig, filename='normalized_stocks.html')
    url2 = py.offline.plot(cosine_fig, filename='pandas-line-naming-traces-distance.html')
    url3 = py.offline.plot(r2score_fig, filename='pandas-line-naming-traces-r2-distance.html')
    url4 = py.offline.plot(normalized_r2score_fig, filename='pandas-line-naming-traces-normalized-r2-distance.html')


    print("Chart in " + url)
    print("Chart in " + url2)
    print("Chart in " + url3)
    print("Chart in " + url4)
    print("Chart in " + url5)


def load_stocks(alice, stock_gateway):
    for stock in stocks:
        load_stock(alice, paths[stock], stock, stock_gateway)


def load_stock(alice, stock_path, stock_name, stock_gateway):
    alice.add_company(stock_name, stock_gateway.fetch_from_csv(path=stock_path))


if __name__ == '__main__':
    main()
