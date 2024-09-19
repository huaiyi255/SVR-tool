# 测试代理是否可用  输入格式：proxy = {'http': 'http://47.122.65.254:8080', 'https': 'http://47.122.65.254:8080'}
def proxy_test(proxy):
    try:
        testurl = "http://example.com"
        res = requests.get(testurl, timeout=10, proxies=proxy, verify=False, headers=random_header())
        # print(res.status_code)    # 发起请求,返回响应码
        if res.status_code == 200:
            print(f"[+] {proxy['http']} 代理可用，GET example.com 状态码为：{str(res.status_code)}。")
        return True
    except Exception as e:
        print(f"{proxy} 代理不可用")
        return False
