# -*- coding: utf-8 -*-

class GildedRoseInventoryStatusUpdater(object):

    def __init__(self, inventory):
        self.inventory = inventory

    def age_by_one_day(self):
        for item in self.inventory:
            item.age()
