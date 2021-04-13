# myo-inositol reactions
mi3p__D = Metabolite(
    "mi3p__D",
    formula="C6H11O9P",
    name="1D-myo-Inositol (3)-phosphate",
    compartment="c"
)
g6p = model.metabolites.get_by_id("g6p_c")
inost = model.metabolites.get_by_id("inost_c")
pi = model.metabolites.get_by_id("pi_c")
h2o = model.metabolites.get_by_id("h2o_c")

mi3ps = Reaction("MI3PS")
mi3ps.name = "Myo Inositol 1 phosphate synthase"
mi3ps.add_metabolites(
    {
        g6p: -1.0,
        mi3p__D: 1.0
    }
)

mi3pp = Reaction("MI3PP")
mi3pp.name = "Myo-inositol 1-phosphate"
mi3pp.add_metabolites(
    {
        h2o: -1.0,
        mi3p__D: -1.0,
        inost: 1.0,
        pi: 1.0
    }
)


model.add_reactions(
    [
        mi3ps, mi3pp
    ]
)

cobra.io.save_json_model(model, "model/iML1515_inost.json")
model.optimize().objective_value
