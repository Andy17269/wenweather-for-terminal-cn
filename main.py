import os

import requests
import time

amap_key = '1e4fce5cc58bc22229fe6cf0814074f1'
qw_key = '781742beafdc4ddc8e0d7a3e46fd113c'

try:
    config_info_get = requests.get('https://assets.wenlei.club/wenweather/config.json')
    config_info = config_info_get.json()

    status = config_info.get('status')
    mode = config_info.get('mode')
    wen_name = config_info.get('name')
    wen_cloud_name = config_info.get('cloud')
    version = config_info.get('version')
    versiontime = config_info.get('versiontime')
except:
    print('无法连接网络，或服务器正在维护')

print('欢迎使用 {} For Terminal\n'.format(wen_name))

time.sleep(0.6)

try:
    ageo_get = requests.get('https://restapi.amap.com/v3/ip?key={}'.format(amap_key))
    ageo = ageo_get.json()
    geo_city = ageo.get('city')
    adcode = ageo.get('adcode')
    wa_get = requests.get('https://restapi.amap.com/v3/weather/weatherInfo?key=1e4fce5cc58bc22229fe6cf0814074f1&extensions=base&city={}'.format(adcode))
    wa = wa_get.json()
    ageo_city = wa.get('lives')[0].get("city")
    weather = wa.get('lives')[0].get("weather")
    temperature = wa.get('lives')[0].get("temperature")
    windpower = wa.get('lives')[0].get("windpower")
    winddirection = wa.get('lives')[0].get("winddirection")
    humidity = wa.get('lives')[0].get("humidity")
    reporttime = wa.get('lives')[0].get("reporttime")
except:
    print('无法连接至天气数据服务器')

print('功能列表：\n1.查询所在地天气\n2.查询其它城市天气\n3.退出 {}\n4.关于 {}\n'.format(wen_name, wen_name))
choose = input('')
if choose == '1':
    print('您来自 {}'.format(geo_city))
    print('\033[0;32;40m目前\033[0m', ageo_city, '的天气为', weather, '，温度', temperature, '℃，', winddirection,
          windpower, '级风，空气湿度', humidity, '，此数据最后更新于', reporttime, '\n')
    print('查询完成')
    print("按下任意键以退出程序")
    input()
elif choose == '2':
    print('请输入此城市的Adcode码（Adcode）：')
    choose_city = input('')

    geo_get_user = requests.get('https://restapi.amap.com/v3/weather/weatherInfo?key=1e4fce5cc58bc22229fe6cf0814074f1&city={}'.format(choose_city))
    geo_user = geo_get_user.json()
    uageo_city = geo_user.get('lives')[0].get("city")
    uweather = geo_user.get('lives')[0].get("weather")
    utemperature = geo_user.get('lives')[0].get("temperature")
    uwindpower = geo_user.get('lives')[0].get("windpower")
    uwinddirection = geo_user.get('lives')[0].get("winddirection")
    uhumidity = geo_user.get('lives')[0].get("humidity")
    ureporttime = geo_user.get('lives')[0].get("reporttime")
    print('\033[0;32;40m目前\033[0m', uageo_city, '的天气为', uweather, '，温度', utemperature, '℃，', uwinddirection,
          uwindpower, '级风，空气湿度', uhumidity, '，此数据最后更新于', ureporttime, '\n')
    print("按下任意键以退出程序")
    input()
elif choose == '3':
    quit()
elif choose == '4':
    print(
        '\033[1mWenWeather  V0.9.4     CloudVersion: {}.{}\033[0m\nBy \033[0;32;40mAndy17269\033[0m\nGithub@Andy17269\nBilibili@干净T松鼠\nWenCenter Studio@2023 https://wenlei.club\n由\033[0;32;40m高德地图\033[0m提供天气数据。'.format(
            versiontime, version))
    print("按下任意键以退出程序")
    input()
elif choose == '7890':
    print('+ -- + -- + -- + -- +')
    print('____________________________________________________')
    print('\nDeveloper Tools 已启动')
    print('____________________________________________________')
    print('CityWeather: ',wa)
    print('CloudConfig: ',config_info)
    print('Geo: ',ageo)
    print("按下任意键以退出程序")
    input()
else:
    print('请选择正确的功能选项，再次进入后重试。')
    print("按下任意键以退出程序")
    input()
