from scrapyd_api import ScrapydAPI
scrapyd = ScrapydAPI('http://localhost:6800')
scrapyd.schedule('lab6', 'hotline')
scrapyd.schedule('lab6', 'rozetka')