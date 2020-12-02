import re
import akshare as ak

sz_df = ak.stock_info_sz_name_code("上市公司列表")
# sh_df = ak.stock_info_sh_name_code("主板A股")

industry_tmp = list(set(sz_df["所属行业"]))
industry_list = [re.sub(r"[A-z]| ", '', s) for s in industry_tmp]