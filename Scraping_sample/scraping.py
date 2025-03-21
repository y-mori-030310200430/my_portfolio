from bs4 import BeautifulSoup as bs4
from playwright.sync_api import sync_playwright
from lxml import html
import pandas as pd
import datetime

def scraping_RCL():
  url = "https://recruit-holdings.com/ja/newsroom/"

  with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()
    page.goto(url, wait_until="networkidle")
    res = page.content()
    browser.close()

  soup = bs4(res, "html.parser")
  lxml_data = html.fromstring(str(soup))
  article_list = lxml_data.xpath("//div[contains(@id, 'news')]//p[contains(@class, 'C102_Text')]")
  article_url_list = lxml_data.xpath("//div[contains(@id, 'news')]//a/@href")

  article_columns = dict(date = [], articleName = [], url = [])
  columns = ["date", "articleName", "url"]
  df_article = pd.DataFrame(article_columns)
  index = range(len(article_list))[0::2]

  for i in index:
    article_set = [[article_list[i].text, article_list[i+1].text, f"https://recruit-holdings.com{article_url_list[i]}"]]
    df_article_set = pd.DataFrame(data=article_set, columns=columns)
    df_article = pd.concat([df_article, df_article_set], ignore_index=True)
  df_article["date"] = pd.to_datetime(df_article["date"], format="%Y年%m月%d日")

  target_article = df_article.loc[df_article["date"]==pd.to_datetime(datetime.datetime.now().strftime("%Y-%m-%d"))]
  # テスト用
  # target_article = df_article.loc[df_article["date"]==pd.to_datetime(datetime.date(2025, 3, 12).strftime("%Y-%m-%d"))]
  return target_article