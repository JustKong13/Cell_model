# g15lac reactions

glc__D = model.metabolites.get_by_id("glc__D_c")
nad = model.metabolites.get_by_id("nad_c")
nadh = model.metabolites.get_by_id("nadh_c")
g15lac = Metabolite(
    "g15lac_c",
    formula="C6H10O6",
    name="D-glucono-1,5-lactone",
    compartment="c"
)
h = model.metabolites.get_by_id("h_c")

g1dx = Reaction("G1Dx")
g1dx.name = "Glucose 1 dehydrogenase NAD"
g1dx.add_metabolites(
    {
        glc__D: -1.0,
        nad: -1.0,
        g15lac: 1.0,
        h: 1.0,
        nadh: 1.0
    }
)

model.add_reactions([g1dx])
cobra.io.save_json_model(model, "./models/iML1515_g15lac.json")
