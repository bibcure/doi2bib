"""
crossref integration
===========================
The core module
"""

from __future__ import unicode_literals, print_function, absolute_import
from builtins import str
import requests
import bibtexparser
import re

bare_url = "http://api.crossref.org/"


def get_bib(doi):
    """
    Parameters
    ----------

        doi: str

    Returns
    -------

        found: bool
        bib: str
    """
    url = "{}works/{}/transform/application/x-bibtex"
    url = url.format(bare_url, doi)
    r = requests.get(url)
    found = False if r.status_code != 200 else True
    bib = r.content
    bib = str(bib, "utf-8")

    return found, bib


def get_json(doi):
    """
    Parameters
    ----------
        doi: str

    Returns
    -------

        found: bool
        item: dict
            Response from crossref
    """

    url = "{}works/{}"
    url = url.format(bare_url, doi)
    r = requests.get(url)
    found = False if r.status_code != 200 else True
    item = r.json()

    return found, item


def get_bib_from_doi(doi, abbrev_journal=True, add_abstract=False):
    """
    Parameters
    ----------

        doi: str
        abbrev_journal: bool
            If True try to abbreviate the journal name
        add_abstract: bool
            If True try to add abstract to bibtex
    Returns
    -------

        found: bool
        bib: str
            The bibtex string
    """
    found, bib = get_bib(doi)
    if found:
        found, item = get_json(doi)
        if found:
            message = item.get("message")
            if message:
                abstract = message.get("abstract")
                abbreviated_journal = message.get("short-container-title")
                if add_abstract and abstract:
                    bi = bibtexparser.loads(bib)
                    bi.entries[0]["abstract"] = abstract
                    bib = bibtexparser.dumps(bi)
                if abbrev_journal and abbreviated_journal:
                    abbreviated_journal = abbreviated_journal[0].strip()
                    bib = re.sub(
                        r"journal = \{[^>]*?\}",
                        "journal = {" + abbreviated_journal + "}",
                        bib
                    )
    return found, bib
