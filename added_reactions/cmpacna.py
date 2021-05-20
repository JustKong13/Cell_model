# cmpacna reactions "cmpacna_c": 0.08657083577

# EC number 5.3.1.19 https://biocyc.org/META/NEW-IMAGE?type=REACTION&object=L-GLN-FRUCT-6-P-AMINOTRANS-RXN

f6p = model.metabolites.get_by_id("f1p_c")
gln__L = model.metabolites.get_by_id("gln__L_c")
gam6p = model.metabolites.get_by_id("gam6p_c")
glu__L= model.metabolites.get_by_id("glu__L_c")

l_gln_fruct_6_p_aminotrans_rxn = Reaction("L-GLN-FRUCT-6-P-AMINOTRANS-RXN")
l_gln_fruct_6_p_aminotrans_rxn.name = "L-GLN-FRUCT-6-P-AMINOTRANS-RXN"
l_gln_fruct_6_p_aminotrans_rxn.add_metabolites(
    {
        f6p: -1.0,
        gln__L: -1.0,
        gam6p: 1.0,
        glu__L:1.0
    }
)

# EC number 5.4.2.10 https://biocyc.org/gene?orgid=META&id=EG11553#tab=RXNS

gam6p = model.metabolites.get_by_id("gam6p_c")
gam1p = model.metabolites.get_by_id("gam1p_c")

rxn_5_4_2_10 = Reaction("5.4.2.10-RXN")
rxn_5_4_2_10.name = "rxn_5_4_2_10"
rxn_5_4_2_10.subsystem = "UDP-N-acetyl-D-glucosamine biosynthesis I",
rxn_5_4_2_10.add_metabolites(
    {
        gam6p:-1.0,
        gam1p:1.0
    }
)

# EC number 2.3.1.157 https://biocyc.org/META/NEW-IMAGE?type=REACTION&object=2.3.1.157-RXN

accoa = model.metabolites.get_by_id("accoa_c")
gam1p = model.metabolites.get_by_id("gam1p_c")
acgam1p = model.metabolites.get_by_id("acgam1p_c")
coa = model.metabolites.get_by_id("coa_c")
h = model.metabolites.get_by_id("h_c")

rxn_2_3_1_157 = Reaction("2.3.1.157-RXN")
rxn_2_3_1_157.name = "2.3.1.157-RXN"
rxn_2_3_1_157.subsystem = "UDP-N-acetyl-D-glucosamine biosynthesis I"
rxn_2_3_1_157.add_metabolites(
    {
        accoa: -1.0,
        gam1p: -1.0,
        acgam1p: 1.0,
        coa: 1.0,
        h: 1.0
    }
)

# EC number 2.7.7.23 https://biocyc.org/META/NEW-IMAGE?type=REACTION&object=NAG1P-URIDYLTRANS-RXN

utp = model.metabolites.get_by_id("utp_c")
acgam1p = model.metabolites.get_by_id("acgam1p_c")
h = model.metabolites.get_by_id("h_c")
uacgam = model.metabolites.get_by_id("uacgam_c")
ppi = model.metabolites.get_by_id("ppi_c")

nag1p_uridyltrans_rxn = Reaction("NAG1P-URIDYLTRANS-RXN")
nag1p_uridyltrans_rxn.name = "NAG1P-URIDYLTRANS-RXN"
nag1p_uridyltrans_rxn.subsystem = "UDP-N-acetyl-D-glucosamine biosynthesis I"
nag1p_uridyltrans_rxn.add_metabolites(
    {
        utp: -1.0,
        acgam1p: -1.0,
        h:-1.0,
        uacgam: 1.0,
        ppi: 1.0
    }
)

# EC number 3.2.1.183 https://biocyc.org/META/NEW-IMAGE?type=REACTION&object=RXN-9987 

uacgam = model.metabolites.get_by_id("uacgam_c")
h2o = model.metabolites.get_by_id("h2o_c")
acmana = model.metabolites.get_by_id("acmana_c")
udp = model.metabolites.get_by_id("udp_c")
h = model.metabolites.get_by_id("h_c")

rxn_9987 = Reaction("RXN-9987")
rxn_9987.name = "RXN-9987"
rxn_9987.subsystem = "CMP-N-acetylneuraminate biosynthesis II"
rxn_9987.add_metabolites(
    {
        uacgam: -1.0,
        h2o: -1.0,
        acmana: 1.0,
        udp: 1.0,
        h: 1.0
    }
)


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
N_acetylneuraminate_synthesis_rxn.subsystem = "CMP-N-acetylneuraminate biosynthesis II"
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
    "cmpacna_c",
    formula="C20H29N4O16P",
    name="CMP-N-acetyl-β-neuraminate",
    compartment="c"
)
ppi = model.metabolites.get_by_id("ppi_c")

cmpacna_production_rxn = Reaction("CMPACNA_rxn")
cmpacna_production_rxn.name = "N-acylneuraminate cytidylyltransferase"
cmpacna_production_rxn.subsystem = "CMP-N-acetylneuraminate biosynthesis II"
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
        cmpacna_production_rxn, N_acetylneuraminate_synthesis_rxn, rxn_9987, nag1p_uridyltrans_rxn, rxn_2_3_1_157, rxn_5_4_2_10, l_gln_fruct_6_p_aminotrans_rxn
    ]
)

model.optimize().objective_value
cobra.io.save_json_model(model, "./models/iML1515_cmpacna.json")
