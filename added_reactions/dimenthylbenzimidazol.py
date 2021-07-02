# 5,6-Dimenthylbenzimidazol reactions
FMNH = model.metabolites.get_by_id("fmnh2_c")
O2 = model.metabolites.get_by_id("o2_c")

derythrosefourphosphate = model.metabolites.get_by_id("e4p_c")
h = model.metabolites.get_by_id("h_c")
Dmbd = model.metabolites.get_by_id("dmbzid_c")

dialurate = Metabolite(
    'dialurate_c',
    formula = 'C4H4N2O4',
    name = 'dialurate',
    compartment = 'c')


dimethy = Reaction("5,6-dimethylbenzimidazole")
dimethy.name = "5,6-dimethylbenzimidazole"
dimethy.add_metabolites({
        FMNH: -1.0,
        O2: -1.0,
        
        h: 1.0,
        derythrosefourphosphate: 1.0,
        Dmbd: 1.0,
        dialurate: 1.0
        })



model.add_reactions([dimethy])
cobra.io.save_json_model(model, 'dimethy_iML1515.json')

model.optimize().objective_value
