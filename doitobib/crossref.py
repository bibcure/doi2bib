from __future__ import print_function
import requests

bare_url = "http://api.crossref.org/"


def get_bib(doi):
    url = "{}works/{}/transform/application/x-bibtex"
    url = url.format(bare_url, doi)
    r = requests.get(url)
    found = False if r.status_code != 200 else True
    bib = r.content
    return found, bib


def get_json(doi):
    url = "{}works/{}"
    url = url.format(bare_url, doi)
    r = requests.get(url)
    found = False if r.status_code != 200 else True
    item = r.content
    return found, item


def get_bib_from_doi(doi):
    bib = ""
    found, item = get_json(doi)
    if found:
        # contracted_journal = item.json()["message"]["short-container-title"]
        found, bib = get_bib(doi)
        #pegar journal contraido e contrair autores
        # depois fazer um replace no bib com  o nome do journal e o
        #contraido, ou usar o bibtexparser(ultima melhor)
    else:
        found = False

    return found, bib
