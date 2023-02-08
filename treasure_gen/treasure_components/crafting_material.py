
class CraftingMaterial:

    def __init__(self, rarity, material):
        self.rarity = rarity
        self.material = material

    def __str__(self):
        return f"{self.rarity} {self.material}"
