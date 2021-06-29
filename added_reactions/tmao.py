# Trimethylamine N-oxide (tamo) Reactions

# EC Number 1.14.13.148 https://biocyc.org/META/NEW-IMAGE?type=REACTION&object=RXN-12900

tma = model.metabolites.get_by_id("tma_c")
nadph = model.metabolites.get_by_id("nadph_c")
o2 = model.metabolites.get_by_id("o2_c")
tmao = model.metabolites.get_by_id("tmao_c")
h2o = model.metabolites.get_by_id("h2o_c")

rxn_12990 = Reaction("rxn_12900") # Bigg ID for reaction
rxn_12990.name = "RXN-12900"
rxn_12990.add_metabolites(
    {
        tma: -1.0,
        nadph: -1.0,
        o2: 1.0,
        tmao: 1.0,
        h2o: 1.0
    }
)

# EC Number 1.14.13.239 https://biocyc.org/META/NEW-IMAGE?type=REACTION&object=RXN-5921

crn = model.metabolites.get_by_id("crn_c")
nadph = model.metabolites.get_by_id("nadph_c")
o2 = model.metabolites.get_by_id("o2_c")
h = model.metabolites.get_by_id("h_c")
msal__L = Metabolite(
    "msal__L_c",
    formula="C4H5O4",
    name="L-malic semialdehyde",
    compartment="c"
)
tma = model.metabolites.get_by_id("tma_c")
nadp = model.metabolites.get_by_id("nadp_c")
h2o = model.metabolites.get_by_id("h2o_c")

rxn_5921 = Reaction("rxn_5921")
rxn_5921.name = "RXN-5921"
rxn_5921.add_metabolites(
    {
        crn: -1.0,
        nadph: -1.0,
        o2: -1.0,
        h: -1.0,
        msal__L: 1.0,
        tma: 1.0,
        nadp: 1.0,
        h2o: 1.0
    }
)

# EC Number 1.14.13.239 https://biocyc.org/META/NEW-IMAGE?type=REACTION&object=RXN-18258

gbbtn = model.metabolites.get_by_id("gbbtn_c")
nadph = model.metabolites.get_by_id("nadph_c")
o2 = model.metabolites.get_by_id("o2_c")
h = model.metabolites.get_by_id("h_c")
sucsal = model.metabolites.get_by_id("sucsal_c")
tma = model.metabolites.get_by_id("tma_c")
nadp = model.metabolites.get_by_id("nadp_c")
h2o = model.metabolites.get_by_id("h2o_c")

rxn_18258 = Reaction("RXN-18258")
rxn_18258.name = "RXN-18258"
rxn_18258.add_metabolites(
    {
        gbbtn: -1.0,
        nadph: -1.0,
        o2: -1.0,
        h: -1.0,
        sucsal: 1.0,
        tma: 1.0,
        nadp: 1.0,
        h2o: 1.0
    }
)

# EC Number 1.14.13.239 https://biocyc.org/META/NEW-IMAGE?type=REACTION&object=RXN-18376 

chol = model.metabolites.get_by_id("chol_c")
nadph = model.metabolites.get_by_id("nadph_c")
o2 = model.metabolites.get_by_id("o2_c")
h = model.metabolites.get_by_id("h_c")
gcald = model.metabolites.get_by_id("gcald_c")
tma = model.metabolites.get_by_id("tma_c")
nadp = model.metabolites.get_by_id("nadp_c")
h2o = model.metabolites.get_by_id("h2o_c")

rxn_18376 = Reaction("RXN-18376")
rxn_18376.name = "RXN-18376"
rxn_18376.add_metabolites(
    {
        chol: -1.0,
        nadph: -1.0,
        o2: -1.0,
        h: -1.0,
        gcald: 1.0,
        tma: 1.0,
        nadp: 1.0,
        h2o: 1.0
    }
)


model.add_reactions([rxn_12990, rxn_5921, rxn_18258, rxn_18376])
cobra.io.save_json_model(model, "./models/iML1515_tmao.json")
model.optimize().objective_value
