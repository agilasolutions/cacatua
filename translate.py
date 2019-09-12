"""
Google translate
"""


from bs4 import BeautifulSoup
import urllib.request

global URL
global chromeUA
global mozillaUA

URL = 'https://google.com/search?q=translate+{WORD}+from+{FROM}+to+{TO}'
chromeUA = """\
  Mozilla/5.0 (Windows NT 6.3; Win64; x64) \
  AppleWebKit/537.36 (KHTML, like Gecko) \
  Chrome/37.0.2049.0 Safari/537.36"""

mozillaUA = 'Mozilla/5.0 (X11; Linux i686; rv:10.0) Gecko/20100101 Firefox/10.0'

def _getHTMLPage(word, fromLang, toLang, userAgent=chromeUA):
  """
  Get HTML Web Page
  :param word: word to convert
  :type word: string
  :param fromLang: base language
  :type fromLang: string
  :param toLang: language output
  :type toLang: string
  :param userAgent: request user agent
  :type userAgent: string
  :returns: html page
  :rtype: string
  """

  global URL

  url = URL
  url = url.replace('{WORD}', word)
  url = url.replace('{FROM}', fromLang)
  url = url.replace('{TO}', toLang)

  headers = {
    'User-Agent' : userAgent
  }

  req = urllib.request.Request(
    url,
    data = None,
    headers = headers
  )
  resp = urllib.request.urlopen(req)
  htmlpage = resp.read().decode('utf-8')
  return htmlpage

def _parse_page(htmlPage):
  """
  Parse HTML Page
  :param htmlPage: html page to parse
  :type htmlPage: string
  :returns: translation
  :rtype: string
  """

  soup = BeautifulSoup(htmlPage, features="html.parser")
  pageElements = soup.findAll('pre', {'data-placeholder' : 'Translation'})
  for element in pageElements:
    for res in element.find('span'):
      if res != 'Translation':
        return res
  return None


def translate(word, fromLang, toLang):
  """
  Translate Word/Phrase
  :param word: word to convert
  :type word: string
  :param fromLang: base language
  :type fromLang: string
  :param toLang: language output
  :type toLang: string
  :returns: translation result
  :rtype: string
  """

  pageStr = _getHTMLPage(word, 'English', 'Tagalog')
  result = _parse_page(pageStr)
  return result




