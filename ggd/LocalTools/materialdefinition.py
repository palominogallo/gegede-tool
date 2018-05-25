# based on Tyler https://github.com/tyleralion/duneggd
#^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^
def define_materials( g ):
    h  = g.matter.Element("hydrogen",   "H",  1,  "1.00791*g/mole" )
    b  = g.matter.Element("boron",      "B",  5,  "10.811*g/mole" )
    c  = g.matter.Element("carbon",     "C",  6,  "12.0107*g/mole")
    n  = g.matter.Element("nitrogen",   "N",  7,  "14.0671*g/mole")
    o  = g.matter.Element("oxygen",     "O",  8,  "15.999*g/mole" )
    f  = g.matter.Element("fluorine",   "F",  9,  "18.9984*g/mole")
    na = g.matter.Element("sodium",     "Na", 11, "22.99*g/mole"  )
    mg = g.matter.Element("magnesium",  "Mg", 12, "24.305*g/mole" )
    al = g.matter.Element("aluminum",   "Al", 13, "26.9815*g/mole")
    si = g.matter.Element("silicon",    "Si", 14, "28.0855*g/mole")
    p  = g.matter.Element("phosphorus", "P",  15, "30.973*g/mole" )
    s  = g.matter.Element("sulfur",     "S",  16, "32.065*g/mole" )
    ar = g.matter.Element("argon",      "Ar", 18, "39.948*g/mole" )
    ar = g.matter.Element("potassium",  "K",  19, "39.0983*g/mole")
    ca = g.matter.Element("calcium",    "Ca", 20, "40.078*g/mole" )
    ti = g.matter.Element("titanium",   "Ti", 22, "47.867*g/mole" )
    cr = g.matter.Element("chromium",   "Cr", 24, "51.9961*g/mole")
    mn = g.matter.Element("manganese",  "Mn", 25, "54.9380*g/mole")
    fe = g.matter.Element("iron",       "Fe", 26, "55.8450*g/mole")
    ni = g.matter.Element("nickel",     "Ni", 28, "58.6934*g/mole")

