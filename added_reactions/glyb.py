# Betaine (glyb) reactions

# EC Number 1.2.1.8 https://biocyc.org/META/NEW-IMAGE?type=REACTION&object=BADH-RXN

betald = model.metabolites.get_by_id("betald_c")
nad = model.metabolites.get_by_id("nad_c")
h2o = model.metabolites.get_by_id("h2o_c")
glyb = model.metabolites.get_by_id("glyb_c")
nadh = model.metabolites.get_by_id("nadh_c")
h = model.metabolites.get_by_id("h_c")

badh_rxn = Reaction("BADH-RXN")
badh_rxn.name = "Betaine Aldehyde dehydrogenase"
badh_rxn.add_metabolites(
    {
        betald: -1.0,
        nad: -1.0,
        h2o: -1.0,
        glyb: 1.0,
        nadh: 1.0,
        h: 2.0
    }
)

# EC number 1.1.99.1 https://biocyc.org/META/NEW-IMAGE?type=REACTION&object=CHD-RXN

chol = model.metabolites.get_by_id("chol_c")
betald = betald
h = h

chd_rxn = Reaction("CHD-RXN")
chd_rxn.name = "Choline dehydrogenase"
chd_rxn.add_metabolites(
    {
        chol: -1.0,
        betald: 1.0,
        h: 2.0
    }
)

# There is no explaination for the synthesis of choline 

model.add_reactions([badh_rxn, chd_rxn])

model.optimize().objective_value
cobra.io.save_json_model(model, "./models/iML1515_glyb.json")
