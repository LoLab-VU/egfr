"""
Model M1a: Extrinsic apoptosis model with "embedded together" model of MOMP.
"""


from pysb import *
import pickle

#from egfr import shared
Model()
from . import chen_modules_Rexer_EGF_noactErbB2

# Declare monomers
chen_modules_Rexer_EGF_noactErbB2.rec_monomers()
chen_modules_Rexer_EGF_noactErbB2.mapk_monomers()
chen_modules_Rexer_EGF_noactErbB2.akt_monomers()
chen_modules_Rexer_EGF_noactErbB2.crosstalk_monomers()

# Generate the upstream and downstream sections
chen_modules_Rexer_EGF_noactErbB2.rec_events()
chen_modules_Rexer_EGF_noactErbB2.mapk_events()
chen_modules_Rexer_EGF_noactErbB2.akt_events()
chen_modules_Rexer_EGF_noactErbB2.crosstalk_events()

# Initial protein concentrations
chen_modules_Rexer_EGF_noactErbB2.rec_initial_inhib_LAP()
chen_modules_Rexer_EGF_noactErbB2.rec_initial_lig_pEGF()
chen_modules_Rexer_EGF_noactErbB2.rec_initial()
chen_modules_Rexer_EGF_noactErbB2.mapk_initial()
chen_modules_Rexer_EGF_noactErbB2.akt_initial()
chen_modules_Rexer_EGF_noactErbB2.crosstalk_initial()

#Declare observables
Observable('obsAKTPP', AKT(S='PP'))
Observable('obsAKTP', AKT(S='P'))
Observable('obsAKT', AKT())
Observable('obsErbB1_P_CE', erbb(ty='1', st='P'))
Observable('obsErbB1', erbb(ty='1'))
Observable('obsErbB2_P_CE', erbb(ty='2', st='P'))
Observable('obsErbB2', erbb(ty='2'))
Observable('obsERKPP', ERK(st='PP'))
Observable('obsMEK', MEK())
Observable('obsPDK1', PDK1())
Observable('obsPI3K', PI3K())
Observable('obsPTEN', PTEN())

# # Observable('obsEGF', EGF())

# Observable('obsErbB1_lig', erbb(bd=None, ty='1', st='U', bl=ANY))
# Observable('obsErbB1_ErbB', erbb(bd=1, ty='1', st='U') % erbb(bd=1, st='U'))
# Observable('obsErbB1_ErbB1', erbb(bd=1, ty='1', st='U') % erbb(bd=1, ty='1', st='U'))
# Observable('obsErbB1_ErbB2', erbb(bd=1, ty='1', st='U') % erbb(bd=1, ty='2', st='U'))
# Observable('obsErbB1_ErbB3', erbb(bd=1, ty='1', st='U') % erbb(bd=1, ty='3', st='U'))
# Observable('obsErbB1_ErbB4', erbb(bd=1, ty='1', st='U') % erbb(bd=1, ty='4', st='U'))
# Observable('obsErbB1_ErbB_ATP', erbb(bd=1, ty='1', st='U', b=2) % erbb(bd=1, st='U') % ATP(b=2))

# Observable('obsErbB_GAP_GRB2', erbb(bd=1) % erbb(bd=1) % GAP(bgrb2=2) % GRB2(bgap=2, bsos=None))
# Observable('obsErbB_GAP_GRB2_GAB1U', erbb(bd=1) % erbb(bd=1) % GAP(bgrb2=2) % GRB2(bgap=2, bgab1=3) % GAB1(bgrb2=3, S='U'))
# Observable('obsErbB_GAP_GRB2_GAB1P', erbb(bd=1) % erbb(bd=1) % GAP(bgrb2=2) % GRB2(bgap=2, bgab1=3) % GAB1(bgrb2=3, S='P'))
# Observable('obsErbB_GAP_GRB2_GAB1P_PI3K', erbb(bd=1) % erbb(bd=1) % GAP(bgrb2=2) % GRB2(bgap=2, bgab1=3) % GAB1(bgrb2=3, S='P', bpi3k=4) % PI3K(bgab1=4))
# Observable('obsPIP3', PIP(S='PIP3'))
# Observable('obsAKT_PIP3', AKT(bpip3=1, S='U') % PIP(S='PIP3', bakt=1))
# Observable('obsAKTP', AKT(S='P'))

