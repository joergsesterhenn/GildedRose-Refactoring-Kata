from abc import abstractmethod, ABC


class Item(ABC):
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)

    def increment_quality(self):
        self.quality += 1

    def devalue(self):
        self.quality = 0

    def decrement_quality(self):
        self.quality -= 1

    def decrement_sell_in(self):
        self.sell_in -= 1

    def is_quality_not_yet_maxed(self):
        return self.quality < 50

    def is_expired(self):
        return self.sell_in < 0

    @abstractmethod
    def age(self):
        pass

    @staticmethod
    def of(name, sell_in, quality):

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

    def age(self):
        # update quality
        if self.quality > 0:
            self.decrement_quality()
        # update sell_in
        self.decrement_sell_in()
        # update quality for expired items
        if self.is_expired():
            if self.quality > 0:
                self.decrement_quality()


class SulfurasItem(Item):

    def age(self):
        pass


class ConjuredItem(Item):

    def age(self):
        if self.quality > 0:
            self.decrement_quality()
        if self.quality > 0:
            self.decrement_quality()
        self.decrement_sell_in()
        if self.is_expired():
            if self.quality > 0:
                self.decrement_quality()
            if self.quality > 0:
                self.decrement_quality()


class AgedBrieItem(Item):

    def age(self):
        if self.is_quality_not_yet_maxed():
            self.increment_quality()
        self.decrement_sell_in()
        if self.is_expired():
            if self.is_quality_not_yet_maxed():
                self.increment_quality()


class BackstagePassItem(Item):

    def age(self):
        if self.is_quality_not_yet_maxed():
            self.increment_quality()
        if self.sell_in < 11 and self.is_quality_not_yet_maxed():
            self.increment_quality()
        if self.sell_in < 6 and self.is_quality_not_yet_maxed():
            self.increment_quality()
        self.decrement_sell_in()
        if self.is_expired():
            self.devalue()
