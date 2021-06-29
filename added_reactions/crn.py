# cartinine (crn) reactions

# EC Number 1.14.11.1 https://metacyc.org/META/NEW-IMAGE?type=EC-NUMBER&object=EC-1.14.11.1 

gbbtc = model.metabolites.get_by_id("gbbtn_c")
akg = model.metabolites.get_by_id("akg_c")
crn = model.metabolites.get_by_id("crn_c")
succ = model.metabolites.get_by_id("succ_c")
co2 = model.metabolites.get_by_id("co2_c")

l_carnitine_biosynthesis = Reaction("L-Carnitine-Biosynthesis")
l_carnitine_biosynthesis.name = "L-Carnitine-Biosynthesis"
l_carnitine_biosynthesis.add_metabolites(
    {
        gbbtc: -1.0,
        akg: -1.0,
        crn: 1.0,
        succ: 1.0,
        co2: 1.0
    }
)

# EC Number 1.3.8.13 https://biocyc.org/META/NEW-IMAGE?type=REACTION&object=CROBETREDUCT-RXN

bbtcoa = model.metabolites.get_by_id("bbtcoa_c")
nadph = model.metabolites.get_by_id("nadph_c")
h = model.metabolites.get_by_id("h_c")
ctbtcoa = model.metabolites.get_by_id("ctbtcoa_c")

crobetreduct_rxn = Reaction("CROBETREDUCT-RXN")
crobetreduct_rxn.name = "CROBETREDUCT RXN"
crobetreduct_rxn.add_metabolites(
    {
        bbtcoa: -1.0,
        nadph: -1.0,
        h: -1.0,
        nadph: 1.0,
        ctbtcoa: 1.0,
    }
)

model.add_reactions([l_carnitine_biosynthesis, crobetreduct_rxn])
model.optimize().objective_value

cobra.io.save_json_model(model, "./models/IMPROVED_iML1515.json")