# Observable('obsErbB_GAP_GRB2_SOS', erbb(bd=1) % erbb(bd=1) % GAP(bgrb2=2) % GRB2(bgap=2, bsos=3) % SOS(bras=None, bgrb=3, bERKPP=None, st='U'))
# Observable('obsErbB_GAP_SHCP', erbb(bd=1) % erbb(bd=1) % GAP(bgrb2=None, b=2) % SHC(batp=None, st='P', bgrb=None, bgap=2))
# Observable('obsErbB11_GAP_GRB2', erbb(bd=1, ty='1') % erbb(bd=1, ty='1') % GAP(bgrb2=2) % GRB2(bgap=2, bsos=None))
# Observable('obsErbB12_GAP_GRB2', erbb(bd=1, ty='1') % erbb(bd=1, ty='2') % GAP(bgrb2=2) % GRB2(bgap=2, bsos=None))
# Observable('obsErbB13_GAP_GRB2', erbb(bd=1, ty='1') % erbb(bd=1, ty='3') % GAP(bgrb2=2) % GRB2(bgap=2, bsos=None))
# Observable('obsErbB14_GAP_GRB2', erbb(bd=1, ty='1') % erbb(bd=1, ty='4') % GAP(bgrb2=2) % GRB2(bgap=2, bsos=None))
# Observable('obsErbB22_GAP_GRB2', erbb(bd=1, ty='2') % erbb(bd=1, ty='2') % GAP(bgrb2=2) % GRB2(bgap=2, bsos=None))
# Observable('obsErbB23_GAP_GRB2', erbb(bd=1, ty='2') % erbb(bd=1, ty='3') % GAP(bgrb2=2) % GRB2(bgap=2, bsos=None))
# Observable('obsErbB24_GAP_GRB2', erbb(bd=1, ty='2') % erbb(bd=1, ty='4') % GAP(bgrb2=2) % GRB2(bgap=2, bsos=None))
# Observable('obsErbB22_GAP_GRB2_SOS', erbb(bd=1, ty='2') % erbb(bd=1, ty='2') % GAP(bgrb2=2) % GRB2(bgap=2, bsos=3) % SOS(bras=None, bgrb=3, bERKPP=None, st='U'))
# Observable('obsErbB23_GAP_GRB2_SOS', erbb(bd=1, ty='2') % erbb(bd=1, ty='3') % GAP(bgrb2=2) % GRB2(bgap=2, bsos=3) % SOS(bras=None, bgrb=3, bERKPP=None, st='U'))
# Observable('obsErbB24_GAP_GRB2_SOS', erbb(bd=1, ty='2') % erbb(bd=1, ty='4') % GAP(bgrb2=2) % GRB2(bgap=2, bsos=3) % SOS(bras=None, bgrb=3, bERKPP=None, st='U'))
# Observable('obsErbB22_GAP_SHCP', erbb(bd=1, ty='2') % erbb(bd=1, ty='2') % GAP(bgrb2=None, b=2) % SHC(batp=None, st='P', bgrb=None, bgap=2))
# Observable('obsErbB23_GAP_SHCP', erbb(bd=1, ty='2') % erbb(bd=1, ty='3') % GAP(bgrb2=None, b=2) % SHC(batp=None, st='P', bgrb=None, bgap=2))
# Observable('obsErbB24_GAP_SHCP', erbb(bd=1, ty='2') % erbb(bd=1, ty='4') % GAP(bgrb2=None, b=2) % SHC(batp=None, st='P', bgrb=None, bgap=2))

# with open('model_species', 'rb') as handle:
#     model_species = pickle.loads(handle.read())
# n = 1
# for i in model_species:
#     Observable('m'+str(n), i)
#     n = n + 1

