# fofa查询
def fofa_search(key, searchquery):
    fafa_search_data = []
    qbase64 = base64.b64encode(searchquery.encode('utf-8')).decode('utf-8')
    url = "https://fofa.info/api/v1/search/all?&key=" + key + "&qbase64=" + qbase64 + "&fields=ip,port,link,title,icp,product" + "&size=10000"
    req = requests.get(url=url, verify=True, timeout=10).text
    data = json.loads(req)
    for i in data['results']:
        # print(f'ip：{i[0]}，端口：{i[1]}，资产链接：{i[2]}，标题：{i[3]}，icp备案号：{i[4]}，指纹：{i[5]}')
        if survive_scan(i[2]):
            fafa_search_data.append(i)
    return fafa_search_data
