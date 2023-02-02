import random


class Quality:
    def __init__(self, quality=None):
        if quality is not None:
            self.quality = quality
        else:
            pass
    def get_quality(self):
        return self.quality
    def get_random_quality(self):
        """Returns a random quality. Inferior: 8%, Normal: 83%, Superior: 8%"""
        self.quality = random.choices(("Inferior", "Normal", "Superior"), weights=(8,83,8))[0]
        return self.quality
