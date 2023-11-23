# -*- coding: utf-8 -*-
def update_item_quality(item):
    if item.is_aged_brie() or item.is_backstage_pass():
        increase_quality(item)
    else:
        decrease_quality(item)


def decrease_item_sell_in(item):
    if not item.is_sulfuras():
        item.sell_in -= 1


def update_item_quality_past_sell_in(item):
    if item.is_sell_in_date_passed():
        if item.is_aged_brie():
            if item.is_quality_not_yet_maxed():
                item.increment_quality()
        else:
            if item.is_backstage_pass():
                item.devalue()
            else:
                decrease_quality(item)


def decrease_quality(item):
    if item.quality > 0:
        if not item.is_sulfuras():
            item.decrement_quality()
        if item.is_conjured():
            item.decrement_quality()


def increase_quality(item):
    if item.is_quality_not_yet_maxed():
        item.increment_quality()
        if item.is_backstage_pass():
            if item.sell_in < 11 and item.is_quality_not_yet_maxed():
                item.increment_quality()
            if item.sell_in < 6 and item.is_quality_not_yet_maxed():
                item.increment_quality()


class GildedRoseStockStatusUpdater(object):

    def __init__(self, items):
        self.items = items

    def update_stock_status(self):
        for item in self.items:
            update_item_quality(item)
            decrease_item_sell_in(item)
            update_item_quality_past_sell_in(item)
