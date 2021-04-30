# Tyramine (Tym) reactions

# EC Number 4.1.1.25 https://biocyc.org/META/NEW-IMAGE?type=REACTION&object=TYROSINE-DECARBOXYLASE-RXN

tyr = model.metabolites.get_by_id("tyr__L_c")
h = model.metabolites.get_by_id("h_c")
co2 = model.metabolites.get_by_id("co2_c")
tym = Metabolite(
    "tym_c",
    formula="C8H12NO",
    name="Tyramine",
    compartment="c"
)

tyrosine_decarboxylase = Reaction("TDC")
tyrosine_decarboxylase.name = "Tyrosine Decarboxylase Reaction"
tyrosine_decarboxylase.add_metabolites(
    {
        tyr: -1.0,
        h: -1.0,
        co2: 1.0,
        tym: 1.0
    }
)

model.add_reactions([tyrosine_decarboxylase])
model.optimize().objective_value
