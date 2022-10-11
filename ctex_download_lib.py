"""Function to download the ancient chinese text from the ctext.org website.

Binxu Wang
Oct. 8th, 2022
"""

import re
import os
from os.path import join
import pickle as pkl
from bs4 import BeautifulSoup
import requests
from easydict import EasyDict as edict
from tqdm import tqdm


def find_chap_urls(bookname, book_url=None):
  """Find the chapter urls for a given book."""
  if book_url is None:
    book_url = f"https://ctext.org/{bookname}/zhs?en=on"
  toc = requests.get(book_url)
  toc_soup = BeautifulSoup(toc.text, 'html.parser')
  chap_urls = []
  for link in toc_soup.find_all('a'):
    href = link.get('href')
    if f"{bookname}/" in href and "zhs?en=on" in href:
      # print(href)
      chap_urls.append(href)
  chap_urls_uniq = list(dict.fromkeys(chap_urls))
  print("\n".join(chap_urls_uniq))
  return chap_urls_uniq, toc_soup


def download_book_htmls(bookname, chap_urls: list):
  """Download the text htmls for a given book.

  Args:
    bookname: the name of the book
    chap_urls: the chapter urls for the book, list
  """
  os.makedirs(join("ctext", bookname), exist_ok=True)
  for urlpart in tqdm(chap_urls):
    url = f"https://ctext.org/{urlpart}"
    parts = urlpart.split("/")
    if not "zhs?en=on" in parts[-1]:
      continue
    if len(parts) == 3:
      bookname, chapter = parts[:-1]
    elif len(parts) == 2:
      chapter = bookname
    else:
      raise Exception
    if os.path.exists(f'ctext/{bookname}/{chapter}.html'):
      continue
    r = requests.get(url)
    with open(f'ctext/{bookname}/{chapter}.html', 'w') as f:
      f.write(r.text)


def parse_saved_htmls(bookname, chap_urls):
  """Parse the saved htmls for a given book.
  """
  # parse html
  chn_text_pool = []
  eng_text_pool = []
  valid_urls = []
  for urlpart in chap_urls:
    parts = urlpart.split("/")
    if len(parts) == 3:
      _, chapter = parts[:-1]
    elif len(parts) == 2:
      chapter = bookname
    else:
      raise Exception
    if not os.path.exists(f'ctext/{bookname}/{chapter}.html'):
      print(urlpart, "not exists")
    with open(f'ctext/{bookname}/{chapter}.html', 'r') as f:
      html_txt = f.read()
    soup = BeautifulSoup(html_txt, 'html.parser')
    chn_texts = soup.find_all(lambda tag: tag.name == 'td' and tag.get('class') == ['ctext'])
    eng_texts = soup.find_all(lambda tag: tag.name == 'td' and tag.get('class') == ['etext']
                                          and ("意见" not in tag.text) and ("网站" not in tag.text))
    if len(eng_texts) == len(chn_texts):
      chn_text_pool.extend([tag.text for tag in chn_texts])
      eng_text_pool.extend([tag.text for tag in eng_texts])
    else:
      if len(eng_texts) != 0:
        print(chapter, len(chn_texts), "Chn paragraph", len(eng_texts), "Eng paragraph", "mismatch")
      chn_text_pool.extend([tag.text for tag in chn_texts])
      eng_text_pool.extend(["" for tag in chn_texts])
    valid_urls.append(urlpart)

  print("\n", bookname)
  print("Chinese text paragraphs 章", len(chn_text_pool))
  print("Chinese text sentence count 句", len("\n".join(chn_text_pool).split("。")))
  print("Chinese text character count 字", len("\n".join(chn_text_pool)))
  print("English text paragraphs", len(eng_text_pool))
  print("English text sentence count", len("\n".join(eng_text_pool).split(". ")))
  print("English text word count", len("\n".join(eng_text_pool).split(" ")))
  savedict = edict({"chn_text_pool": chn_text_pool, "eng_text_pool": eng_text_pool,
                    "chap_urls": valid_urls, "bookname": bookname})
  non_empty_eng = [text for text in eng_text_pool if text != ""]
  if len(chn_text_pool) == len(non_empty_eng):
    suffix = "ChEn"
  elif len(non_empty_eng) == 0:
    suffix = "Ch"
  else:
    suffix = "ChParten"
  pkl.dump(savedict,
           open(f"ctext/{bookname}_{suffix}.pkl", "wb"), )
  print(f"\nSaved to 'ctext/{bookname}_{suffix}.pkl'")
  return savedict


def fetch_parse_text_page(url=None, text=None):
  """Fetch and parse one html page.

  Args:
    url: the url of the page
    text: the html text of the page
  """
  if url is not None and text is None:
    r = requests.get(url)
    text = r.text
  soup = BeautifulSoup(text, 'html.parser')
  chn_texts = soup.find_all(lambda tag: tag.name == 'td' and tag.get('class') == ['ctext'])
  eng_texts = soup.find_all(lambda tag: tag.name == 'td' and tag.get('class') == ['etext']
                  and ("意见" not in tag.text) and ("网站" not in tag.text))
  chn_texts_pure = [tag.text for tag in chn_texts]
  eng_texts_pure = [tag.text for tag in eng_texts]
  print(len(chn_texts), "Chn paragraph", len(eng_texts), "Eng paragraph")
  return chn_texts_pure, eng_texts_pure
