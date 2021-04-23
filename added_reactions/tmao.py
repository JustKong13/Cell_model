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

model.add_reactions([rxn_12990])
cobra.io.save_json_model(model, "./models/iML1515_tmao.json")
model.optimize().objective_value
