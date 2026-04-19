class Element:
    def __init__(self, name: str, formula: str, state: str, electric: bool):
        self.name = name
        self.formula = formula
        self.state = state
        self.electric = electric

    def __str__(self):
        return f"Name: {self.name}\nFormula: {self.formula}\nState: {self.state}"
    
    def is_metal(self) -> bool:
        return self.state.lower() == "solid" and self.electric == True or self.name.lower() == "mercury" or self.formula.lower() == "hg"

water = Element("Water", "H20", "Fluid", False)
merc = Element ("Merc", "HG", "Fluid", False)
bromine = Element("Bromium", "BR", "Fluid", False) 

print(water) 
print(f"Metal?: {water.is_metal()}\n")
print(merc)
print(f"Metal?: {merc.is_metal()}\n")
print(bromine)
print(f"Metal?: {bromine.is_metal()}")

