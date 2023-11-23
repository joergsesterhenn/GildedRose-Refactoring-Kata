# -*- coding: utf-8 -*-

def update_item_quality(item):
    if is_aged_brie(item) or is_backstage_pass(item):
        if item.quality < 50:
            item.quality = item.quality + 1
            if is_backstage_pass(item):
                if item.sell_in < 11 and item.quality < 50:
                    item.quality = item.quality + 1
                if item.sell_in < 6 and item.quality < 50:
                    item.quality = item.quality + 1
    else:
        if item.quality > 0:
            if not is_sulfuras(item):
                item.quality = item.quality - 1
    if not is_sulfuras(item):
        item.sell_in = item.sell_in - 1
    if item.sell_in < 0:
        if is_aged_brie(item):
            if item.quality < 50:
                item.quality = item.quality + 1
        else:
            if is_backstage_pass(item):
                item.quality = item.quality - item.quality
            else:
                if item.quality > 0:
                    if not is_sulfuras(item):
                        item.quality = item.quality - 1


def is_sulfuras(item):
    return item.name == "Sulfuras, Hand of Ragnaros"


def is_backstage_pass(item):
    return item.name == "Backstage passes to a TAFKAL80ETC concert"


def is_aged_brie(item):
    return item.name == "Aged Brie"


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
