# encoding: utf-8
"""Tests for browsing the api."""
from unittest import TestCase
import re

from viltolyckor.scraper import ViltolyckorScraper


class TestViltolyckorScraper(TestCase):

    def setUp(self):
        self.scraper = ViltolyckorScraper()
        self.dataset = self.scraper.items[0]

    def test_get_dataset(self):
        assert len(self.scraper.items) == 1

    def test_get_regions(self):
        regions = self.dataset.dimensions["region"].allowed_values
        assert len(regions) >= 22

    def test_get_years(self):
        years = self.dataset.dimensions["year"].allowed_values
        assert len(years) >= 9

    def test_get_latest_year(self):
        latest_year = self.dataset.latest_year
        assert isinstance(latest_year, unicode)
        assert re.match("\d\d\d\d", latest_year)

    def test_get_viltslag(self):
        viltslag = self.dataset.dimensions["viltslag"].allowed_values
        assert len(viltslag) == 14


    def test_basic_query(self):
        res = self.dataset.fetch()
        assert len(res) == 13 * 14

    def test_specific_query(self):
        res = self.dataset.fetch({
            "region": u"Kalmar län",
            "year": "2016"
        })
        assert len(res) == 13 * 14
        data = res.list_of_dicts[0]
        assert data["year"] == "2016"
        assert data["region"] == u"Kalmar län"
