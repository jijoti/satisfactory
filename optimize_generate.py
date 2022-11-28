from scipy.optimize import linprog
from pulp import LpMaximize, LpProblem, LpStatus, lpSum, LpVariable
from satisfactory_data import Resource, ResourceStack, Trade 
from satisfactory_data import StaticSatisfactoryDataLoader, SatisfactoryResourceFactory, SatisfactoryTradeFactory 

# Create the model
model = LpProblem(name="small-problem", sense=LpMaximize)

rf = SatisfactoryResourceFactory()
tf = SatisfactoryTradeFactory()
data = StaticSatisfactoryDataLoader(rf, tf)
data.load()
trades = data.getTrades()

available_resources = {}
available_resources[data.IRON_ORE.getId()] = 6000 
available_resources[data.COPPER_ORE.getId()] = 6000 
available_resources[data.CATERIUM_ORE.getId()] = 6000 
available_resources[data.RAW_QUARTZ.getId()] = 6000 
available_resources[data.LIMESTONE.getId()] = 6000 
available_resources[data.COAL.getId()] = 6000 
available_resources[data.SULFUR.getId()] = 6000 
available_resources[data.CRUDE_OIL.getId()] = 6000 
available_resources[data.BAUXITE.getId()] = 6000 
available_resources[data.WATER.getId()] = 6000 
available_resources[data.NITROGEN_GAS.getId()] = 6000 
available_resources[data.URANIUM.getId()] = 6000 

maximize_array = []
kept_resources = {}
made_resources = {}
iterations = {}
used_in_index = {}

def maybeAddKeptResource(resource):
    if resource.getId() in kept_resources:
        return
    kept_resource = LpVariable(name="kept_" + str(resource), lowBound=0)
    if resource.getMetadata("sink_points") != 0:
        maximize_array.append(kept_resource * resource.getMetadata("sink_points"))
    kept_resources[resource.getId()] = kept_resource

def addMadeResource(resource, trade_name):
    if resource.getId() not in made_resources:
        made_resources[resource.getId()] = []
    made_resource = LpVariable(name="made_" + str(resource) + "(" + trade_name + ")", lowBound=0)
    made_resources[resource.getId()].append(made_resource)
    return made_resource

def constrainOutputToIterations(model, made_resource, iteration):
    if output.getAmount() != 1:
        model += (made_resource * 1/output.getAmount() == iteration)
    else:
        model += (made_resource == iteration)

def addToUsedInIndex(input, made_resource, made_amount):
    if input.getResource().getId() not in used_in_index:
        used_in_index[input.getResource().getId()] = []
    used_in_index[input.getResource().getId()].append(input.getAmount() / made_amount * made_resource)

for trade in trades:
    iteration = LpVariable(name=str(trade) + "_iterations", lowBound=0, cat="Integer")
    iterations[trade.getId()] = iteration
    made_resource = None
    made_amount = None

    for output in trade.getOutput():
        maybeAddKeptResource(output.getResource())
        made_resource = addMadeResource(output.getResource(), str(trade))
        constrainOutputToIterations(model, made_resource, iteration)
        made_amount = output.getAmount()

    for input in trade.getInput():
        maybeAddKeptResource(input.getResource())
        addToUsedInIndex(input, made_resource, made_amount)


for id, resource in kept_resources.items():
    start_amount = 0
    if id in available_resources:
        start_amount = available_resources[id]    
    used = []
    if id in used_in_index:
        used = used_in_index[id]
    made = []
    if id in made_resources:
        made = made_resources[id]
    model += resource + sum(used) == sum(made) + start_amount

model += lpSum(maximize_array)

# Solve the problem
status = model.solve()

print(f"status: {model.status}, {LpStatus[model.status]}")
print(f"objective: {model.objective.value()}")
print("-")
for id, amount in available_resources.items():
    print(f"start_{data.getResource(id)}: {amount}")
print("-")
for var in model.variables():
    if round(var.value(),8) != 0 and "iterations" in var.name:
        print(f"{var.name}: {var.value()}")
print("-")
for var in model.variables():
    if round(var.value(),8) != 0 and "made" in var.name:
        print(f"{var.name}: {var.value()}")
print("-")
for var in model.variables():
    if round(var.value(),8) != 0 and "kept" in var.name:
        print(f"{var.name}: {var.value()}")
#for name, constraint in model.constraints.items():
#    print(f"{name}: {constraint.value()}")
