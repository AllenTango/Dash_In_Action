import re
import akshare as ak
import pandas as pd

sz_df = ak.stock_info_sz_name_code("上市公司列表")
# sh_df = ak.stock_info_sh_name_code("主板A股")
stock_comment = ak.stock_em_comment()

industry_tmp = list(set(sz_df["所属行业"]))
industry_list = [re.sub(r"[A-z]| ", "", s) for s in industry_tmp]

def completion_stock_coke(stock_code):
    stock_code = str(stock_code)
    while len(stock_code) < 6:
        stock_code = "0" + stock_code
    return stock_code

def get_detail_info():
    sz_df["公司代码"] = sz_df["公司代码"].apply(completion_stock_coke)

    detail_df = pd.merge(sz_df, stock_comment, left_on="公司代码", right_on="Code", how="left")

    detail_df = detail_df[["公司代码", "公司简称", "城     市", "所属行业", "PERation", "TurnoverRate"]]

    detail_df.dropna(inplace=True) # 清洗 空市盈率、最新价、换手率
    detail_df.drop_duplicates(inplace=True)
    return detail_df

def choose_industry(industry_name):
    detail_df = get_detail_info()
    return detail_df[detail_df["所属行业"].str.contains(industry_name)].to_dict("records")


def get_60d_kline_data(s_code):
    df = ak.stock_zh_index_daily_tx(symbol=f"sz{s_code}")
    df.index = pd.to_datetime(df.index)
    df_60d = df[-60:]
    return df_60d