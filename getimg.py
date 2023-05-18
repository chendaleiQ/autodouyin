import requests
from bs4 import BeautifulSoup
from PIL import Image, ImageDraw, ImageFont
from PIL import Image, ImageDraw, ImageFont
import textwrap
import os
def draw_text_on_image(text:str, image_size:tuple=(500,1200), font_family:str='Hiragino Sans GB.ttc', font_size:int=30, background_color:str='white', text_color:str='black', filename:str='hello_world.png',folder:str='output'):
    """
    给定一段文本，生成一张带有文本的图片

    Args:
        text (str): 要在图片上显示的文本
        image_size (tuple, optional): 图片大小. Defaults to (200,50).
        font_family (str, optional): 字体名称. Defaults to 'Helvetica'.
        font_size (int, optional): 字号. Defaults to 30.
        background_color (str, optional): 背景颜色. Defaults to 'white'.
        text_color (str, optional): 文本颜色. Defaults to 'black'.
        filename (str, optional): 保存文件名. Defaults to 'hello_world.png'.

    Returns:
        None
    """
    # 获取输出路径
    if not os.path.exists(folder):
        os.makedirs(folder)
    filename = os.path.join(folder, f'{text}.png')

    # 定义图像大小和背景颜色
    image = Image.new('RGB', image_size, color=background_color)

    # 在图像上绘制文本
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype(font_family, font_size) # 设置字体和字号

    # 计算文本区域的大小
    lines = textwrap.wrap(text, width=int(image_size[0] / font_size))
    max_width = 0
    total_height = 0
    for line in lines:
        line_width, line_height = font.getsize(line)
        max_width = max(max_width, line_width)
        total_height += line_height

    # 计算文本起始位置
    x = (image.width - max_width) / 2 # 计算文本横坐标
    y = (image.height - total_height) / 2 # 计算文本纵坐标

    # 绘制文本
    for line in lines:
        line_width, line_height = font.getsize(line)
        draw.text((x, y), line, font=font, fill=text_color)
        y += line_height

    # 保存图像
    image.save(filename)

url = 'https://tophub.today/n/KqndgapoLl'
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36'
}
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, 'html.parser')

# 定位到新闻列表
news_list = soup.find_all('td', class_='al')
# 遍历获取每条新闻的标题和链接
if news_list is not None:
    for news_item in news_list:
        for news in news_item.find_all('a'):
            title = news.text.strip()
            link = news['href']
            draw_text_on_image(text=title,filename=title+'.png')
