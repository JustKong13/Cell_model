# guanidinoacetate reaction

# EC number 2.1.4.1 https://biocyc.org/META/NEW-IMAGE?type=REACTION&object=GLYCINE-AMIDINOTRANSFERASE-RXN

arg__L = model.metabolites.get_by_id("arg__L_c")
gly = model.metabolites.get_by_id("gly_c")
guanidinoacetate = Metabolite(
    "guanidinoacetate_c",
    formula="C3H7N3O2",
    name="guanidinoacetate",
    compartment="c"
)
orn = model.metabolites.get_by_id("orn_c")

glyaminotranferase = Reaction("GLYCINE-AMIDINOTRANSFERASE-RXN")
glyaminotranferase.name = "GLYCINE AMIDINOTRANSFERASE RXN"
glyaminotranferase.add_metabolites(
    {
        arg__L: -1.0,
        gly: -1.0,
        guanidinoacetate: 1.0,
        orn:1.0
    }
)

model.add_reactions([glyaminotranferase]
