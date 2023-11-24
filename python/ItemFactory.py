from Item import Item


class ItemFactory:
    @staticmethod
    def of(name, sell_in, quality) -> Item:

        if "Conjured" in name:
            return ConjuredItem(name, sell_in, quality)

        if "Sulfuras" in name:
            return SulfurasItem(name, sell_in, quality)

        if "Backstage passes" in name:
            return BackstagePassItem(name, sell_in, quality)

        if "Aged Brie" in name:
            return AgedBrieItem(name, sell_in, quality)

        else:
            return DefaultItem(name, sell_in, quality)


class DefaultItem(Item):

    def update(self):
        if self.quality > 0:
            self.decrement_quality()
        self.decrement_sell_in()
        if self.is_sell_in_date_passed():
            if self.quality > 0:
                self.decrement_quality()


class SulfurasItem(Item):

    def update(self):
        pass


class ConjuredItem(Item):

    def update(self):
        if self.quality > 0:
            self.decrement_quality()
        if self.quality > 0:
            self.decrement_quality()
        self.decrement_sell_in()
        if self.is_sell_in_date_passed():
            if self.quality > 0:
                self.decrement_quality()
            if self.quality > 0:
                self.decrement_quality()


class AgedBrieItem(Item):

    def update(self):
        if self.is_quality_not_yet_maxed():
            self.increment_quality()
        self.decrement_sell_in()
        if self.is_sell_in_date_passed():
            if self.is_quality_not_yet_maxed():
                self.increment_quality()


class BackstagePassItem(Item):

    def update(self):
        if self.is_quality_not_yet_maxed():
            self.increment_quality()
        if self.sell_in < 11 and self.is_quality_not_yet_maxed():
            self.increment_quality()
        if self.sell_in < 6 and self.is_quality_not_yet_maxed():
            self.increment_quality()
        self.decrement_sell_in()
        if self.is_sell_in_date_passed():
            self.devalue()
