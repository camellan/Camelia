# -*- coding: utf-8 -*-
import http.client, re, time
conn = http.client.HTTPSConnection("p.ya.ru")
conn.request("GET", "/togliatti")
response = conn.getresponse()
str_resp = response.read().decode("utf-8")
today_forecast = re.search(r'<div class="today-forecast">(.+?)<\/div>',str_resp).group(1)
temp_current = re.search(r'{"temp-current":{"temp":(.*)}}\'>(.+?)</span> ',str_resp).group(2)
print(today_forecast+",", temp_current+"˚C")
#my_file = open("/home/camellan/.weather/response", 'w')
#my_file.write(str_resp)
#my_file.close()
