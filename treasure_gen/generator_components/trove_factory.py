import dice

from treasure_gen.utilities import get_valid_int

class Trove:

    def __init__(self, game_state):
        self.game_state = game_state
        self.num_of_trove_dice = self.game_state.get_trove_dice_count()
        self.coin_allocation = None
        self.item_allocation = None
        self.coin_value = 0
        self.item_weighting = None

    def set_trove_allocation(self):
            print(f"There are {self.num_of_trove_dice} Trove Dice at the {self.game_state.get_tier()} tier.\n")
            self._get_valid_dice_allocation(self.set_coin_allocation, f"How many are allocated to coins?: ")
            if self.num_of_trove_dice > 0:
                self._get_valid_dice_allocation(self.set_item_allocation, f"How many are allocated to items?: ")
                self._set_item_weighting()
            print(f"Coin dice: {self.coin_allocation}\nItem dice: {self.item_allocation}")

    def roll_trove_dice(self):
        if self.coin_allocation >= 1:
            self._roll_coin_dice()
        if self.item_allocation >= 1:
            self._roll_item_dice()

    def _set_item_weighting(self):
        print(f"How do you want to weigh items in this trove?: ")
        choice = 0
        while choice == 0:
            try:
                choice = int(input(f"1. Balanced\n2. More Trade Goods\n3. More Art Objects\n4. More Gemstones" f"\n"
                                   f"5. No Trade Goods\n6. No Art Objects\n7. No Gemstones"))
            except ValueError:
                print("Must be on of the valid options.")
            else:
                if choice < 1 or choice > 7 :
                    print("Must be one of the valid options.")
                    choice = 0

    def _build_trove(self):



    def _roll_coin_dice(self):
        result = sum(dice.roll(f"{self.coin_allocation}d6"))
        self.coin_value = result * self.game_state.get_coin_multiplier()
        # TODO
        # Convert Gold Pieces to Copper Pieces and multiply
        print(f"{self.coin_value} Gold Pieces")

    def _roll_item_dice(self):
        result = sum(dice.roll(f"{self.item_allocation}d6"))

    def _get_valid_dice_allocation(self, set_allocation, message):
        allocated = False
        while self.num_of_trove_dice > 0 and allocated == False:
            allocation = get_valid_int(message, allow_zero=True)
            if allocation > self.num_of_trove_dice:
                print("You cannot allocate more than you have available!")
            else:
                self.num_of_trove_dice -= allocation
                set_allocation(allocation)
                allocated = True

    def set_coin_allocation(self, allocation):
        self.coin_allocation = allocation

    def set_item_allocation(self, allocation):
        self.item_allocation = allocation