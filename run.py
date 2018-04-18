# encoding: utf-8
"""Tests for browsing the api."""

from viltolyckor.scraper import ViltolyckorScraper

# Init scraper
scraper = ViltolyckorScraper()
ds =  scraper.items[0]

ds.fetch({"region": u"Stockholms län", "year": "*"})
