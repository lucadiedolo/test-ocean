from dimod import Binary, quicksum, ConstrainedQuadraticModel
from dwave.system import LeapHybridCQMSampler

num_customer = 5
num_facility = 3

demand = [80, 270, 250, 160, 180]
open_cost = [1000, 1000, 1000]
capacity = [500, 500, 500]

cost = [
    [4, 6, 9],
    [5, 4, 7],
    [6, 3, 4],
    [8, 5, 3],
    [10, 8, 4]
]


y = [Binary(f"y[{f}]") for f in range(num_facility)]
z = [[Binary(f"z[{c},{f}]") for f in range(num_facility)] for c in range(num_customer)]

objective = quicksum(open_cost[f] * y[f] for f in range(num_facility)) + quicksum(cost[c][f] * demand[c] * z[c][f] for f in range(num_facility) for c in range(num_customer))

link_constraints = [z[c][f] - y[f] <= 0 for f in range(num_facility) for c in range(num_customer)]
demand_constraints = [quicksum(z[c][f] for f in range(num_facility)) == 1 for c in range(num_customer)]
capacity_constraints = [quicksum(demand[c] * z[c][f] for c in range(num_customer)) <= capacity[f] for f in range(num_facility)]

cqm = ConstrainedQuadraticModel()

cqm.set_objective(objective)

for c in link_constraints:
    cqm.add_constraint(c)

for c in capacity_constraints:
    cqm.add_constraint(c)

for c in demand_constraints:
    cqm.add_constraint(c)

# cqm_sampler = LeapHybridCQMSampler()
# sampleset = cqm_sampler.sample_cqm(cqm, label="test")
#
# print(sampleset.info)
