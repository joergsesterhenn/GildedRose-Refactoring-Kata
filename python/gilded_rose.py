# -*- coding: utf-8 -*-

def update_item_quality(item):
    aged_brie = item.name == "Aged Brie"
    backstage_pass = item.name == "Backstage passes to a TAFKAL80ETC concert"
    sulfuras = item.name == "Sulfuras, Hand of Ragnaros"
    if not aged_brie and not backstage_pass:
        if item.quality > 0:
            if not sulfuras:
                item.quality = item.quality - 1
    else:
        if item.quality < 50:
            item.quality = item.quality + 1
            if backstage_pass:
                if item.sell_in < 11:
                    if item.quality < 50:
                        item.quality = item.quality + 1
                if item.sell_in < 6:
                    if item.quality < 50:
                        item.quality = item.quality + 1
    if not sulfuras:
        item.sell_in = item.sell_in - 1
    if item.sell_in < 0:
        if not aged_brie:
            if not backstage_pass:
                if item.quality > 0:
                    if not sulfuras:
                        item.quality = item.quality - 1
            else:
                item.quality = item.quality - item.quality
        else:
            if item.quality < 50:
                item.quality = item.quality + 1


class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            update_item_quality(item)


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
