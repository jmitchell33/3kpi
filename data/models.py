from django.db import models

# Create your models here.

DAMAGE_CHOICES = (
    ('edged', 'edged'),
    ('blunt', 'blunt'),
    ('fire', 'fire'),
    ('ice', 'ice'),
    ('acid', 'acid'),
    ('electricity', 'electricity'),
    ('mind', 'mind'),
    ('energy', 'energy'),
    ('poison', 'poison'),
    ('radiation', 'radiation')
)

ATTACK_TYPE_CHOICES = (
    ('Normal', 'Normal'),
    ('Special', 'Special')
)

WEIGHT_CHOICES = (
    ("It looks very light.", "It looks very light."),
    ("It looks light.", "It looks light."),
    ("It doesn't look too heavy.", "It doesn't look too heavy."),
    ("It looks heavy.", "It looks heavy."),
    ("It would take considerable effort to lift this.", "It would take considerable effort to lift this."),
    ("You'll most likely herniate a disc lifting this.", "You'll most likely herniate a disc lifting this.")
)

ITEM_TYPE = (
    ('Normal', 'Normal'),
    ('Legendary', 'Legendary'),
    ('World Drop', 'World Drop'),
    ('Guild Artifact', 'Guild Artifact')
)

ITEM_SLOT = (
    ('Object', 'Object'),
    ('Weapon', 'Weapon'),
    ('Wand', 'Wand'),
    ('Head', 'Head'),
    ('Around neck', 'Around neck'),
    ('Heavy Body', 'Heavy Body'),
    ('Upper body', 'Upper body'),
    ('On legs', 'On legs'),
    ('Light body', 'Light body'),
    ('Hands', 'Hands'),
    ('Feet', 'Feet'),
    ('On fingers', 'On fingers'),
    ('Shield', 'Shield'),
    ('Other', 'Other'),
    ('Magical', 'Magical'),
    ('Unknown', 'Unknown'),
)

REALM_CHOICES = (
    ('Chaos', 'Chaos'),
    ('Fantasy', 'Fantasy'),
    ('Science,', 'Science'),
    ('Pinnacle', 'Pinnacle')
)

class Area(models.Model):
    name = models.CharField(max_length=255, blank=False)
    realm = models.CharField(choices=REALM_CHOICES, max_length=100, blank=True)
    dungeon = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Monster(models.Model):
    parent_area = models.ForeignKey(Area, related_name='area_monsters', on_delete=models.CASCADE, blank=True, null=True)
    short = models.CharField(max_length=255, blank=False)
    description = models.TextField(blank=True)
    size = models.IntegerField(blank=True, null=True)
    notes = models.TextField(blank=True)
    scaler = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return '%a (Sclr: %a)' % (self.short, self.scaler)

class Monster_AttackType(models.Model):
    parent_monster = models.ForeignKey(Monster, related_name='monster_damage_types', on_delete=models.CASCADE, blank=True, null=True)
    damage_type = models.CharField(choices=DAMAGE_CHOICES, max_length=50, blank=True)
    attack_type = models.CharField(choices=ATTACK_TYPE_CHOICES, max_length=50, blank=True)

class Item(models.Model):
    parent_monster = models.ForeignKey(Monster, related_name='monster_items', on_delete=models.CASCADE, blank=True, null=True)
    parent_area = models.ForeignKey(Area, related_name='area_items', on_delete=models.CASCADE, blank=True, null=True)
    short = models.CharField(max_length=255, blank=False)
    description = models.TextField(blank=True)
    slot = models.CharField(choices=ITEM_SLOT, max_length=100, blank=False)
    weight = models.CharField(choices=WEIGHT_CHOICES, max_length=255, blank=True)
    unbreakable = models.BooleanField(default=False, blank=False)
    cursed = models.BooleanField(default=False, blank=False)
    hp_regen = models.IntegerField(null=True)
    sp_regen = models.IntegerField(null=True)
    hp_drain = models.IntegerField(null=True)
    sp_drain = models.IntegerField(null=True)
    ftouchable = models.BooleanField(default=False, blank=False)
    transmutable = models.BooleanField(default=False, blank=False)
    duplicable = models.BooleanField(default=False, blank=False)
    bind_on_pickup = models.BooleanField(default=False, blank=False)
    bind_on_equip = models.BooleanField(default=False, blank=False)
    stats_str = models.IntegerField(null=True)
    stats_con = models.IntegerField(null=True)
    stats_int = models.IntegerField(null=True)
    stats_wis = models.IntegerField(null=True)
    stats_dex = models.IntegerField(null=True)
    stats_cha = models.IntegerField(null=True)
    smd = models.BooleanField(default=False, blank=False)
    specials = models.TextField(blank=True)
    edged = models.IntegerField(null=True)
    blunt = models.IntegerField(null=True)
    fire = models.IntegerField(null=True)
    ice = models.IntegerField(null=True)
    acid = models.IntegerField(null=True)
    electricity = models.IntegerField(null=True)
    mind = models.IntegerField(null=True)
    energy = models.IntegerField(null=True)
    poison = models.IntegerField(null=True)
    radiation = models.IntegerField(null=True)

    def __str__(self):
        return self.short
    

