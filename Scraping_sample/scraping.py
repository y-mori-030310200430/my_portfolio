from bs4 import BeautifulSoup as bs4
import requests
from lxml import html
import pandas as pd

def scraping_RCL():
  url = "https://recruit-holdings.com/ja/newsroom/"
  res = requests.get(url)

  soup = bs4(res.text, "html.parser")

  lxml_data = html.fromstring(str(soup))
  article_list = lxml_data.xpath("//div[@id='notifications']//p[contains(@class, 'C102_Text')]")

  article_columns = dict(date = [], articleName = [])
  columns = ["date", "articleName"]
  df_article = pd.DataFrame(article_columns)
  index = range(len(article_list))[0::2]

  for i in index:
    article_set = [[article_list[i].text, article_list[i+1].text]]
    df_article_set = pd.DataFrame(data=article_set, columns=columns)
    df_article = pd.concat([df_article, df_article_set], ignore_index=True)
  df_article["date"] = pd.to_datetime(df_article["date"], format="%Y年%m月%d日")

  target_article = df_article.loc[df_article["date"]==pd.to_datetime("20250303")]
  return target_article