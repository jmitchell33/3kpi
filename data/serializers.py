from rest_framework import serializers
from .models import *


class EternalPowersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Eternal_Powers
        fields = ('id', 'character', 'hmheal', 'destroy', 'divine_insight', 'duplicate_creature', 'duplicate_item', 'embiggen', 'energy_well', 'enlarge', 'farsight', 'fry', 'hasten', 'heal', 'heightened_awareness', 'immortality', 'pick_pocket', 'protection', 'quicken', 'redact', 'refresh_area', 'refresh_item', 'reset_dungeon', 'resurrect', 'shred', 'summon', 'teleport', 'unload_room', 'reload_item', 'cooldown_hmheal', 'cooldown_destroy', 'cooldown_divine_insight', 'cooldown_duplicate_creature', 'cooldown_duplicate_item', 'cooldown_embiggen', 'cooldown_energy_well', 'cooldown_enlarge', 'cooldown_farsight', 'cooldown_fry', 'cooldown_hasten', 'cooldown_heal', 'cooldown_heightened_awareness', 'cooldown_immortality', 'cooldown_pick_pocket', 'cooldown_protection', 'cooldown_quicken', 'cooldown_redact', 'cooldown_refresh_area', 'cooldown_refresh_item', 'cooldown_reset_dungeon', 'cooldown_resurrect', 'cooldown_shred', 'cooldown_summon', 'cooldown_teleport', 'cooldown_unload_room', 'cooldown_reload_item')


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ('id', 'parent_monster', 'parent_area', 'short', 'description', 'slot', 'weight', 'unbreakable', 'cursed', 'hp_regen', 'sp_regen', 'hp_drain', 'sp_drain', 'ftouchable', 'transmutable', 'duplicable', 'bind_on_pickup', 'bind_on_equip', 'stats_str', 'stats_con', 'stats_int', 'stats_wis', 'stats_dex', 'stats_cha', 'smd', 'specials', 'edged', 'blunt', 'fire', 'ice', 'acid', 'electricity', 'mind', 'energy', 'poison', 'radiation')

class AreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Area
        fields = ('id', 'name', 'realm', 'dungeon')

class MonsterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Monster
        fields = ('id', 'parent_area', 'short', 'description', 'size', 'notes', 'scaler')

class MonsterAttackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Monster_AttackType
        fields = ('id', 'parent_monster', 'damage_type', 'attack_type')
