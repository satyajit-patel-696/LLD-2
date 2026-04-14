from abc import ABC, abstractmethod
import copy


class Prototype(ABC):
    @abstractmethod
    def clone(self) -> "Prototype":
        pass


class GameCharacter(Prototype):
    def __init__(self, name: str, health: int, weapon: str, level: int) -> None:
        self.name = name
        self.health = health
        self.weapon = weapon
        self.level = level

    def clone(self) -> "GameCharacter":
        return copy.deepcopy(self)


class PrototypeRegistry:
    def __init__(self) -> None:
        # ❌ OLD:
        # self._prototypes: dict[str, Prototype] = {}

        # ✅ FIX: store correct type
        self._prototypes: dict[str, GameCharacter] = {}   # ⭐ FIXED

    def register_prototype(self, name: str, prototype: GameCharacter) -> None:  # ⭐ FIXED
        self._prototypes[name] = prototype

    def unregister_prototype(self, name: str) -> None:
        if name in self._prototypes:
            del self._prototypes[name]

    def get_clone(self, name: str) -> GameCharacter:   # ⭐ FIXED
        if name not in self._prototypes:
            raise ValueError(f"Prototype '{name}' not found.")
        return self._prototypes[name].clone()


# ===== MAIN =====
if __name__ == "__main__":

    registry = PrototypeRegistry()

    # Register base characters (prototypes)
    warrior_base = GameCharacter("Warrior", 100, "Sword", 1)
    mage_base = GameCharacter("Mage", 80, "Staff", 1)

    registry.register_prototype("warrior", warrior_base)
    registry.register_prototype("mage", mage_base)

    print("=== BASE PROTOTYPES ===")
    print("warrior_base:", warrior_base)
    print("mage_base   :", mage_base)

    # Clone characters
    warrior1 = registry.get_clone("warrior")
    warrior2 = registry.get_clone("warrior")

    mage1 = registry.get_clone("mage")
    mage2 = registry.get_clone("mage")

    # Modify clones
    warrior1.name = "Warrior Rookie"
    warrior1.level = 2

    warrior2.name = "Warrior Elite"
    warrior2.level = 5
    warrior2.weapon = "Golden Sword"

    mage1.name = "Mage Beginner"
    mage1.level = 2

    mage2.name = "Mage Master"
    mage2.level = 6
    mage2.weapon = "Ancient Wand"

    print("\n=== CLONED & MODIFIED CHARACTERS ===")
    print("warrior1:", warrior1)
    print("warrior2:", warrior2)
    print("mage1   :", mage1)
    print("mage2   :", mage2)

    print("\n=== ORIGINAL PROTOTYPES (UNCHANGED) ===")
    print("warrior_base:", warrior_base)
    print("mage_base   :", mage_base)