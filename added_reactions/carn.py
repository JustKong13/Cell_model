# Carnosine (carn) reactions

ala_B = model.metabolites.get_by_id("ala_B_c")
his__L = model.metabolites.get_by_id("his__L_c")
atp = model.metabolites.get_by_id("atp_c")
carn = Metabolite(
        "carn",
        formula="C9H14N4O3",
        name="carnosine",
        compartment="c"
)
adp = model.metabolites.get_by_id("adp_c")
pi = model.metabolites.get_by_id("pi_c")
h = model.metabolites.get_by_id("h_c")

carnosine_synthase_reaction = Reaction("CARNOSINE-SYNTHASE-RXN")
carnosine_synthase_reaction.name = "Carnosine Synthase Reaction"
carnosine_synthase_reaction.add_metabolites(
    {
        ala_B: -1.0,
        his__L: -1.0,
        atp: -1.0,
        carn: 1.0,
        adp: 1.0,
        pi: 1.0,
        h: 1.0
    }
)

model.add_reactions([carnosine_synthase_reaction])
cobra.io.save_json_model(model, "./models/iML1515_carn.json")
