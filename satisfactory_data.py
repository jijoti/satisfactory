
class Resource:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.metadata = {}

    def __str__(self):
        return self.name

    def getId(self):
        return self.id

    def addMetadata(self, key, value):
        self.metadata[key] = value

    def getMetadata(self, key):
        return self.metadata[key]

class ResourceStack:
    def __init__(self, resource, amount):
        self.resource = resource
        self.amount = amount

    def __str__(self):
        return " ".join([str(self.amount), str(self.resource)])

    def getResource(self):
        return self.resource

    def getAmount(self):
        return self.amount

class Trade:
    def __init__(self, id, name, input, output):
        self.id = id
        self.name = name
        self.input = input 
        self.output = output

    def __str__(self):
        return self.name

    def getId(self):
        return self.id

    def getInput(self):
        return self.input

    def getOutput(self):
        return self.output

    def addMetadata(self, key, value):
        self.metadata[key] = value

    def getMetadata(self, key):
        return self.metadata[key]
  

#class SatisfactoryData:
#    def __init__(self, data_loader):
#        self.data_loader = data_loader
#        self.resources = []
#        self.trades = []
#
#    def load(self):
#        self.data_loader.load()
#        self.trades = self.data_loader.getTrades()
#
#    def getTrades(self):
#        return self.trades

class SatisfactoryResourceFactory:
    def __init__(self):
        self.next_id = 1

    def create(self, name, sink_points):
        resource = Resource(self.next_id, name)
        resource.addMetadata("sink_points", sink_points)
        self.next_id = self.next_id + 1
        return resource

class SatisfactoryTradeFactory:
    def __init__(self):
        self.next_id = 1

    def create(self, name, input, output):
        trade = Trade(self.next_id, name, input, output)
        self.next_id = self.next_id + 1
        return trade

#class SatisfactoryResourceStore:
#    def __init__(self):
#        self.resources = {}
#    
#    def addResource(self, resource):
#        self.resources[resource.getId()] = resource
#        return resource.getId()
#    
#    def getResource(self, id):
#        return self.resources[id]

