# 输入一个url，利用Selenium访问并截图保存在本地，name为文件名，通过改变(0, 0, 1000, 300)来改变截图的大小
# getHtmlScreenshot('http://www.baidu.com','111')
def getHtmlScreenshot(url, name):
    potoName = name + '.png'

    chrome_options = webdriver.ChromeOptions()  # 初始化 Chrome 浏览器的设置
    chrome_options.add_argument("--headless")  # 无头模式（不显示浏览器窗口）
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(options=chrome_options)  # 创建 WebDriver 对象
    driver.get(url)       # 打开网页
    driver.maximize_window()       # 最大化浏览器窗口
    time.sleep(2)  # 等待几秒
    driver.save_screenshot(potoName)    # 保存图片到本地
    driver.quit()    # 关闭浏览器
    image = Image.open(potoName)     # 打开图片
    cropped_image = image.crop((0, 0, 1000, 300))  # 裁剪图片  前两个数是第一个坐标点为新图片的左上角，后两个数为第二个坐标为新图片的右下角，两个数前者为x坐标，后者为y坐标
    cropped_image.save('222.png')    # 保存裁剪后的图片
