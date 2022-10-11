"""Download all from ctext.org."""
from ctex_download_lib import find_chap_urls, download_book_htmls, parse_saved_htmls

bookname = "mengzi"
chap_urls, _ = find_chap_urls(bookname, book_url=None)
download_book_htmls(bookname, chap_urls)
textdict_mz = parse_saved_htmls(bookname, chap_urls)
#%%
bookname = "analects"
chap_urls, _ = find_chap_urls(bookname, book_url=None)
download_book_htmls(bookname, chap_urls)
textdict_lunyu = parse_saved_htmls(bookname, chap_urls)
#%%
bookname = "shang-jun-shu"
chap_urls, _ = find_chap_urls(bookname, book_url=None)
download_book_htmls(bookname, chap_urls)
textdict = parse_saved_htmls(bookname, chap_urls)
#%%
bookname = "liji"
chap_urls, _ = find_chap_urls(bookname, book_url=None)
download_book_htmls(bookname, chap_urls)
textdict = parse_saved_htmls(bookname, chap_urls)
#%%
bookname = "art-of-war"
chap_urls, _ = find_chap_urls(bookname, book_url=None)
download_book_htmls(bookname, chap_urls)
textdict = parse_saved_htmls(bookname, chap_urls)
#%%
bookname = "mozi"
chap_urls, _ = find_chap_urls(bookname, book_url=None)
download_book_htmls(bookname, chap_urls)
textdict_mz = parse_saved_htmls(bookname, chap_urls)
#%%
bookname = "zhuangzi"
chap_urls, _ = find_chap_urls(bookname, book_url=None)
download_book_htmls(bookname, chap_urls)
textdict = parse_saved_htmls(bookname, chap_urls)
#%%
bookname = "dao-de-jing"
# chap_urls, _ = find_chap_urls(bookname, book_url=None)
download_book_htmls(bookname, ["dao-de-jing/zhs?en=on"])
textdict_mz = parse_saved_htmls(bookname, ["dao-de-jing/zhs?en=on"])

#%%
"""Chinese only """
#%%
bookname = "hanfeizi"
chap_urls, _ = find_chap_urls(bookname, book_url=None)
download_book_htmls(bookname, chap_urls)
textdict = parse_saved_htmls(bookname, chap_urls)

bookname = "shiji"
chap_urls, _ = find_chap_urls(bookname, book_url=None)
download_book_htmls(bookname, chap_urls)
textdict = parse_saved_htmls(bookname, chap_urls)

bookname = "zhan-guo-ce"
chap_urls, _ = find_chap_urls(bookname, book_url=None)
download_book_htmls(bookname, chap_urls)
textdict = parse_saved_htmls(bookname, chap_urls)

bookname = "han-shu"
chap_urls, _ = find_chap_urls(bookname, book_url=None)
download_book_htmls(bookname, chap_urls)
textdict = parse_saved_htmls(bookname, chap_urls)

bookname = "sanguozhi"
chap_urls, _ = find_chap_urls(bookname, book_url=None)
download_book_htmls(bookname, chap_urls)
textdict = parse_saved_htmls(bookname, chap_urls)

bookname = "hou-han-shu"
chap_urls, _ = find_chap_urls(bookname, book_url=None)
download_book_htmls(bookname, chap_urls)
textdict = parse_saved_htmls(bookname, chap_urls)

bookname = "shi-shuo-xin-yu"
chap_urls, _ = find_chap_urls(bookname, book_url=None)
download_book_htmls(bookname, chap_urls)
textdict = parse_saved_htmls(bookname, chap_urls)

bookname = "yan-shi-jia-xun"
chap_urls, _ = find_chap_urls(bookname, book_url=None)
download_book_htmls(bookname, chap_urls)
textdict = parse_saved_htmls(bookname, chap_urls)

bookname = "hongloumeng"
chap_urls, _ = find_chap_urls(bookname, book_url=None)
download_book_htmls(bookname, chap_urls)
textdict = parse_saved_htmls(bookname, chap_urls)