#    cu = g.matter.Element("copper",     "Cu", 29, "63.546*g/mole")
    cu63=g.matter.Isotope("copper63", 29, 63, "62.93*g/mole")
    cu63=g.matter.Isotope("copper65", 29, 65, "64.93*g/mole")
    cu=g.matter.Composition("copper",
                            isotopes=(("copper63",0.6917),
                                      ("copper65",0.3083)) )

    zn64=g.matter.Isotope("zinc64", 30, 64, "63.93*g/mole")

    zn= g.matter.Composition("zinc",
                             isotopes=(("zinc64",1.0),) ) # Note: odd syntax ((a,b),) defines a tuple of tuples with one element

    br = g.matter.Element("bromine",    "Br", 35, "79.904*g/mole" )
    sb = g.matter.Element("antimony",   "Sb", 51, "121.76*g/mole" )
    xe = g.matter.Element("xenon",      "Xe", 54, "131.293*g/mole")
    pb = g.matter.Element("lead",       "Pb", 82, "207.20*g/mole" )

    # Molecules for Rock and fibrous_glass Mixtures
    SiO2  = g.matter.Molecule("SiO2",  density="2.2*g/cc",   elements=(("silicon",1),("oxygen",2)))
    FeO   = g.matter.Molecule("FeO",   density="5.745*g/cc", elements=(("iron",1),("oxygen",1)))
    Al2O3 = g.matter.Molecule("Al2O3", density="3.97*g/cc",  elements=(("aluminum",2),("oxygen",3)))
    MgO   = g.matter.Molecule("MgO",   density="3.58*g/cc",  elements=(("magnesium",1),("oxygen",1)))
    CO2   = g.matter.Molecule("CO2",   density="1.562*g/cc", elements=(("carbon",1),("oxygen",2)))
    CaO   = g.matter.Molecule("CaO",   density="3.35*g/cc",  elements=(("calcium",1),("oxygen",1)))
    Na2O  = g.matter.Molecule("Na2O",  density="2.27*g/cc",  elements=(("sodium",2),("oxygen",1)))
    P2O5  = g.matter.Molecule("P2O5",  density="1.562*g/cc", elements=(("phosphorus",2),("oxygen",5)))
    TiO2  = g.matter.Molecule("TiO2",  density="4.23*g/cc",  elements=(("titanium",1),("oxygen",2)))
    Fe2O3 = g.matter.Molecule("Fe2O3", density="5.24*g/cc",  elements=(("iron",2),("oxygen",3)))

    rock  = g.matter.Mixture( "Rock", density = "2.82*g/cc",
                            components = (
                               ("SiO2",   0.5267),
                               ("FeO",    0.1174),
                               ("Al2O3",  0.1025),
                               ("oxygen", 0.0771),
                               ("MgO",    0.0473),
                               ("CO2",    0.0422),
                               ("CaO",    0.0382),
                               ("carbon", 0.0240),
                               ("sulfur", 0.0186),
                               ("Na2O",   0.0053),
                               ("P2O5",   0.0007),
                            ))

    dirt  = g.matter.Mixture( "Dirt", density = "1.7*g/cc",
                            components = (
                                ("oxygen",    0.438),
                                ("silicon",   0.257),
                                ("sodium",    0.222),
                                ("aluminum",  0.049),
                                ("iron",      0.019),
                                ("potassium", 0.015),
                            ))

    air   = g.matter.Mixture( "Air", density = "0.001225*g/cc",
                            components = (
                                ("nitrogen", 0.781154),
                                ("oxygen",   0.209476),
                                ("argon",    0.00934)
                            ))


    bakelite = g.matter.Mixture( "Bakelite", density = "1.25*g/cc",
                            components = (
                                ("hydrogen", 0.057441),
                                ("carbon",   0.774591),
                                ("oxygen",   0.167968)
                            ))


    honeycomb = g.matter.Mixture( "Honeycomb", density = "0.94*g/cc",
                            components = (
                                ("hydrogen", 0.143711),
                                ("carbon",   0.856289)
                            ))

       # Materials for the radiators and st planes following
       # WARNING! densities not right!
    C3H6   = g.matter.Molecule("C3H6",   density="0.946*g/cc",   elements=(("carbon",3), ("hydrogen",6)))
    fracC3H6 = (25*0.946)/(25*0.946+125*0.001225) # TODO get from spacing in RadiatorBldr cfg
       #densRad = fracC3H6*0.946 + (1-fracC3H6)*0.001225
       #dRad = str(densRad)+"*g/cc"
    dRad = "0.1586875*g/cc"
    RadBlend = g.matter.Mixture( "RadiatorBlend", density = dRad,
                            components = (
                                ("Air",  1-fracC3H6),
                                ("C3H6", fracC3H6)
                            ))
    densCO2 = 44.01/22.4*0.001 # molar mass / STP molar volume * conversion to g/cm3 from L
    densAr  = 39.95/22.4*0.001
    densXe  = 131.3/22.4*0.001
    fracCO2 = .3
    densArCO2 = fracCO2 * densCO2 + (1-fracCO2) * densAr
    densXeCO2 = fracCO2 * densCO2 + (1-fracCO2) * densXe
    dArCO2 = str(densArCO2)+"*g/cc"
    dXeCO2 = str(densXeCO2)+"*g/cc"

    stGas_Xe = g.matter.Mixture( "stGas_Xe", density = dXeCO2,
                            components = (
                                ("CO2",    fracCO2),
                                ("argon",  1-fracCO2)
                                #("xenon",  1-fracCO2)   #GENIE XSec spline having trouble with xenon
                            ))

    # Materials for the targets and st planes following
    H2O      = g.matter.Molecule("Water",       density="1.0*kg/l",   elements=(("oxygen",1),("hydrogen",2)))
    ArTarget = g.matter.Molecule("ArgonTarget", density="0.2297*g/cc", elements=(("argon",1),))
    #ArTarget = g.matter.Molecule("ArgonTarget", density="10.2297*g/cc", elements=(("argon",1),))
    Aluminum = g.matter.Molecule("Aluminum",    density="2.70*g/cc",  elements=(("aluminum",1),))
    Copper = g.matter.Molecule("Copper",    density="8.96*g/cc",  elements=(("copper",1),))
    MagnetCoilMassFracCopper=0.964
    MagnetCoil=g.matter.Mixture("MagnetCoil", density="6.94*g/cc",
                                components=( ("Copper",MagnetCoilMassFracCopper),
                                            ("Water",1-MagnetCoilMassFracCopper) ) )

    CarFiber = g.matter.Molecule("CarbonFiber", density="1.6*g/cc",  elements=(("carbon",1),))
    stGas_Ar = g.matter.Mixture( "stGas_Ar", density = dArCO2,
                            components = (
                                ("CO2",    fracCO2),
                                ("argon",  1-fracCO2)
                            ))

    Kapton   = g.matter.Molecule("Kapton",   density="1.4*g/cc",   elements=(("carbon",22), ("oxygen",5), ("nitrogen",2)))


    Iron     = g.matter.Molecule("Iron",     density="7.874*g/cc", elements=(("iron",1),))
    Graphite = g.matter.Molecule("Graphite", density="2.23*g/cc",  elements=(("carbon",1),))
    Calcium  = g.matter.Molecule("Calcium",  density="1.55*g/cc",  elements=(("calcium",1),))

    Steel    = g.matter.Mixture( "Steel", density = "7.9300*g/cc",
                            components = (
                                ("iron",     0.7298),
                                ("chromium", 0.1792),
                                ("nickel",   0.0900),
                                ("carbon",   0.0010)
                            ))

    Polycarbonate = g.matter.Molecule("polycarbonate", density="1.2*g/cc",
                            elements=(
                                ("carbon",16),
                                ("hydrogen",6),
                                ("oxygen",3)
                            ))



       # make up a dumb but not crazy density for the STT framing just inside of the ECAL
    sttFrameMix = g.matter.Mixture( "sttFrameMix", density = "0.235*g/cc",
                            components = (
                                ("carbon",        3.9/5.1),
                                ("polycarbonate", 1.2/5.1)
                            ))

    # for the straws -- density??
    fib_glass = g.matter.Mixture( "fibrous_glass", density = "1.0*g/cc",
                            components = (
                                ("SiO2",   0.600),
                                ("CaO",    0.224),
                                ("Al2O3",  0.118),
                                ("MgO",    0.034),
                                ("TiO2",   0.013),
                                ("Na2O",   0.010),
                                ("Fe2O3",  0.001)
                            ))

       #   Materials for the RPCs
       # tetraflouroethane:
    CH2FCF3 = g.matter.Molecule( "CH2FCF3",  density="0.00425*g/cc",
                            elements=( ("carbon",2), ("hydrogen",2), ("fluorine",4) ))
       # isobutane:
    C4H10   = g.matter.Molecule( "C4H10",    density="0.00251*g/cc",
                            elements=( ("carbon",4), ("hydrogen",10) ))

    # sulphurhexaflouride:
    SF6     = g.matter.Molecule( "SF6",      density="6.17*g/L",
                            elements=( ("sulfur",4), ("fluorine",6)  ))

       # use argon density at stp for now. has very little effect.
    rpcGas   = g.matter.Mixture( "rpcGas", density = "1.784*g/L",
                            components = (
                                    ("argon",   0.75),
                                    ("CH2FCF3", 0.20),
                                    ("C4H10",   0.04),
                                    ("SF6",     0.01)
                            ))


    # Materials for the ECAL
    # Epoxy Resin (Glue that will hold the scintillator bars and the lead sheets together):
    # probably won't show up, just the default material of SBPlane
    epoxy_resin   = g.matter.Molecule("epoxy_resin",   density="1.1250*g/cc",
                            elements=(
                                    ("carbon",38),
                                    ("hydrogen",40),
                                    ("oxygen",6)
                                    #("bromine",4) GENIE having trouble with Br
                            ))

    # https://www.thebalance.com/type-304-and-304l-stainless-steel-2340261
    # fractional mass
    # density based on Table 8 DUNE-doc-6652-v5, jp
    ssteel304 = g.matter.Mixture("SSteel304", density="7.9*g/cc",
                            components = (
                                    ("carbon",0.0008),
                                    ("manganese",0.02),
                                    ("phosphorus",0.00045),
                                    ("sulfur",0.0003),
                                    ("silicon",0.0075),
                                    ("chromium",0.18),
                                    ("nickel",0.08),
                                    ("nitrogen",0.0010),
                                    ("iron",0.70995)
                            ))

    # https://www.americanelements.com/calcium-silicate-board-10101-39-0
    # CaO3Si
    # density based on Table 8 DUNE-doc-6652-v5
    calciumSilicate = g.matter.Molecule("CalciumSilicate", density="0.6*g/cc",
                            elements=(
                                ("calcium",1),
                                ("oxygen",3),
                                ("silicon",1)
                            ))

    # https://www.azom.com/article.aspx?ArticleID=6117
    # density based on Table 8 DUNE-doc-6652-v5, jp
    carbonSteel = g.matter.Mixture("CarbonSteel", density="7.9*g/cc",
                            components = (
                                ("carbon",0.0030),
                                ("copper",0.0025),
                                ("iron",0.98),
                                ("manganese",0.0103),
                                ("phosphorus",0.00090),
                                ("silicon",0.00280),
                                ("sulfur",0.00050)
                            ))

    # http://iti.northwestern.edu/cement/monograph/Monograph3_6.html
    # density based on Table 8 DUNE-doc-6652-v5, jp
    reifConcrete = g.matter.Mixture("ReifConcrete", density="2.5*g/cc",
                            components = (
                                ("CaO",0.6661),
                                ("SiO2",0.2345),
                                ("Al2O3",0.0445),
                                ("Fe2O3",0.0307),
                                ("MgO",0.0242)
                            ))

    # https://pubchem.ncbi.nlm.nih.gov/compound/114729#section=Names-and-Identifiers
    # C27 H36 N2 O10
    # LBNE 35 ton - Low Pressure Vessel Engineering Note Rev. 2 - Appendix O - 11/21/12
    # Foam grade C 65kg/m^3, jp
    polyurethane = g.matter.Molecule("Polyurethane", density="0.065*g/cc",
                            elements=(
                                ("carbon",27),
                                ("hydrogen",36),
                                ("nitrogen",2),
                                ("oxygen",10)
                            ))

    # http://www.engineeringtoolbox.com/engineering-materials-properties-d_1225.html
    # http://hepwww.rl.ac.uk/atlas-sct/engineering/material_budget/models/Endcap_Module/ATLAS_ECSCT_Materials.pdf
    # table 3 - C6 H6 O, jp
    epoxy = g.matter.Molecule("Epoxy", density="1.25*g/cc",
                            elements = (
                                    ("carbon",6),
                                    ("hydrogen",6),
                                    ("oxygen",1)
                            ))

    # http://hepwww.rl.ac.uk/atlas-sct/engineering/material_budget/models/Endcap_Module/ATLAS_ECSCT_Materials.pdf
    # table 6, fractional mass, jp
    glass = g.matter.Mixture("Glass", density="2.70*g/cc",
                            components = (
                                    ("silicon",0.2743),
                                    ("boron",0.0166),
                                    ("aluminum",0.0207),
                                    ("sodium",0.0449),
                                    ("potassium",0.0821),
                                    ("zinc",0.0882),
                                    ("titanium",0.0292),
                                    ("oxygen",0.4440)
                            ))

    # http://hepwww.rl.ac.uk/atlas-sct/engineering/material_budget/models/Endcap_Module/ATLAS_ECSCT_Materials.pdf
    # table 6, fractional mass, jp
    # could be also G10
    fr4 = g.matter.Mixture("FR4", density="1.850*g/cc",
                            components = (
                                    ("Epoxy",0.206),
                                    ("Glass",0.794)
                            ))

    # Radiation Physics and Chemistry 63 (2002) 89 92, jp
    # http://www.eljentechnology.com/products/wavelength-shifting-plastics/ej-280-ej-282-ej-284-ej-286?highlight=WyJwb2x5dmlueWx0b2x1ZW5lIl0=
    pvt = g.matter.Molecule("PVT", density="1.023*g/cc",
                            elements = (
                                    ("carbon",9),
                                    ("hydrogen",10)
                            ))

    # Scintillator:
    Scintillator  = g.matter.Mixture("Scintillator",   density="1.05*g/cc",
                            components = (
                                    ("carbon",   0.916),
                                    ("hydrogen", 0.084)
                            ))
    # Oil to be fixed
    Oil  = g.matter.Mixture("Oil",   density="0.8*g/cc",
                            components = (
                                    ("carbon",   0.916),
                                    ("hydrogen", 0.084)
                            ))

    # Lead:
    Lead  = g.matter.Molecule("Lead",   density="11.342*g/cc",   elements=(("lead",1),))


    # for LAr otion using this world:
    LArTarget = g.matter.Molecule("LAr", density="1.4*g/cc", elements=(("argon",1),))

    GArTarget = g.matter.Molecule("GAr", density="1.784*0.001*g/cc", elements=(("argon",1),) )

    KLOEECal  = g.matter.Mixture("KLOEEcal",   density="5.3*g/cc",
                            components = (
                                    ("Lead",   0.42),
                                    ("Scintillator", 0.48),
                                    ("epoxy_resin",0.10)
                            ))

    # Materials for Gas TPC construction

    # For Gas TPC field cage & central electrode
    # Polyvinyl fluoride (Tedlar)
    pvf = g.matter.Molecule("PVF",density="1.71*g/cc",
                            elements=(("carbon",2),("hydrogen",3),
                                      ("fluorine",1)) )

    kevlar = g.matter.Molecule("Kevlar",density="1.45*g/cc",
                               elements=(("carbon",7),("hydrogen",5),
                                         ("nitrogen",1),("oxygen",1))
                              )

    nomex_honeycomb = g.matter.Molecule("NomexHoneycomb",
                                        density="0.029*g/cc",
                                        elements=(
                                               ("carbon",7),
                                               ("hydrogen",5),
                                               ("nitrogen",1),
                                               ("oxygen",1)) )

    mylar = g.matter.Molecule('Mylar',density="1.39*g/cc",
                              elements=(('carbon',10),
                                        ('hydrogen',8),
                                        ('oxygen',4)))
    # 60% kevlar, 40% epoxy resin
    kevlar_prepreg = g.matter.Mixture("KevlarPrepreg",density="1.37*g/cc",
                                      components=(("Kevlar",0.6),
                                                  ("epoxy_resin",0.4)) )


    methane  = g.matter.Molecule('Methane',
                                 density='0.000716*g/cc',
                                 elements=(
                                    ('carbon',1),
                                    ('hydrogen',4)))

    ethane  = g.matter.Molecule('Ethane',
                                density='0.00134*g/cc',
                                elements=(
                                    ('carbon',2),
                                    ('hydrogen',6)))

