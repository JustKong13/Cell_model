# cartinine (crn) reactions

gbbtc = model.metabolites.get_by_id("gbbtn_c")
akg = model.metabolites.get_by_id("akg_c")
crn = model.metabolites.get_by_id("crn_c")
succ = model.metabolites.get_by_id("succ_c")
co2 = model.metabolites.get_by_id("co2_c")

l_carnitine_biosynthesis = Reaction("L-Carnitine-Biosynthesis")
l_carnitine_biosynthesis.name = "L-Carnitine-Biosynthesis"
l_carnitine_biosynthesis.add_metabolites(
    {
        gbbtc: -1.0,
        akg: -1.0,
        crn: 1.0,
        succ: 1.0,
        co2: 1.0
    }
)

model.add_reactions([l_carnitine_biosynthesis])
cobra.io.save_json_model(model, "./models/iML1515_crn.json")
model.optimize().objective_value
