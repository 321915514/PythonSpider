import requests
from lxml import etree
import json
from bs4 import BeautifulSoup
import pandas as pd
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/76.0.3809.100 Safari/537.36 '
}

cities = []
pros = []


def append_list():
    citys = []
    beijing = []
    tianjing = []
    hebei = []
    shanxi = []
    nmg = []
    heilongjiang = []
    jilin = []
    liaoning = []
    shanghai = []
    anhui = []
    jiangsu = []
    shandong = []
    zhejiang = []
    fujian = []
    jiangxi = []
    hubei = []
    hunan = []
    henan = []
    guangxi = []
    guangdong = []
    hainan = []
    shannxi = []
    gansu = []
    xinjiang = []
    qinghai = []
    ningxia = []
    sichuan = []
    chongqing = []
    guizhou = []
    yunnan = []
    xizang = []
    for i in range(0, 17):
        beijing.append(cities[i])
    for i in range(17, 34):
        tianjing.append(cities[i])
    for i in range(34,46):
        hebei.append(cities[i])
    for i in range(46, 57):
        shanxi.append(cities[i])
    for i in range(57, 69):
        nmg.append(cities[i])

    for i in range(69, 82):
        heilongjiang.append(cities[i])

    for i in range(82, 91):
        jilin.append(cities[i])

    for i in range(91, 105):
        liaoning.append(cities[i])
    for i in range(105, 122):
        shanghai.append(cities[i])

    for i in range(122, 138):
        anhui.append(cities[i])

    for i in range(138, 151):
        jiangsu.append(cities[i])

    for i in range(151, 168):
        shandong.append(cities[i])

    for i in range(168, 179):
        zhejiang.append(cities[i])

    for i in range(191, 189):
        fujian.append(cities[i])

    for i in range(189, 200):
        jiangxi.append(cities[i])

    for i in range(200, 217):
        hubei.append(cities[i])

    for i in range(217, 231):
        hunan.append(cities[i])
    for i in range(231, 249):
        henan.append(cities[i])
    for i in range(249, 263):
        guangxi.append(cities[i])
    for i in range(263, 284):
        guangdong.append(cities[i])
    for i in range(284, 305):
        hainan.append(cities[i])
    for i in range(305, 316):
        shannxi.append(cities[i])
    for i in range(316, 330):
        gansu.append(cities[i])
    for i in range(330, 352):
        xinjiang.append(cities[i])
    for i in range(352, 360):
        qinghai.append(cities[i])
    for i in range(360, 365):
        ningxia.append(cities[i])
    for i in range(365, 386):
        sichuan.append(cities[i])
    for i in range(386, 425):
        chongqing.append(cities[i])
    for i in range(425, 434):
        guizhou.append(cities[i])
    for i in range(434, 450):
        yunnan.append(cities[i])
    for i in range(450, 457):
        xizang.append(cities[i])
    # for i in range(457, 458):
    #     xianggang.append(cities[i])
    # for i in range(458, 459):
    #     aomen.append(cities[i])
    # for i in range(459, 462):
    #     taiwan.append(cities[i])
    hubei[9] = '恩施州'
    beijing[14] = '平谷区'
    shanghai[5] = '浦东'
    chongqing[11] = '万州区'
    chongqing[13] = '城口县'
    chongqing[14] = '云阳县'
    chongqing[15] = '巫溪县'
    chongqing[16] = '奉节县'
    chongqing[20] = '梁平区'
    chongqing[-1] = '开州区'
    chongqing[19] = '垫江县'
    chongqing[8] = '长寿区'
    chongqing[12] = '涪陵区'
    chongqing[9] = '黔江区'
    chongqing[-8] = '酉阳县'
    chongqing[-6] = '秀山县'
    chongqing[-10] = '彭水县'
    chongqing[-11] = '武隆区'
    chongqing[5] = '渝北区'
    chongqing[4] = '江津区'
    chongqing[-9] = '綦江区'
    chongqing[3] = '南川区'
    chongqing[1] = '永川区'
    chongqing[24] = '荣昌区'
    chongqing[23] = '大足区'
    chongqing[25] = '铜梁区'
    chongqing[18] = '潼南区'
    chongqing[2] = '合川区'
    tianjing[-4] = '蓟州区'
    tianjing[2] = '宝坻区'
    tianjing[1] = '武清区'
    tianjing[6] = '宁河区'
    tianjing[5] = '北辰区'
    tianjing[3] = '东丽区'
    tianjing[9] = '津南区'
    tianjing[4] = '西青区'
    tianjing[8] = '静海区'
    nmg[-2] = '兴安盟乌兰浩特'
    jilin[-1] = '白山市'
    liaoning[3] = '抚顺市'
    shandong[-6] = '东营市'
    hunan[-1] = '湘西自治州'
    henan[-1] = '济源示范区'
    hainan[3] = '临高县'
    hainan[4] = '澄迈县'
    hainan[5] = '儋州县'
    hainan[6] = '昌江县'
    hainan[8] = '琼中县'
    hainan[9] = '定安县'
    hainan[-6] = '陵水县'
    hainan[10] = '屯昌县'
    hainan[7] = '白沙黎族自治县'
    hainan[-4] = '五指山市'
    gansu[-7] = '酒泉市'
    gansu[-3] = '甘南州'
    gansu[-1] = '嘉峪关市'
    xinjiang[2] = '石河子市'
    xinjiang[-11] = '哈密市'
    xinjiang[3] = '昌吉州'
    xinjiang[-5] = '五家渠市'
    xinjiang[-9] = '阿勒泰地区'
    xinjiang[-3] = '北屯市'
    xinjiang[10] = '塔城地区'
    xinjiang[-7] = '博尔塔拉蒙古自治州'
    xinjiang[9] = '伊犁州'
    xinjiang[-1] = '可克达拉市'
    xinjiang[5] = '巴音郭楞蒙古自治州'
    xinjiang[-4] = '铁门关市'
    xinjiang[-10] = '和田地区'
    xinjiang[8] = '喀什地区'
    xinjiang[6] = '阿拉尔市'
    xinjiang[-8] = '克孜勒苏柯尔克孜自治州'
    xinjiang[-6] = '图木舒克市'
    xinjiang[-5] = '五家渠市'
    qinghai[1] = '海东市'
    qinghai[2] = '黄南藏族自治州'
    qinghai[3] = '海南藏族自治州'
    qinghai[-2] = '海西蒙古族藏族自治州'
    qinghai[-3] = '玉树藏族自治州'
    qinghai[-1] = '海北州'
    qinghai[-4] = '果洛藏族自治州'
    chongqing[3] = '南川区'
    chongqing[7] = '巴南区'
    chongqing[10] = '渝中区'
    chongqing[17] = '巫山县'
    chongqing[-17] = '石柱县'
    chongqing[-12] = '丰都县'
    chongqing[-13] = '璧山区'
    chongqing[-7] = '大渡口区'
    chongqing[-5] = '江北区'
    chongqing[-4] = '沙坪坝区'
    chongqing[-3] = '九龙坡区'
    chongqing[-2] = '南岸区'
    guizhou[3] = '黔南州'
    guizhou[-1] = '黔西南州'
    yunnan[4] = '保山市'
    yunnan[5] = '文山州'
    yunnan[7] = '楚雄州'
    yunnan[-4] = '迪庆藏族自治州'
    yunnan[-5] = '怒江傈僳族自治州'
    yunnan[-2] = '德宏州'
    yunnan[-1] = '西双版纳州'
    xizang[0] = '拉萨市'
    xizang[1] = '日喀则市'
    xizang[2] = '山南市'
    xizang[3] = '林芝市'
    xizang[-3] = '昌都市'
    xizang[-2] = '那曲地区'
    xizang[-1] = '阿里地区'
    citys.append(beijing)
    citys.append(tianjing)
    citys.append(hebei)
    citys.append(shanxi)
    citys.append(nmg)
    citys.append(heilongjiang)
    citys.append(jilin)
    citys.append(liaoning)
    citys.append(shanghai)
    citys.append(anhui)
    citys.append(jiangsu)
    citys.append(shandong)
    citys.append(zhejiang)
    citys.append(fujian)
    citys.append(jiangxi)
    citys.append(hubei)
    citys.append(hunan)
    citys.append(henan)
    citys.append(guangxi)
    citys.append(guangdong)
    citys.append(hainan)
    citys.append(shannxi)
    citys.append(gansu)
    citys.append(xinjiang)
    citys.append(qinghai)
    citys.append(ningxia)
    citys.append(sichuan)
    citys.append(chongqing)
    citys.append(guizhou)
    citys.append(yunnan)
    citys.append(xizang)
    # citys.append(xianggang)
    # citys.append(aomen)
    # citys.append(taiwan)
    # print(beijing)
    # print(tianjing)
    # print(hebei)
    # print(nmg)
    # print(hubei)
    # print(shanghai)
    # print(xinjiang)
    # print(qinghai)
    # print(ningxia)
    # print(sichuan)
    # print(chongqing)
    # print('*'*50)
    return citys


