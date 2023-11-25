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

    def is_sell_in_date_passed(self):
        return self.sell_in < 0

    @abstractmethod
    def update(self):
        pass


