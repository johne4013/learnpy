import urllib.request
import re

stock_CodeUrl = 'http://quote.eastmoney.com/stocklist.html'


# 获取股票代码列表
def urlTolist(url):
    allCodeList = []

    html = urllib.request.urlopen(url).read()

    html = html.decode('gbk')

    s = r'<li><a target="_blank" href="http://quote.eastmoney.com/\S\S(.*?).html">'

    pat = re.compile(s)

    code = pat.findall(html)

    for item in code:

        if item[0] == '6' or item[0] == '3' or item[0] == '0':
            allCodeList.append(item)

    return allCodeList


allCodelist = urlTolist(stock_CodeUrl)

for code in allCodelist:

    print('正在获取%s股票数据...' % code)

    if code[0] == '6':

        url = 'http://quotes.money.163.com/service/chddata.html?code=0' + code + \
              '&end=20180302&fields=TCLOSE;HIGH;LOW;TOPEN;LCLOSE;CHG;PCHG;TURNOVER;VOTURNOVER;VATURNOVER;TCAP;MCAP'

    else:

        url = 'http://quotes.money.163.com/service/chddata.html?code=1' + code + \
              '&end=20180302&fields=TCLOSE;HIGH;LOW;TOPEN;LCLOSE;CHG;PCHG;TURNOVER;VOTURNOVER;VATURNOVER;TCAP;MCAP'

    urllib.request.urlretrieve(url, 'D:\\python\\demo\\' + code + '.csv')