def get_province_city():
    page = ['hb', 'db', 'hd', 'hz', 'hn', 'xb', 'xn']
    for url in page:
        url = 'http://www.weather.com.cn/textFC/' + url + '.shtml'
        parse_page(url)


def parse_page(url):
    res = requests.get(url, headers=headers)
    html = res.content.decode('utf-8')
    soup = BeautifulSoup(html, 'html5lib')
    div = soup.find_all('div', attrs={'class': 'conMidtab'})[0]
    tables = div.find_all('table')
    text = etree.HTML(str(tables))
    for pro in text.xpath("//td[@class='rowsPan']/a/text()"):
        pros.append(pro)
    for city_ in text.xpath("//td[@width='83']/a/text()"):
        cities.append(city_)
    # for i in pros:
    #     for j in citys:
    # pc = {
    #     'province': province,
    #     'city': city
    # }
    # pcs.append(pc)
    # print(pcs)
    # soup = BeautifulSoup(html, 'html5lib')
    # div = soup.find_all('div', attrs={'class': 'conMidtab'})[0]
    # tables = div.find_all('table')
    # for table in tables:
    #     trs = table.find_all('tr')[2:]
    #     for tr in trs:
    #         tds = tr.find_all('td')
    #         city_td = tds[1]
    #         pro_teg = tds[0]
    #         pro = list(pro_teg.stripped_strings)[0]
    #         city = list(city_td.stripped_strings)[0]
    #         print(pro)
    #         print('*'*30)
    #         print(city)
    #         citys.append(city)


