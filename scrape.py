"""
Build Knowledge Base by Scraping the web
"""

import os
import translate

def _load_progress():
  """
  Load Progress
  :returns: index progress
  :rtype: string
  """

  if( not os.path.isfile('res/_metadata') ):
    writer = open('res/_metadata', 'w')
    writer.write('0')
    writer.close()
    return 0
  meta = int(open('res/_metadata', 'r').read())
  return meta

def _save_progress(count):
  """
  Save Scraping Progress
  :param count: index number
  :type count: int
  """

  writer = open('res/_metadata', 'w')
  writer.write(str(count))
  writer.close()

def _save_data(eng, out, count):
  """
  Save Scraped Data
  :param eng: english word
  :type eng: string
  :param out: word output
  :type out: string
  :param count: index number
  :type count: int
  """

  writer = open('res/'+str(count),'w')
  writer.write(eng + ' : ' + out)
  writer.close()
  _save_progress(count)

def scrape(langOutput):
  """
  Scrape the web and build knowledge base
  :param langOutput: language output
  :type langOutput: string
  """

  start = _load_progress()
  count = start
  words = open('alphaextract.txt','r').read().split()
  print('Starting at: Index '+str(start))
  for word in words[start:]:
    count += 1
    print('\rProcessing ['+str(count)+'/'+str(len(words))+']',end='')

    fil = translate.translate(word, 'English', langOutput)
    if not fil:
      print('Skipping: '+word)
      continue
    _save_data(
      word,
      fil,
      count
    )


if __name__ == '__main__':
  # Start Scraping
  scrape('Filipino')

