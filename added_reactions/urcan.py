reaction = Reaction('urcan')
reaction.name = 'Test 1'

Histidine = model.metabolites.get_by_id('his__L_c')
Ammonium = model.metabolites.get_by_id('nh4_c')
Urocanate = Metabolite(
    'urocanate',
    formula = 'C6H5N2O2',
    name = 'urocanate',
    compartment = 'c')

reaction.add_metabolites({
    Histidine: -1.0,
    Ammonium: 1.0,
    Urocanate: 1.0})

model.add_reactions([reaction])

cobra.io.save_json_model(model, 'iml1515_urcan_reaction.json')
#
