import random


class QualityFactory:
    def __init__(self, quality=None):
        if quality is not None:
            self.quality = quality
        else:
            pass

    def get_quality(self):
        if self.quality == "Inferior":
            return Inferior
        elif self.quality == "Normal":
            return Normal
        elif self.quality == "Superior":
            return Superior

    @staticmethod
    def get_random_quality(inferior_weight, normal_weight, superior_weight):
        return random.choices((Inferior, Normal, Superior), weights=(inferior_weight, normal_weight, superior_weight))


class Inferior:
    def __init__(self):
        self.quality = "Inferior"


class Normal:
    def __init__(self):
        self.quality = "Normal"


class Superior:
    def __init__(self):
        self.quality = "Superior"
