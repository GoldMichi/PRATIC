# %%
import openmc
import numpy as np
import matplotlib.pyplot as plt

# converto tutte le temperature in K
C2K = 273.15

# %%
"""Creazione uranio """

uo2_central = openmc.Material(1, "uo2_central")

uo2_central.add_nuclide("U235", 0.025)      #ho modificato gli isotopi e la densità
uo2_central.add_nuclide("U234", 0.00021)
uo2_central.add_nuclide("U236", 0.00011)
uo2_central.add_nuclide("U238", 0.97468)
uo2_central.add_nuclide("O16", 2)
uo2_central.set_density("g/cm3", 10.1711)        
uo2_central.temperature = 350 + C2K

uo2_internal = openmc.Material(2, "uo2_internal")

uo2_internal.add_nuclide("U235", 0.035)
uo2_internal.add_nuclide("U234", 0.00030)
uo2_internal.add_nuclide("U236", 0.00016)
uo2_internal.add_nuclide("U238", 0.96454)
uo2_internal.add_nuclide("O16", 2)
uo2_internal.set_density("g/cm3", 10.1711)       
uo2_internal.temperature = 350 + C2K

uo2_external = openmc.Material(3, "uo2_external")

uo2_external.add_nuclide("U235", 0.05)
uo2_external.add_nuclide("U234", 0.00044)
uo2_external.add_nuclide("U236", 0.00023)
uo2_external.add_nuclide("U238", 0.94933)
uo2_external.add_nuclide("O16", 2)
uo2_external.set_density("g/cm3", 10.1711)      
uo2_external.temperature = 350 + C2K

gadolinium = openmc.Material(4, "gadolinium")

gadolinium.add_nuclide("O16", 5)
gadolinium.add_element("Gd", 2)

uo2_poisoned = openmc.Material.mix_materials([uo2_central, gadolinium], [0.92, 0.08], "wo")
uo2_poisoned.set_density("g/cm3", 9.8003)
uo2_poisoned.temperature = 350 + C2K


# %%
"""Creazione Cladding"""

zirconium= openmc.Material(5, name = "zirconium")
zirconium.add_element("Zr", 1)

stagno = openmc.Material(6, name = "stagno")
stagno.add_element("Sn", 1)

ferro = openmc.Material(10, name = "Ferro")
ferro.add_element("Fe", 1)

oxigen = openmc.Material(11, name = "Oxygen")
oxigen.add_element("O", 1)

cromo = openmc.Material(12, name = "cromo")
cromo.add_element("Cr", 1)

zirc_clad = openmc.Material.mix_materials([zirconium, stagno, ferro, oxigen, cromo], [0.98115, 0.0145, 0.0021, 0.00125, 0.001], "wo")
zirc_clad.set_density("g/cm3", 6.5215)
zirc_clad.temperature = 300 + C2K

# %%
"""creazione acciaio   """                  
# ferro e cromo già inseriti

manganese = openmc.Material(11, name = "Manganese")
manganese.add_element("Mn", 1)

nichel = openmc.Material(12, name = "Nichel")   
nichel.add_element("Ni", 1)

silicio = openmc.Material(13, name = "Silicio")
silicio.add_element("Si", 1)

steel = openmc.Material.mix_materials([ferro, cromo, nichel, manganese,  silicio], [0.684, 0.19, 0.10, 0.02, 0.006], "wo") 
steel.set_density("g/cm3", 7.9181)
steel.temperature = 300 + C2K

# %%
"""creazione AIC"""
Argento = openmc.Material(8,   name = "Argento")
Argento.add_element("Ag", 1)             

Indio = openmc.Material(9, name = "Indio")
Indio.add_element("In", 1)

Cadmio = openmc.Material(10, name = "Cadmio")
Cadmio.add_element("Cd", 1)

AIC = openmc.Material.mix_materials([Argento, Indio, Cadmio], [0.8, 0.15, 0.05], "wo") 
AIC.set_density("g/cm3", 9.9849)
AIC.temperature = 300 + C2K

# %%

"""Creazione acqua e gap (helium)"""
helium = openmc.Material(6, name = "gap")         #parametri modificabile (da chiedere)

# Valore dalla Tabella 9: 2.4044E-04
helium.set_density('atom/b-cm', 2.4044e-04)

# Aggiunta degli isotopi con i valori specificati
helium.add_nuclide('He3', 4.8089e-10)
helium.add_nuclide('He4', 2.4044e-04)

# Temperatura operativa (600 K come da specifica)
helium.temperature = 600 


water = openmc.Material(7, name = "water")
water.add_element("H", 2)
water.add_nuclide("O16", 1)
water.set_density("g/cm3", 0.72683)    #densità cambiata (condizioni isoterme 300)
water.temperature = 300 + C2K
water.add_s_alpha_beta("c_H_in_H2O")

# %%

materials = openmc.Materials([uo2_external, uo2_internal, uo2_central, uo2_poisoned, zirc_clad, helium, water, AIC])
materials.export_to_xml()