class StaticSatisfactoryDataLoader:
    #def __init__(self, resource_factory, resource_store):
    #    self.rf = resoure_factory
    #    self.rs = resoure_store
    #    self.IRON_ORE = resource_store.addResource(resource_factory.create("iron_ore", 1))
    #    self.IRON_INGOT = resource_store.addResource(resource_factory.create("iron_ingot", 2))

    def __init__(self, resource_factory, trade_factory):
        self.resource_factory = resource_factory
        self.trade_factory = trade_factory
        self.loaded = False
        self.trades = []
        self.resources = {}

    def load(self):
        if self.loaded:
            return
        self._loadResources()
        self._loadTrades()
        self.loaded = True

    def _addResource(self, name, sink_price):
        resource = self.resource_factory.create(name, sink_price)
        self.resources[resource.getId()] = resource
        return resource

    def _addTrade(self, name, input, output):
        inputs = []
        for resource in input:
            inputs.append(ResourceStack(resource[0], resource[1]))
        outputs = []
        for resource in output:
            outputs.append(ResourceStack(resource[0], resource[1]))

        self.trades.append(self.trade_factory.create(name, inputs, outputs))


    def _loadResources(self):
        self.IRON_ORE = self._addResource("iron_ore", 1)
        self.COPPER_ORE = self._addResource("copper_ore", 3)
        self.LIMESTONE = self._addResource("limestone", 2)
        self.CATERIUM_ORE = self._addResource("caterium_ore", 7)
        self.SULFUR = self._addResource("sulfur", 11)
        self.RAW_QUARTZ = self._addResource("raw_quartz", 15)
        self.COAL = self._addResource("coal", 3)
        self.CRUDE_OIL = self._addResource("crude_oil", 0)
        self.BAUXITE = self._addResource("bauxite", 8)
        self.WATER = self._addResource("water", 0)
        self.NITROGEN_GAS = self._addResource("nitrogen_gas", 0)
        self.URANIUM = self._addResource("uranium", 0)
        self.IRON_INGOT = self._addResource("iron_ingot", 2)
        self.COPPER_INGOT = self._addResource("copper_ingot", 6)
        self.CATERIUM_INGOT = self._addResource("caterium_ingot", 42)
        self.STEEL_INGOT = self._addResource("steel_ingot", 8)
        self.ALUMINUM_INGOT = self._addResource("aluminum_ingot", 131)
        self.IRON_PLATE = self._addResource("iron_plate", 6)
        self.IRON_ROD = self._addResource("iron_rod", 4)
        self.SCREW = self._addResource("screw", 2)
        self.COPPER_SHEET = self._addResource("copper_sheet", 24)
        self.STEEL_BEAM = self._addResource("steel_beam", 64)
        self.STEEL_PIPE = self._addResource("steel_pipe", 24)
        self.ALUMINUM_CASING = self._addResource("aluminum_casing", 393)
        self.WIRE = self._addResource("wire", 6)
        self.CABLE = self._addResource("cable", 24)
        self.QUICKWIRE = self._addResource("quickwire", 17)
        self.CONCRETE = self._addResource("concrete", 12)
        self.QUARTZ_CRYSTAL = self._addResource("quartz_crystal", 50)
        self.SILICA = self._addResource("silica", 20)
        self.EMPTY_CANISTER = self._addResource("empty_canister", 60)
        self.EMPTY_FLUID_TANK = self._addResource("empty_fluid_tank", 225)
        self.IRON_REBAR = self._addResource("iron_rebar", 8)
        self.REINFORCED_IRON_PLATE = self._addResource("reinforced_iron_plate", 120)
        self.MODULAR_FRAME = self._addResource("modular_frame", 408)
        self.ENCASED_INDUSTRIAL_BEAM = self._addResource("encased_industrial_beam", 632)
        self.ALCAD_ALUMINUM_SHEET = self._addResource("alcad_aluminum_sheet", 266)
        self.ROTOR = self._addResource("rotor", 140)
        self.STATOR = self._addResource("stator", 240)
        self.MOTOR = self._addResource("motor", 1520)
        self.HEAT_SINK = self._addResource("heat_sink", 2804)
        self.SMART_PLATING = self._addResource("smart_plating", 520)
        self.VERSATILE_FRAMEWORK = self._addResource("versatile_framework", 1176)
        self.AUTOMATED_WIRING = self._addResource("automated_wiring", 1440)
        self.ASSEMBLY_DIRECTOR_SYSTEM = self._addResource("assembly_director_system", 0)
        self.ELECTROMAGNETIC_CONTROL_ROD = self._addResource("electromagnetic_control_rod", 2560)
        self.AI_LIMITER = self._addResource("ai_limiter", 920)
        self.CIRCUIT_BOARD = self._addResource("circuit_board", 696)
        self.COMPACTED_COAL = self._addResource("compacted_coal", 28)
        self.BLACK_POWDER = self._addResource("black_powder", 14)
        self.STUN_REBAR = self._addResource("stun_rebar", 186)
        self.SHATTER_REBAR = self._addResource("shatter_rebar", 332)
        self.NOBELISK = self._addResource("nobelisk", 152)
        self.RIFLE_AMMO = self._addResource("rifle_ammo", 25)
        self.HOMING_RIFLE_AMMO = self._addResource("homing_rifle_ammo", 855)
        self.TURBO_MOTOR = self._addResource("turbo_motor", 0)
        self.HEAVY_MODULAR_FRAME = self._addResource("heavy_modular_frame", 11520)
        self.COMPUTER = self._addResource("computer", 17260)
        self.SUPERCOMPUTER = self._addResource("supercomputer", 99576)
        self.CRYSTAL_OSCILLATOR = self._addResource("crystal_oscillator", 3072)
        self.RADIO_CONTROL_UNIT = self._addResource("radio_control_unit", 19600)
        self.MODULAR_ENGINE = self._addResource("modular_engine", 9960)
        self.ADAPTIVE_CONTROL_UNIT = self._addResource("adaptive_control_unit", 86120)
        self.MAGNETIC_FIELD_GENERATOR = self._addResource("magnetic_field_generator", 0)
        self.THERMAL_PROPULSION_ROCKET = self._addResource("thermal_propulsion_rocket", 0)
        self.URANIUM_FUEL_ROD = self._addResource("uranium_fuel_rod", 0)
        self.HIGH_SPEED_CONNECTOR = self._addResource("high_speed_connector", 3776)
        self.BEACON = self._addResource("beacon", 320)
        self.GAS_FILTER = self._addResource("gas_filter", 830)
        self.IODINE_INFUSED_FILTER = self._addResource("iodine_infused_filter", 2718)
        self.EXPLOSIVE_REBAR = self._addResource("explosive_rebar", 360)
        self.PLASTIC = self._addResource("plastic", 75)
        self.RUBBER = self._addResource("rubber", 60)
        self.PETROLEUM_COKE = self._addResource("petroleum_coke", 20)
        self.FUEL = self._addResource("fuel", 0)
        self.TURBOFUEL = self._addResource("turbofuel", 0)
        self.ALUMINA_SOLUTION = self._addResource("alumina_solution", 0)
        self.ALUMINUM_SCRAP = self._addResource("aluminum_scrap", 27)
        self.SULFURIC_ACID = self._addResource("sulfuric_acid", 0)
        self.FABRIC = self._addResource("fabric", 140)
        self.SMOKELESS_POWDER = self._addResource("smokeless_powder", 58)
        self.COOLING_SYSTEM = self._addResource("cooling_system", 0)
        self.FUSED_MODULAR_FRAME = self._addResource("fused_modular_frame", 62840)
        self.BATTERY = self._addResource("battery", 0)
        self.ENCASED_URANIUM_CELL = self._addResource("encased_uranium_cell", 0)
        self.HEAVY_OIL_RESIDUE = self._addResource("heavy_oil_residue", 0)
        self.POLYMER_RESIN = self._addResource("polymer_resin", 12)
        self.PACKAGED_WATER = self._addResource("packaged_water", 0)
        self.PACKAGED_OIL = self._addResource("packaged_oil", 0)
        self.PACKAGED_HEAVY_OIL_RESIDUE = self._addResource("packaged_heavy_oil_residue", 0)
        self.PACKAGED_FUEL = self._addResource("packaged_fuel", 270)
        self.PACKAGED_TURBOFUEL = self._addResource("packaged_turbofuel", 0)
        self.PACKAGED_ALUMINA_SOLUTION = self._addResource("packaged_alumina_solution", 0)
        self.PACKAGED_SULFURIC_ACID = self._addResource("packaged_sulfuric_acid", 0)
        self.PACKAGED_NITROGEN_GAS = self._addResource("packaged_nitrogen_gas", 0)
        # Cannot automate
        self.HOVER_PACK = self._addResource("hover_pack", 413920)

    def _loadTrades(self):
        self._addTrade("iron_ingot",[(self.IRON_ORE, 1)],[(self.IRON_INGOT, 1)])
        self._addTrade("copper_ingot",[(self.COPPER_ORE, 1)],[(self.COPPER_INGOT, 1)])
        self._addTrade("caterium_ingot",[(self.CATERIUM_ORE, 3)],[(self.CATERIUM_INGOT, 1)])
        self._addTrade("copper_alloy_ingot",[(self.COPPER_ORE, 10),(self.IRON_ORE, 5)],[(self.COPPER_INGOT, 20)])
        self._addTrade("steel_ingot",[(self.IRON_ORE, 3),(self.COAL, 3)],[(self.STEEL_INGOT, 3)])
        self._addTrade("solid_steel_ingot",[(self.IRON_INGOT, 2),(self.COAL, 2)],[(self.STEEL_INGOT, 3)])
        self._addTrade("aluminum_ingot",[(self.ALUMINUM_SCRAP, 6),(self.SILICA, 5)],[(self.ALUMINUM_INGOT, 4)])
        self._addTrade("iron_plate",[(self.IRON_INGOT, 3)],[(self.IRON_PLATE, 2)])
        self._addTrade("iron_rod",[(self.IRON_INGOT, 1)],[(self.IRON_ROD, 1)])
        self._addTrade("screw",[(self.IRON_ROD, 1)],[(self.SCREW, 4)])
        self._addTrade("cast_screw",[(self.IRON_INGOT, 5)],[(self.SCREW, 20)])
        self._addTrade("copper_sheet",[(self.COPPER_INGOT, 2)],[(self.COPPER_SHEET, 1)])
        self._addTrade("steel_beam",[(self.STEEL_INGOT, 4)],[(self.STEEL_BEAM, 1)])
        self._addTrade("steel_pipe",[(self.STEEL_INGOT, 3)],[(self.STEEL_PIPE, 2)])
        self._addTrade("aluminum_casing",[(self.ALUMINUM_INGOT, 3)],[(self.ALUMINUM_CASING, 2)])
        self._addTrade("wire",[(self.COPPER_INGOT, 1)],[(self.WIRE, 2)])
        self._addTrade("cable",[(self.WIRE, 2)],[(self.CABLE, 1)])
        self._addTrade("quickwire",[(self.CATERIUM_INGOT, 1)],[(self.QUICKWIRE, 5)])
        self._addTrade("concrete",[(self.LIMESTONE, 3)],[(self.CONCRETE, 1)])
        self._addTrade("quartz_crystal",[(self.RAW_QUARTZ, 5)],[(self.QUARTZ_CRYSTAL, 3)])
        self._addTrade("silica",[(self.RAW_QUARTZ, 3)],[(self.SILICA, 5)])
        self._addTrade("empty_canister",[(self.PLASTIC, 2)],[(self.EMPTY_CANISTER, 4)])
        self._addTrade("empty_fluid_tank",[(self.ALUMINUM_INGOT, 1)],[(self.EMPTY_FLUID_TANK, 1)])
        self._addTrade("iron_rebar",[(self.IRON_ROD, 1)],[(self.IRON_REBAR, 1)])
        self._addTrade("reinforced_iron_plate",[(self.IRON_PLATE, 6),(self.SCREW, 12)],[(self.REINFORCED_IRON_PLATE, 1)])
        self._addTrade("bolted_iron_plate",[(self.IRON_PLATE, 18),(self.SCREW, 50)],[(self.REINFORCED_IRON_PLATE, 3)])
        self._addTrade("adhered_iron_plate",[(self.IRON_PLATE, 3),(self.RUBBER, 1)],[(self.REINFORCED_IRON_PLATE, 1)])
        self._addTrade("modular_frame",[(self.REINFORCED_IRON_PLATE, 3),(self.IRON_ROD, 12)],[(self.MODULAR_FRAME, 2)])
        self._addTrade("steeled_frame",[(self.REINFORCED_IRON_PLATE, 2),(self.STEEL_PIPE, 10)],[(self.MODULAR_FRAME, 3)])
        self._addTrade("encased_industrial_beam",[(self.STEEL_BEAM, 4),(self.CONCRETE, 5)],[(self.ENCASED_INDUSTRIAL_BEAM, 1)])
        self._addTrade("alcad_aluminum_sheet",[(self.ALUMINUM_INGOT, 3),(self.COPPER_INGOT, 1)],[(self.ALCAD_ALUMINUM_SHEET, 3)])
        self._addTrade("rotor",[(self.IRON_ROD, 5),(self.SCREW, 25)],[(self.ROTOR, 1)])
        self._addTrade("copper_rotor",[(self.COPPER_SHEET, 6),(self.SCREW, 52)],[(self.ROTOR, 3)])
        self._addTrade("stator",[(self.STEEL_PIPE, 3),(self.WIRE, 8)],[(self.STATOR, 1)])
        self._addTrade("quickwire_stator",[(self.STEEL_PIPE, 4),(self.QUICKWIRE, 15)],[(self.STATOR, 2)])
        self._addTrade("motor",[(self.ROTOR, 2),(self.STATOR, 2)],[(self.MOTOR, 1)])
        self._addTrade("heat_sink",[(self.ALCAD_ALUMINUM_SHEET, 5),(self.COPPER_SHEET, 3)],[(self.HEAT_SINK, 1)])
        self._addTrade("smart_plating",[(self.REINFORCED_IRON_PLATE, 1),(self.ROTOR, 1)],[(self.SMART_PLATING, 1)])
        self._addTrade("versatile_framework",[(self.MODULAR_FRAME, 1),(self.STEEL_BEAM, 12)],[(self.VERSATILE_FRAMEWORK, 2)])
        self._addTrade("automated_wiring",[(self.STATOR, 1),(self.CABLE, 20)],[(self.AUTOMATED_WIRING, 1)])
        self._addTrade("assembly_director_system",[(self.ADAPTIVE_CONTROL_UNIT, 2),(self.SUPERCOMPUTER, 1)],[(self.ASSEMBLY_DIRECTOR_SYSTEM, 1)])
        self._addTrade("electromagnetic_control_rod",[(self.STATOR, 3),(self.AI_LIMITER, 2)],[(self.ELECTROMAGNETIC_CONTROL_ROD, 2)])
        self._addTrade("ai_limiter",[(self.COPPER_SHEET, 5),(self.QUICKWIRE, 20)],[(self.AI_LIMITER, 1)])
        self._addTrade("circuit_board",[(self.COPPER_SHEET, 2),(self.PLASTIC, 4)],[(self.CIRCUIT_BOARD, 1)])
        self._addTrade("electrode_circuit_board",[(self.RUBBER, 6),(self.PETROLEUM_COKE, 9)],[(self.CIRCUIT_BOARD, 1)])
        self._addTrade("caterium_circuit_board",[(self.PLASTIC, 10),(self.QUICKWIRE, 30)],[(self.CIRCUIT_BOARD, 7)])
        self._addTrade("compacted_coal",[(self.COAL, 5),(self.SULFUR, 5)],[(self.COMPACTED_COAL, 5)])
        self._addTrade("black_powder",[(self.COAL, 1),(self.SULFUR, 1)],[(self.BLACK_POWDER, 2)])
        self._addTrade("stun_rebar",[(self.IRON_REBAR, 1),(self.QUICKWIRE, 5)],[(self.STUN_REBAR, 1)])
        self._addTrade("shatter_rebar",[(self.IRON_REBAR, 2),(self.QUARTZ_CRYSTAL, 3)],[(self.SHATTER_REBAR, 1)])
        self._addTrade("nobelisk",[(self.BLACK_POWDER, 2),(self.STEEL_PIPE, 2)],[(self.NOBELISK, 1)])
        self._addTrade("rifle_ammo",[(self.COPPER_SHEET, 3),(self.SMOKELESS_POWDER, 2)],[(self.RIFLE_AMMO, 15)])
        self._addTrade("homing_rifle_ammo",[(self.RIFLE_AMMO, 20),(self.HIGH_SPEED_CONNECTOR, 1)],[(self.HOMING_RIFLE_AMMO, 10)])
        self._addTrade("turbo_motor",[(self.COOLING_SYSTEM, 4),(self.RADIO_CONTROL_UNIT, 2),(self.MOTOR, 4),(self.RUBBER, 24)],[(self.TURBO_MOTOR, 1)])
        self._addTrade("heavy_modular_frame",[(self.MODULAR_FRAME, 5),(self.STEEL_PIPE, 15),(self.ENCASED_INDUSTRIAL_BEAM, 5),(self.SCREW, 100)],[(self.HEAVY_MODULAR_FRAME, 1)])
        self._addTrade("heavy_flexible_frame",[(self.MODULAR_FRAME, 5),(self.ENCASED_INDUSTRIAL_BEAM, 3),(self.RUBBER, 20),(self.SCREW, 104)],[(self.HEAVY_MODULAR_FRAME, 1)])
        self._addTrade("heavy_encased_frame",[(self.MODULAR_FRAME, 8),(self.ENCASED_INDUSTRIAL_BEAM, 10),(self.STEEL_PIPE, 36),(self.CONCRETE, 22)],[(self.HEAVY_MODULAR_FRAME, 3)])
        self._addTrade("computer",[(self.CIRCUIT_BOARD, 10),(self.CABLE, 9),(self.PLASTIC, 18),(self.SCREW, 52)],[(self.COMPUTER, 1)])
        self._addTrade("supercomputer",[(self.COMPUTER, 2),(self.AI_LIMITER, 2),(self.HIGH_SPEED_CONNECTOR, 3),(self.PLASTIC, 28)],[(self.SUPERCOMPUTER, 1)])
        self._addTrade("crystal_oscillator",[(self.QUARTZ_CRYSTAL, 36),(self.CABLE, 28),(self.REINFORCED_IRON_PLATE, 5)],[(self.CRYSTAL_OSCILLATOR, 2)])
        self._addTrade("radio_control_unit",[(self.ALUMINUM_CASING, 32),(self.CRYSTAL_OSCILLATOR, 1),(self.COMPUTER, 1)],[(self.RADIO_CONTROL_UNIT, 2)])
        self._addTrade("modular_engine",[(self.MOTOR, 2),(self.RUBBER, 15),(self.SMART_PLATING, 2)],[(self.MODULAR_ENGINE, 1)])
        self._addTrade("adaptive_control_unit",[(self.AUTOMATED_WIRING, 15),(self.CIRCUIT_BOARD, 10),(self.HEAVY_MODULAR_FRAME, 2),(self.COMPUTER, 2)],[(self.ADAPTIVE_CONTROL_UNIT, 2)])
        self._addTrade("magnetic_field_generator",[(self.VERSATILE_FRAMEWORK, 5),(self.ELECTROMAGNETIC_CONTROL_ROD, 2),(self.BATTERY, 10)],[(self.MAGNETIC_FIELD_GENERATOR, 2)])
        self._addTrade("thermal_propulsion_rocket",[(self.MODULAR_ENGINE, 5),(self.TURBO_MOTOR, 2),(self.COOLING_SYSTEM, 6),(self.FUSED_MODULAR_FRAME, 2)],[(self.THERMAL_PROPULSION_ROCKET, 2)])
        self._addTrade("uranium_fuel_rod",[(self.ENCASED_URANIUM_CELL, 50),(self.ENCASED_INDUSTRIAL_BEAM, 3),(self.ELECTROMAGNETIC_CONTROL_ROD, 5)],[(self.URANIUM_FUEL_ROD, 1)])
        self._addTrade("high_speed_connector",[(self.QUICKWIRE, 56),(self.CABLE, 10),(self.CIRCUIT_BOARD, 1)],[(self.HIGH_SPEED_CONNECTOR, 1)])
        self._addTrade("beacon",[(self.IRON_PLATE, 3),(self.IRON_ROD, 1),(self.WIRE, 15),(self.CABLE, 2)],[(self.BEACON, 1)])
        self._addTrade("gas_filter",[(self.COAL, 5),(self.RUBBER, 2),(self.FABRIC, 2)],[(self.GAS_FILTER, 1)])
        self._addTrade("iodine_infused_filter",[(self.GAS_FILTER, 1),(self.QUICKWIRE, 8),(self.ALUMINUM_CASING, 1)],[(self.IODINE_INFUSED_FILTER, 1)])
        self._addTrade("explosive_rebar",[(self.IRON_REBAR, 2),(self.SMOKELESS_POWDER, 2),(self.STEEL_PIPE, 2)],[(self.EXPLOSIVE_REBAR, 1)])
        self._addTrade("plastic",[(self.CRUDE_OIL, 3)],[(self.PLASTIC, 2),(self.HEAVY_OIL_RESIDUE, 1)])
        self._addTrade("residual_plastic",[(self.POLYMER_RESIN, 6),(self.WATER, 2)],[(self.PLASTIC, 2)])
        self._addTrade("recycled_plastic",[(self.RUBBER, 6),(self.FUEL, 6)],[(self.PLASTIC, 12)])
        self._addTrade("rubber",[(self.CRUDE_OIL, 3)],[(self.RUBBER, 2),(self.HEAVY_OIL_RESIDUE, 2)])
        self._addTrade("residual_rubber",[(self.POLYMER_RESIN, 4),(self.WATER, 4)],[(self.RUBBER, 2)])
        self._addTrade("petroleum_coke",[(self.HEAVY_OIL_RESIDUE, 4)],[(self.PETROLEUM_COKE, 12)])
        self._addTrade("fuel",[(self.CRUDE_OIL, 6)],[(self.FUEL, 4),(self.POLYMER_RESIN, 3)])
        self._addTrade("residual_fuel",[(self.HEAVY_OIL_RESIDUE, 6)],[(self.FUEL, 4)])
        self._addTrade("turbofuel",[(self.FUEL, 6),(self.COMPACTED_COAL, 4)],[(self.TURBOFUEL, 5)])
        self._addTrade("wet_concrete",[(self.LIMESTONE, 6),(self.WATER, 5)],[(self.CONCRETE, 4)])
        self._addTrade("pure_copper_ingot",[(self.COPPER_ORE, 6),(self.WATER, 4)],[(self.COPPER_INGOT, 15)])
        self._addTrade("alumina_solution",[(self.BAUXITE, 12),(self.WATER, 18)],[(self.ALUMINA_SOLUTION, 12),(self.SILICA, 5)])
        self._addTrade("aluminum_scrap",[(self.ALUMINA_SOLUTION, 4),(self.COAL, 2)],[(self.ALUMINUM_SCRAP, 6),(self.WATER, 2)])
        self._addTrade("sulfuric_acid",[(self.SULFUR, 5),(self.WATER, 5)],[(self.SULFURIC_ACID, 5)])
        self._addTrade("polyster_fabric",[(self.POLYMER_RESIN, 1),(self.WATER, 1)],[(self.FABRIC, 1)])
        self._addTrade("steamed_copper_sheet",[(self.COPPER_INGOT, 3),(self.WATER, 3)],[(self.COPPER_SHEET, 3)])
        self._addTrade("smokeless_powder",[(self.BLACK_POWDER, 2),(self.HEAVY_OIL_RESIDUE, 1)],[(self.SMOKELESS_POWDER, 2)])
        self._addTrade("cooling_system",[(self.HEAT_SINK, 2),(self.RUBBER, 2),(self.WATER, 5),(self.NITROGEN_GAS, 25)],[(self.COOLING_SYSTEM, 1)])
        self._addTrade("fused_modular_frame",[(self.HEAVY_MODULAR_FRAME, 1),(self.ALUMINUM_CASING, 50),(self.NITROGEN_GAS, 25)],[(self.FUSED_MODULAR_FRAME, 1)])
        self._addTrade("battery",[(self.SULFURIC_ACID, 2.5),(self.ALUMINA_SOLUTION, 2),(self.ALUMINUM_CASING, 1)],[(self.BATTERY, 1),(self.WATER, 1.5)])
        self._addTrade("encased_uranium_cell",[(self.URANIUM, 10),(self.CONCRETE, 3),(self.SULFURIC_ACID, 8)],[(self.ENCASED_URANIUM_CELL, 5),(self.SULFURIC_ACID, 2)])
        self._addTrade("packaged_water",[(self.WATER, 2),(self.EMPTY_CANISTER, 2)],[(self.PACKAGED_WATER, 2)])
        self._addTrade("packaged_oil",[(self.CRUDE_OIL, 2),(self.EMPTY_CANISTER, 2)],[(self.PACKAGED_OIL, 2)])
        self._addTrade("packaged_heavy_oil_residue",[(self.HEAVY_OIL_RESIDUE, 2),(self.EMPTY_CANISTER, 2)],[(self.PACKAGED_HEAVY_OIL_RESIDUE, 2)])
        self._addTrade("packaged_fuel",[(self.FUEL, 2),(self.EMPTY_CANISTER, 2)],[(self.PACKAGED_FUEL, 2)])
        self._addTrade("packaged_turbofuel",[(self.TURBOFUEL, 2),(self.EMPTY_CANISTER, 2)],[(self.PACKAGED_TURBOFUEL, 2)])
        self._addTrade("packaged_alumina_solution",[(self.ALUMINA_SOLUTION, 2),(self.EMPTY_CANISTER, 2)],[(self.PACKAGED_ALUMINA_SOLUTION, 2)])
        self._addTrade("packaged_sulfuric_acid",[(self.SULFURIC_ACID, 2),(self.EMPTY_CANISTER, 2)],[(self.PACKAGED_SULFURIC_ACID, 2)])
        self._addTrade("packaged_nitrogen_gas",[(self.NITROGEN_GAS, 4),(self.EMPTY_FLUID_TANK, 1)],[(self.PACKAGED_NITROGEN_GAS, 1)])
        self._addTrade("unpackage_water",[(self.PACKAGED_WATER, 2)],[(self.WATER, 2),(self.EMPTY_CANISTER, 2)])
        self._addTrade("unpackage_oil",[(self.PACKAGED_OIL, 2)],[(self.CRUDE_OIL, 2),(self.EMPTY_CANISTER, 2)])
        self._addTrade("unpackage_heavy_oil_residue",[(self.PACKAGED_HEAVY_OIL_RESIDUE, 2)],[(self.HEAVY_OIL_RESIDUE, 2),(self.EMPTY_CANISTER, 2)])
        self._addTrade("unpackage_fuel",[(self.PACKAGED_FUEL, 2)],[(self.FUEL, 2),(self.EMPTY_CANISTER, 2)])
        self._addTrade("unpackage_turbofuel",[(self.PACKAGED_TURBOFUEL, 2)],[(self.TURBOFUEL, 2),(self.EMPTY_CANISTER, 2)])
        self._addTrade("unpackage_alumina_solution",[(self.PACKAGED_ALUMINA_SOLUTION, 2)],[(self.ALUMINA_SOLUTION, 2),(self.EMPTY_CANISTER, 2)])
        self._addTrade("unpackage_sulfuric_acid",[(self.PACKAGED_SULFURIC_ACID, 1)],[(self.SULFURIC_ACID, 1),(self.EMPTY_CANISTER, 1)])
        self._addTrade("unpackage_nitrogen_gas",[(self.PACKAGED_NITROGEN_GAS, 1)],[(self.NITROGEN_GAS, 4),(self.EMPTY_FLUID_TANK, 1)])
        # Cannot Automate
        self._addTrade("hover_pack",[(self.MOTOR, 8),(self.HEAVY_MODULAR_FRAME, 4),(self.COMPUTER,8),(self.ALCAD_ALUMINUM_SHEET,40)],[(self.HOVER_PACK, 1)])



    def getTrades(self):
        return self.trades

    def getResource(self, id):
        return self.resources[id]
