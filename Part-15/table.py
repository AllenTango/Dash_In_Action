import dash_table
import dash_html_components as html
import api

def StockTable():
    return html.Div([
        dash_table.DataTable(
            id="table",
            data=api.choose_industry("制造业"),
            columns=[{"name": "股票代码", "id": "公司代码"},
                     {"name": "名称", "id": "公司简称"},
                     {"name": "地区", "id": "城     市"},
                     {"name": "市盈率(昨)", "id": "PERation"},
                     {"name": "换手率(昨)/%", "id": "TurnoverRate"}])
        ], className="mt-3 mb-3")