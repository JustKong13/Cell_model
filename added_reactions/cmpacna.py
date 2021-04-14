# cmpacna reactions


# EC number 2.5.1.56 https://biocyc.org/META/NEW-IMAGE?type=REACTION&object=N-ACETYLNEURAMINATE-SYNTHASE-RXN

pep = model.metabolites.get_by_id("pep_c")
acmana = model.metabolites.get_by_id("acmana_c")
h2o = model.metabolites.get_by_id("h2o_c")
ncma = Metabolite(
    "ncma_c",
    formula="C11H18NO9",
    name="N-acetyl-β-neuraminate",
    compartment="c"
)
pi = model.metabolites.get_by_id("pi_c")

N_acetylneuraminate_synthesis_rxn = Reaction("ACES")
N_acetylneuraminate_synthesis_rxn.name = "N-ACETYLNEURAMINATE SYNTHASE RXN"
N_acetylneuraminate_synthesis_rxn.add_metabolites(
    {
        pep: -1.0,
        acmana: -1.0,
        h2o: -1.0,
        ncma: 1.0,
        pi: 1.0
    }
)



# EC number 2.7.7.43 https://biocyc.org/META/NEW-IMAGE?type=REACTION&object=RXN-9990

ncma = ncma
ctp = model.metabolites.get_by_id("ctp_c")
cmpacna = Metabolite(
    "cmpacna",
    formula="C20H29N4O16P",
    name="CMP-N-acetyl-β-neuraminate",
    compartment="c"
)
ppi = model.metabolites.get_by_id("ppi_c")

cmpacna_production_rxn = Reaction("CMPACNA_rxn")
cmpacna_production_rxn.name = "N-acylneuraminate cytidylyltransferase"
cmpacna_production_rxn.add_metabolites(
    {
        ncma: -1.0,
        ctp: -1.0,
        cmpacna: 1.0,
        ppi: 1.0

    }
)




model.add_reactions(
    [
        N_acetylneuraminate_synthesis_rxn, cmpacna_production_rxn
    ]
)

cobra.io.save_json_model(model, "iML1515_cmpacna.json")

model.optimize().objective_value