class Eternal_Powers(models.Model):
    character = models.CharField(max_length=255, blank=False)
    hmheal = models.BooleanField(default=False)
    destroy = models.BooleanField(default=False)
    divine_insight = models.BooleanField(default=False)
    duplicate_creature = models.BooleanField(default=False)
    duplicate_item = models.BooleanField(default=False)
    embiggen = models.BooleanField(default=False)
    energy_well = models.BooleanField(default=False)
    enlarge = models.BooleanField(default=False)
    farsight = models.BooleanField(default=False)
    fry = models.BooleanField(default=False)
    hasten = models.BooleanField(default=False)
    heal = models.BooleanField(default=False)
    heightened_awareness = models.BooleanField(default=False)
    immortality = models.BooleanField(default=False)
    pick_pocket = models.BooleanField(default=False)
    protection = models.BooleanField(default=False)
    quicken = models.BooleanField(default=False)
    redact = models.BooleanField(default=False)
    refresh_area = models.BooleanField(default=False)
    refresh_item = models.BooleanField(default=False)
    reset_dungeon = models.BooleanField(default=False)
    resurrect = models.BooleanField(default=False)
    shred = models.BooleanField(default=False)
    summon = models.BooleanField(default=False)
    teleport = models.BooleanField(default=False)
    unload_room = models.BooleanField(default=False)
    reload_item = models.BooleanField(default=False)
    cooldown_hmheal = models.DateTimeField(blank=True, null=True)
    cooldown_destroy = models.DateTimeField(blank=True, null=True)
    cooldown_divine_insight = models.DateTimeField(blank=True, null=True)
    cooldown_duplicate_creature = models.DateTimeField(blank=True, null=True)
    cooldown_duplicate_item = models.DateTimeField(blank=True, null=True)
    cooldown_embiggen = models.DateTimeField(blank=True, null=True)
    cooldown_energy_well = models.DateTimeField(blank=True, null=True)
    cooldown_enlarge = models.DateTimeField(blank=True, null=True)
    cooldown_farsight = models.DateTimeField(blank=True, null=True)
    cooldown_fry = models.DateTimeField(blank=True, null=True)
    cooldown_hasten = models.DateTimeField(blank=True, null=True)
    cooldown_heal = models.DateTimeField(blank=True, null=True)
    cooldown_heightened_awareness = models.DateTimeField(blank=True, null=True)
    cooldown_immortality = models.DateTimeField(blank=True, null=True)
    cooldown_pick_pocket = models.DateTimeField(blank=True, null=True)
    cooldown_protection = models.DateTimeField(blank=True, null=True)
    cooldown_quicken = models.DateTimeField(blank=True, null=True)
    cooldown_redact = models.DateTimeField(blank=True, null=True)
    cooldown_refresh_area = models.DateTimeField(blank=True, null=True)
    cooldown_refresh_item = models.DateTimeField(blank=True, null=True)
    cooldown_reset_dungeon = models.DateTimeField(blank=True, null=True)
    cooldown_resurrect = models.DateTimeField(blank=True, null=True)
    cooldown_shred = models.DateTimeField(blank=True, null=True)
    cooldown_summon = models.DateTimeField(blank=True, null=True)
    cooldown_teleport = models.DateTimeField(blank=True, null=True)
    cooldown_unload_room = models.DateTimeField(blank=True, null=True)
    cooldown_reload_item = models.DateTimeField(blank=True, null=True)    

    def __str__(self):
        return self.character