# response = requests.post(url=url, data=data, headers=headers)

# json_obj = json.loads(response.text)

# for i in json_obj['data']:

json_objs = []


def get_province():
    for province in pros:
        url = 'https://api.inews.qq.com/newsqa/v1/query/pubished/daily/list'
        data = {
            'province': province
        }
        response = requests.post(url=url, headers=headers, data=data)
        json_obj = json.loads(response.text)
        for i in json_obj['data']:
            json_objs.append(i)
    # columns = ['date', 'country', 'province', 'confirm', 'dead', 'heal', 'confirm_add', 'newHeal', 'newDead']
    # pf = pd.DataFrame(list(json_objs), columns=columns)
    # columns_map = {
    #             'date': '日期',
    #             'country': '国家',
    #             'province': '省份',
    #             'confirm': '确诊人数',
    #             'dead': '死亡人数',
    #             'heal': '治愈人数',
    #             'confirm_add': '新增',
    #             'newHeal': '新治愈',
    #             'newDead': '新死亡'
    #     }
    # pf.rename(columns=columns_map, inplace=True)
    # pf.to_excel('D:/省份疫情信息.xlsx', encoding='utf-8', index=False)


def get_city():
    city_list = []
    for index, province in enumerate(pros):
        for city in append_list()[index]:
            url = 'https://api.inews.qq.com/newsqa/v1/query/pubished/daily/list'
            data = {
                'province': province,
                'city': city
            }
            response = requests.post(url=url, headers=headers, data=data)
            json_obj = json.loads(response.text)
            if json_obj['data'] is not None:
                for i in json_obj['data']:
                    city_list.append(i)
    pf = pd.DataFrame(list(city_list))
    columns_map = {
            'date': '日期',
            'city': '城市',
            'confirm': '确诊人数',
            'dead': '死亡人数',
            'heal': '治愈人数',
            'suspect': '怀疑患者',
            'confirm_add': '新增患者'
    }
    pf.rename(columns=columns_map, inplace=True)
    pf.to_excel('D:/地级市疫情信息.xlsx', encoding='utf-8', index=False)


def get_gat():
    gat = ['香港', '澳门', '台湾']
    for i in gat:
        url = 'https://api.inews.qq.com/newsqa/v1/query/pubished/daily/list'
        data = {
            'province': i,
        }
        response = requests.post(url=url, headers=headers, data=data)
        json_obj = json.loads(response.text)
        for j in json_obj['data']:
            json_objs.append(j)
    columns = ['date', 'country', 'province', 'confirm', 'dead', 'heal', 'confirm_add', 'newHeal', 'newDead']
    pf = pd.DataFrame(list(json_objs), columns=columns)
    columns_map = {
        'date': '日期',
        'country': '国家',
        'city': '省',
        'confirm': '确诊人数',
        'dead': '死亡人数',
        'heal': '治愈人数',
        'confirm_add': '新增患者',
        'newHeal': '新治愈',
        'newDead': '新死亡',
    }
    pf.rename(columns=columns_map, inplace=True)
    pf.to_excel('D:/省份疫情信息.xlsx', encoding='utf-8', index=False)


if __name__ == '__main__':
    get_province_city()
    get_province()
    #get_city()
    get_gat()
