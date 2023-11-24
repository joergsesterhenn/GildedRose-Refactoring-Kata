# -*- coding: utf-8 -*-

class GildedRoseStockStatusUpdater(object):

    def __init__(self, items):
        self.items = items

    def update_stock_status(self):
        for item in self.items:
            item.update()
