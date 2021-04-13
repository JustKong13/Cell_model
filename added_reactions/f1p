# f1p reactions
atp = model.metabolites.get_by_id("atp_c")
fru = model.metabolites.get_by_id("fru_c")
adp = model.metabolites.get_by_id("adp_c")
f1p = model.metabolites.get_by_id("f1p_c")
h = model.metabolites.get_by_id("h_c")

khk = Reaction("KHK")
khk.name = "Ketohexokinase"
khk.add_metabolites(
    {
        adp: 1.0,
        atp: -1.0,
        f1p: 1.0,
        fru: -1.0,
        h: 1.0
    }
)

biomass_rxn.add_metabolites(
    {
        f1p: -0.1030074288
    }
)

model.add_reactions(
    [
        khk, biomass_rxn
    ]
)

model.optimize().objective_value
