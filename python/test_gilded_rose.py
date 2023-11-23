# -*- coding: utf-8 -*-
import unittest

from gilded_rose import GildedRoseStockStatusUpdater
from Item import Item


class GildedRoseTest(unittest.TestCase):
    def test_items_are_not_changed_in_name(self):
        items = [Item("foo", 0, 0)]
        gilded_rose = GildedRoseStockStatusUpdater(items)
        gilded_rose.update_stock_status()
        self.assertEqual("foo", items[0].name)

    def test_items_sellIn_reduces_in_value_each_run(self):
        items = [Item("foo", 1, 1)]
        gilded_rose = GildedRoseStockStatusUpdater(items)
        gilded_rose.update_stock_status()
        self.assertEqual(0, items[0].sell_in)

    def test_items_quality_reduces_in_value_each_run(self):
        items = [Item("foo", 1, 1)]
        gilded_rose = GildedRoseStockStatusUpdater(items)
        gilded_rose.update_stock_status()
        self.assertEqual(0, items[0].quality)


if __name__ == '__main__':
    unittest.main()
