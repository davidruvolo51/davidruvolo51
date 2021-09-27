#'////////////////////////////////////////////////////////////////////////////
#' FILE: blogposts.py
#' AUTHOR: David Ruvolo
#' CREATED: 2021-05-05
#' MODIFIED: 2021-09-27
#' PURPOSE: fetch blog posts
#' STATUS: working
#' PACKAGES: requests, feedparser
#' COMMENTS: NA
#'////////////////////////////////////////////////////////////////////////////

import requests
import feedparser

# pull data
raw = requests.get('https://davidruvolo51.github.io/shinytutorials/rss')
rss = raw.content.decode('utf-8')
data = feedparser.parse(rss)


# @title generate entry markup
# @description pull attributes and create markdown for each entry
# @param data a list containing rss feed entries
# @return a list of values
def build_md(data):
    md = []
    for d in data:
        title = d['title']
        summary = d['summary']
        url = d['link']
        m = '- [' + title + ': ' + summary + '](' + url + ')
        md.append(m)
        md.append('\n')
    return md

# @title write_md
# @param file file connection
# @param markdown list containing markdown content
def write_md(file, markdown):
    for m in markdown:
        file.write(m)

# generate markdown
md = build_md(data['entries'])

with open(file='README.md', mode='r') as file:
    readme = file.readlines()

start = readme[0:readme.index('<!-- BlogPosts: start --->\n') + 1]
end = readme[readme.index('<!-- BlogPosts: end --->\n'):len(readme)]

with open('README.md', mode='w', encoding='utf-8') as file:
    write_md(file=file, markdown=start)
    write_md(file=file, markdown=md)
    write_md(file=file, markdown=end)
