# -*- coding: utf-8 -*-

def update_item_quality(item):
    if is_aged_brie(item) or is_backstage_pass(item):
        increase_quality(item)
    else:
        decrease_quality(item)


def update_item_quality_past_sell_in(item):
    if sell_in_date_passed(item):
        if is_aged_brie(item):
            if quality_not_yet_maxed(item):
                increase_quality_by_one(item)
        else:
            if is_backstage_pass(item):
                item.quality = 0
            else:
                decrease_quality(item)


def decrease_item_sell_in(item):
    if not is_sulfuras(item):
        item.sell_in = item.sell_in - 1


def quality_not_yet_maxed(item):
    return item.quality < 50


def sell_in_date_passed(item):
    return item.sell_in < 0


def increase_quality_by_one(item):
    item.quality = item.quality + 1


def is_conjured(item):
    return "Conjured" in item.name


def decrease_quality(item):
    if item.quality > 0:
        if not is_sulfuras(item):
            item.quality = item.quality - 1
        if is_conjured(item):
            item.quality = item.quality - 1


def increase_quality(item):
    if quality_not_yet_maxed(item):
        increase_quality_by_one(item)
        if is_backstage_pass(item):
            if item.sell_in < 11 and quality_not_yet_maxed(item):
                increase_quality_by_one(item)
            if item.sell_in < 6 and quality_not_yet_maxed(item):
                increase_quality_by_one(item)


def is_sulfuras(item):
    return "Sulfuras" in item.name


def is_backstage_pass(item):
    return "Backstage passes" in item.name


def is_aged_brie(item):
    return item.name == "Aged Brie"


class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            update_item_quality(item)
            decrease_item_sell_in(item)
            update_item_quality_past_sell_in(item)


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
