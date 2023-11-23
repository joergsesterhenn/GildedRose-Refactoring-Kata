class Item:
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

    def is_conjured(self):
        return "Conjured" in self.name

    def is_sulfuras(self):
        return "Sulfuras" in self.name

    def is_backstage_pass(self):
        return "Backstage passes" in self.name

    def is_aged_brie(self):
        return self.name == "Aged Brie"

    def is_quality_not_yet_maxed(self):
        return self.quality < 50

    def is_sell_in_date_passed(self):
        return self.sell_in < 0