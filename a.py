class A_estrela:
    def __init__(self, grafo_txt: str, Heuristica_txt: str, initial_point: str, final_point: str):
        self.grafo = dict()
        self.heuristica = dict()
        self.passed_cities = set()
        self.open_cities = set()
        self.cost_city = dict()
        self.initial_city = initial_point
        self.final_city = final_point

        with open(grafo_txt) as f:
            lines = f.readlines()
            for line in lines:
                dado_grafo = line.strip('\n').split(';')
                tupla = dado_grafo[0],dado_grafo[1]
                tupla_reverso = dado_grafo[1],dado_grafo[0]
                self.grafo[tupla] = dado_grafo[2]
                self.grafo[tupla_reverso] = dado_grafo[2]

        with open(Heuristica_txt) as f:
            lines = f.readlines()
            for line in lines:
                dado_heuristica = line.strip('\n').split(';')
                self.heuristica[dado_heuristica[0]] = dado_heuristica[1]
        print(self.grafo)
        print('\n')
        print(self.heuristica)

    #retorna o curto da cidade aberta
    def cost_advance(self, city: str) -> int:
        custo_percorrido = self.cost_city[city]
        custo_heuristica = self.heuristica[city]
        return custo_percorrido + custo_heuristica

    #retorna se já passou pela cidade 1
    def has_passed(self, city: str) -> bool:
        for passed_city in self.passed_cities:
            if passed_city == city:
                return True
        return False

    #retorna a proxima cidade com o provavel caminho mais curto para chegar no destino
    def closest_city(self) -> str:
        cosest_city = self.open_cities[0]
        for city in self.open_cities:
            if self.cost_advance(city) < self.cost_advance(cosest_city):
                cosest_city = city
        return city

    #adiciona a cidade no vetor de cidades percorridas passed_city
    def add_passed(self, city: str):
        self.open_cities.remove(city)
        self.passed_cities.append(city)

    #adiciona a cidade no vetor de cidades abertas open_city
    def add_open_city(self, city: str):
        self.open_cities.append(city)

    #adiciona o valor de cost na tupla com chave city para saber o custo de chegar na cidade
    def sum_cost(self, city: str, cost: int):
        pass

    #retorna as cidades que fazem fronteira com a cidade passada comoargumento
    def find_frontier_cities(self, city: str) -> set():
        pass
    def find_shotest_path(self) -> tuple:
        pass

menor_caminho = A_estrela('Grafo.txt','Heuristica.txt', 'Arad', 'Bucareste')
