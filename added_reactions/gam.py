# glucosamine (gam) reactions

# EC Number 3.1.3.- https://metacyc.org/META/NEW-IMAGE?type=REACTION&object=RXN-17745

gam6p = model.metabolites.get_by_id("gam6p_c")
h2o = model.metabolites.get_by_id("h2o_c")
gam = model.metabolites.get_by_id("gam_c")
pi = model.metabolites.get_by_id("pi_c")

phosphoric_monoester_hydrolases = Reaction("Phosphoric-Monoester_hydrolases")
phosphoric_monoester_hydrolases.name = "Phosphoric Monoester Hydrolases"
phosphoric_monoester_hydrolases.add_metabolites(
    {
        gam6p: -1.0,
        h2o: -1.0,
        gam: 1.0,
        pi: 1.0
    }
)

model.add_reactions([phosphoric_monoester_hydrolases])
cobra.io.save_json_model(model, "./models/iML1515_gam.json")