#    Propane defined as C3H8
#    propane  = g.matter.Molecule('Propane',
#                                 density='0.00197*g/cc',
#                                 elements=(
#                                    ('carbon',3),
#                                    ('hydrogen',8)))

#    Isobutane defined as C4H10
#    isobutane  = g.matter.Molecule('Isobutane',
#                                   density='0.00260*g/cc',
#                                   elements=(
#                                      ('carbon',4),
#                                      ('hydrogen',10)))

#   SF6 already defined

    # Tetrafluoromethane
    cf4  = g.matter.Molecule('CF4',
                             density='0.00393*g/cc',
                             elements=(
                                    ('carbon',1),
                                    ('fluorine',4)))

    # Difluoromethane
    ch2f2  = g.matter.Molecule('CH2F2',
                               density='0.00232*g/cc',
                               elements=(
                                    ('carbon',1),
                                    ('hydrogen',2),
                                    ('fluorine',2)))

    # Dimethyl ether
    dme  = g.matter.Molecule('DME',
                               density='0.00206*g/cc',
                               elements=(
                                    ('carbon',2),
                                    ('hydrogen',6),
                                    ('oxygen',1)))

    n2 = g.matter.Molecule('Nitrogen',
                           density='0.000625*g/cc',
                           elements=(('nitrogen',1),))


    # All at 10 atm
    # Mixes are 9 atm Ar, 1 atm quencher
    hp_ar    = g.matter.Molecule('HP_Ar',
                                 density='0.01784*g/cc',
                                 elements=(('argon',1),))

    hp_arco2 = g.matter.Mixture("HP_ArCO2",
                                density='0.01802*g/cc',
                                components=(
                                    ('HP_Ar',0.890),
                                    ('CO2',0.110)))

    # P10
    hp_arch4 = g.matter.Mixture('HP_ArCH4',
                                density='0.01677*g/cc',
                                components=(
                                ('HP_Ar',0.957),
                                ('Methane',0.043)))

    hp_arcf4 = g.matter.Mixture('HP_ArCF4',
                                density='0.01998*g/cc',
                                components=(('HP_Ar',0.801),
                                ('CF4',0.199)))

    nogas =  g.matter.Mixture('NoGas',
                              density='1.0E-25*g/cc',components=(('argon',1.0),) )
