url = 'https://docs.google.com/spreadsheets/d/1V1_nrdl-UpVEVhS1zFsSIvJzA8qb1VgZm3hRdb3v1QM/pubhtml'

import pytxt, urllib2
ld=pytxt.tsv2ld(url)

def scrape_esquire(url):
    txt=urllib2.urlopen(url).read()
    before,after=txt.split('<div id="article_content">')

    content=after.split('<!-- begin viral toolbar -->')[0]

    phrase = '<!--end image_container-->'
    if phrase in content:
        content = content.split(phrase)[1]
    
    return pytxt.unhtml(content) # the function here removes all html


def scrape_elle(url):
    txt=urllib2.urlopen(url).read()
    content=txt.split('article-body--text ">')[1]
    content = content.split('<div\nclass="article-body--share-container">')[0]
    return pytxt.unhtml(content)

for d in ld: # meaning for every row in the spreadsheet
    print d['#'],'...'
    if d['Magazine']=='Esquire':
        result = scrape_esquire(d['Link'])
    elif d['Magazine']=='Elle':
        result= scrape_elle(d['Link'])

    d['Text'] = result


    
pytxt.write2('magazine_scrape_results.xlsx', ld)
