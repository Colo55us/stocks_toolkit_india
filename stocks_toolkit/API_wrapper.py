class NSEAPIs:
    def __init__(self):
        # self.stock_data = "https://www.nseindia.com/api/quote-equity?symbol={}"
        # self.historical_stock_data = "https://www.nseindia.com/api/historical/cm/equity?symbol={}&series=[%22EQ%22]&from={}&to={}"
        self.stock_data = "https://www1.nseindia.com/products/dynaContent/common/productsSymbolMapping.jsp?symbol={}&segmentLink=3&symbolCount2&series=EQ&dateRange=+&fromDate={}&toDate={}&dataType=PRICEVOLUMEDELIVERABLE"
        self.stock_header = {
            "authority": "www.nseindia.com",
            "method": "GET",
            "scheme": "https",
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            "accept-encoding": "gzip, deflate, br",
            "accept-language": "en-US,en;q=0.9",
            "sec-ch-ua": '"Chromium";v="94", "Google Chrome";v="94", ";Not A Brand";v="99"',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": '"Windows"',
            "sec-fetch-dest": "document",
            "sec-fetch-mode": "navigate",
            "sec-fetch-site": "none",
            "sec-fetch-user": "?1",
            "upgrade-insecure-requests": "1",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36",
            "Referrer Policy": "strict-origin-when-cross-origin",
            "Remote Address": "23.57.254.133:443",
            "Request Method": "GET"
        }

        self.header = {
            "Host": "www1.nseindia.com",
            "User-Agent" : "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:84.0) Gecko/20100101 Firefox/84.0",
            "Accept": "*/*",
            "Accept-Language": "en-US,en;q=0.5",
            "Accept-Encoding": "gzip, deflate, br",
            "X-Requested-With": "XMLHttpRequest",
            "Referer": "https://www1.nseindia.com/products/content/equities/equities/eq_security.htm",
            "Access-Control-Allow-Origin" : "*",
            "Access-Control-Allow-Methods" : "GET,POST,PUT,DELETE,OPTIONS",
            "Access-Control-Allow-Headers": "Content-Type, Access-Control-Allow-Headers, Authorization, X-Requested-With",
            'Content-Type' : 'application/x-www-form-urlencoded; charset=UTF-8'
        }