# trans-Cinnamate (cinnm) reaction

# EC Number 4.3.1.25 https://biocyc.org/META/NEW-IMAGE?type=REACTION&object=PHENYLALANINE-AMMONIA-LYASE-RXN

phe__L = model.metabolites.get_by_id("phe__L_c")
cinnm = model.metabolites.get_by_id("cinnm_c")
nh4 = model.metabolites.get_by_id("nh4_c")

phenylalanine_ammonia_lyase = Reaction("PAL")
phenylalanine_ammonia_lyase.name = "Phenylalanine Ammonia Lyase Reaction"
phenylalanine_ammonia_lyase.add_metabolites(
    {
        phe__L: -1.0,
        cinnm: 1.0,
        nh4: 1.0
    }
)
model.add_reactions([phenylalanine_ammonia_lyase])
cobra.io.save_json_model(model, "./models/iML1515_cinnm.json")
model.optimize().objective_value
