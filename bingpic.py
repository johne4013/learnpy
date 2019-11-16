# 下载并存储必应每日壁纸到指定位置

import time
import os
import urllib.request
import requests

# 保存图片到磁盘文件夹dirname中
def save_img(img_url, dirname):
    try:
        # 文件夹不存在就创建
        if not os.path.exists(dirname):
            print ('    提示：文件夹', dirname, '不存在，重新建立', '\n')
            os.makedirs(dirname)
        # 用日期命名图片文件名，包括后缀
        basename = time.strftime("%Y-%m-%d", time.localtime()) + ".jpg"
        # 拼接目录与文件名，得到图片路径
        filepath = os.path.join(dirname, basename)
        # 下载图片，并保存到文件夹中
        urllib.request.urlretrieve(img_url,filepath)
    except IOError as e:
        print('    错误：文件操作失败', e, '\n')
    except Exception as e:
        print('    错误：', e, '\n')
    else:
        print("    保存", filepath, "成功！", '\n')

    return filepath

# 请求网页，跳转到最终 img 地址
def get_img_url(raw_img_url = "https://area.sinaapp.com/bingImg/"):
    try:
        # 得到图片文件的网址
        r = requests.get(raw_img_url)
        img_url = r.url
    except Exception as e:
        print('    错误：', e, '\n')
        return False
    else:
        return img_url

def main():
    dirname = "D:\\壁纸\\Bing"              # 图片要被保存在的位置
    print("壁纸将被保存在：", dirname, '\n')

    img_url = get_img_url()
    if img_url != False:
        print('图片地址为：', img_url, '\n')
        filepath = save_img(img_url, dirname)   # 图片文件的的路径

    os.system("pause")

main()