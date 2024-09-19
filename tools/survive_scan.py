# 存活扫描，输入一个url，返回存活状态
# survive_scan("http://www.baidu.com")
def survive_scan(url):
    alive_status_codes = [200, 201, 202, 203, 204, 205, 206, 207, 208, 226]  # 存活状态码
    try:
        # 发起GET请求
        requests.packages.urllib3.disable_warnings()
        response = requests.get(url=url, headers=random_header(), timeout=10, verify=False)  # 设置超时6秒

        # 检查状态码
        if response.status_code in alive_status_codes:
            print(f'{url} 存活')
            return True
        else:
            print(f'{url} 不存活')
            return False
    except requests.exceptions.RequestException as e:
        print(f'{url} 检查报错: {e}')
        return False
