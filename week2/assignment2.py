from abc import ABC, abstractmethod
class HasWeight(ABC):
    @property
    @abstractmethod
    def weight(self) -> int:
        pass 

class Astronaut(HasWeight):
    def __init__(self, weight):
        if 50 <= weight <= 95:
            self._weight = weight
        else:
            raise ValueError
    
    @property
    def weight(self) -> int:
        return self._weight

class Propellant(HasWeight):
    @property
    @abstractmethod
    def efficiency(self) -> int:
        pass

    @property
    @abstractmethod
    def emission(self) -> int:
        pass

class AmmoniumDinitramide(Propellant):
    def __init__(self, weight):
        if 1 <= weight <= 200:
            self._weight = weight
        else:
            raise ValueError
    @property
    def efficiency(self) -> int:
        return 3

    @property
    def emission(self) -> int:
        return 3

    @property
    def weight(self) -> int:
        return self._weight

class Hydrazine(Propellant):
    def __init__(self, weight):
        if 1 <= weight <= 200:
            self._weight = weight
        else:
            raise ValueError

    @property
    def efficiency(self) -> int:
        return 10

    @property
    def emission(self) -> int:
        return 20
    
    @property
    def weight(self) -> int:
        return self._weight

class Rocket(HasWeight):
    _weight = 0
    def __init__(self, initial_weight, max_weight):
        if initial_weight <= 0:
            raise ValueError
        else:
            self._initial_weight = initial_weight
        if max_weight < initial_weight:
            raise ValueError
        else:
            self._max_weight = max_weight

    @property
    def weight(self):
        return self._weight

    @weight.setter
    def weight(self, weight):
        self._weight = weight

    def add_astronaut(self, weight):
        self.weight += weight

    def add_propellant(self, weight):
        self.weight += weight

    def launch(self, list_of_astronaut, list_of_proprellant):
        self.weight = 0
        launch_success = True
        for astrounaut in list_of_astronaut:
            self.add_astronaut(astrounaut.weight)
        
        for proprellant in list_of_proprellant:            
            self.add_propellant(proprellant.weight) 
        # print("Total weight is ", self.weight)
        if self.weight > self._max_weight:
            # print("Overload, Launch is not successful")
            launch_success = False
        capacity = 0
        envir_impact = 0
        for proprellant in list_of_proprellant:
            capacity += proprellant.efficiency * proprellant.weight
            envir_impact += proprellant.emission * proprellant.weight
        if capacity < self.weight:
            # print("Total capacity is ", capacity)
            # print("Over capacity, Launch is not successful")
            launch_success = False

            # if launch_success == True:
            # print(f"Launch is success, total weight is {self.weight}, total capacity is {capacity}")
            # print(f"Total environmental impact is {envir_impact}")
        return launch_success, envir_impact

    def cal_proprellant(self, astronauts):
        list_of_proprellants = []
        list_of_impacts = []
        proprellants = []
        for hydra_weight in range(1, 201):
            for ammon_weight in range(1, 201):
                hydrazine = Hydrazine(hydra_weight)
                ammoniumDinitramide = AmmoniumDinitramide(ammon_weight)
                proprellants.clear()
                proprellants.append(hydrazine)
                proprellants.append(ammoniumDinitramide)
                launch_result, environment_impact = self.launch(astronauts, proprellants)
                if launch_result == True:
                    # print(f"hydra_wight {hydra_weight} + ammon_weight {ammon_weight}, {launch_result} : {environment_impact}")
                    list_of_proprellants.append([hydra_weight, ammon_weight, environment_impact])
                    list_of_impacts.append(environment_impact)
        index = list_of_impacts.index(min(list_of_impacts))
        # print("index = ", index, min(list_of_impacts))
        # print(list_of_proprellants[index])
        
        # print(f"When astronauts weight is 350, mix propellant would be {list_of_proprellants[index][0]} of Hydrazine\
            # and {list_of_proprellants[index][1]} of AmmoniumDinitramide")   
        return list_of_proprellants[index]

def main():
    astronauts = []
    result = []
    
    rocket = Rocket(500, 1000)
    astronaut1 = Astronaut(80)
    astronauts.append(astronaut1)
    astronaut2 = Astronaut(80)
    astronauts.append(astronaut2)
    astronaut3 = Astronaut(80)
    astronauts.append(astronaut3)
    astronaut4 = Astronaut(80)
    astronauts.append(astronaut4)

    result = rocket.cal_proprellant(astronauts)
    print(f"When astronauts weight is 320, mix propellant would be {result[0]} of Hydrazine and {result[1]} of AmmoniumDinitramide")
    print(f"In this case, environment impact is ", result[2]) 

    astronaut_nervous = []
    astronaut_nervous1 = Astronaut(87.5)
    astronaut_nervous.append(astronaut_nervous1)
    astronaut_nervous2 = Astronaut(87.5)
    astronaut_nervous.append(astronaut_nervous2)
    astronaut_nervous3 = Astronaut(87.5)
    astronaut_nervous.append(astronaut_nervous3)
    astronaut_nervous4 = Astronaut(87.5)
    astronaut_nervous.append(astronaut_nervous4)

    result = rocket.cal_proprellant(astronaut_nervous)
    print(f"When astronauts weight is 350, mix propellant would be {result[0]} of Hydrazine and {result[1]} of AmmoniumDinitramide")
    print(f"In this case, environment impact is ", result[2])

main()
        
