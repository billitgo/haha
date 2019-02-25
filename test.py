import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
account_dict = {'000001.SZ':10000,'300033.SZ':20000,'600519.SH':50000}
account_cash = 100000
accountdf = pd.DataFrame(account_dict,index =['持仓市值']).T
xxx=accountdf['valuation_symbol'].accountdf.index
print(xxx)
accountdf['industry'] = accountdf['valuation_symbol'].apply(lambda x:get_symbol_industry(x, date).s_industryid1 if get_symbol_industry(x, date) != None else np.nan)

 #基准权重
    q = query(valuation.symbol,
              valuation.market_cap
             ).filter(valuation.symbol.in_(hs300stock)) 
    df = get_fundamentals(q, date = date) #输入时间
    df['industry'] = df['valuation_symbol'].apply(lambda x:get_symbol_industry(x, date).s_industryid1 if get_symbol_industry(x, date) != None else np.nan)
    allmc = df['valuation_market_cap'].sum()
    weight_bench_i_dict={}
    weight_bench_i=[]
    for s in industry_list:
        q = df[df['industry']==s]
        mc = q['valuation_market_cap'].sum()/allmc
        weight_bench_i_dict[s]=mc
        weight_bench_i.append(mc)