"""Implements the MonsterDataManager class"""
from engine.serialization.dmanager import DataManager

class MonsterDataManager(DataManager):
    """Singleton class used to get and assign monster definitions and
    monster attributes"""

    DEFAULT_MONSTER_LOCATION = "location"
    DEFAULT_MONSTER_RATING = 0
    DEFAULT_MONSTER_STATS = {
        "attack" : 0,
        "speed" : 0,
        "defense" : 0,
        "health" : 0,
        "magic" : 0,
        "resist" : 0
    }

    def __init__(self):
        super().__init__("data/monster.p")
        self.attribute = DataManager("data/monster_attributes.p")

    def write(self):
        super().write()
        self.attribute.write()

    def get_attribute(self, name):
        for attr in range(self.attribute.get()):
            if attr.name == name:
                return attr
        return None

    def attributes(self):
        return self.attribute.get()

    def set_attributes(self, attributes):
        self.attribute.set(attribtes)

    def get_monster(self, name):
        """Convenience function. To get a monster"""
        return self.monsters()[name]

    def monsters(self):
        """Convenience function for returning dictionary of monster
        definitions"""
        return self.get()

    def new_monster(self, name):
        """Creates a new monster definition"""
        monster_def = {
            "location" : self.DEFAULT_MONSTER_LOCATION,
            "graphic" : {},
            "rating" : self.DEFAULT_MONSTER_RATING,
            "stats" : dict(self.DEFAULT_MONSTER_STATS),
            "abilities" : [],
            "attributes" : [],
            "drops" : []
        }
        self.monsters()[name] = monster_def

    def delete_monster(self, name):
        """Delete a monster with the given name."""
        del self.monsters()[name]

    def update_monster_name(self, name, new_name):
        monster = self.monsters()[name]
        del self.monsters()[name]
        self.monsters()[new_name] = monster

    def add_monster_drop(self, name, drop):
        self.monsters()[name]["drops"].append(drop)

    def remove_monster_drop(self, name, drop):
        self.monsters()[name]["drops"].remove(drop)

    def add_monster_move(self, name, move):
        self.monsters()[name]["abilities"].append(move)

    def remove_monster_move(self, name, move):
        self.monsters()[name]["abilities"].remove(move)

    def update_monster_stats(self, name, stype, value):
        self.monsters()[name]["stats"][stype] = value

    def update_monster_rating(self, name, rating):
        self.monsters()[name]["rating"] = rating

    def update_monster_location(self, name, location):
        self.monsters()[name]["location"] = location

    def add_monster_attribute(self, name, attribute):
        self.monsters()[name]["attributes"].append(attribute)

    def remove_monster_attribute(self, name, attribute):
        changed_attr = None
        for attr in self.monsters()[name]["attributes"]:
            if attr == attribute:
                changed_attr = attr
                break
        if changed_attr is not None:
            self.monsters()[name]["attributes"].remove(changed_attr)

    def update_monster_image(self, name, image_type, filename):
        self.monsters()[name]["graphic"][image_type] = filename