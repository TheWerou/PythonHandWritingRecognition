from AInetworkClasses.NewNeuron import NewNeuron


class NeuronLayer:
    def __init__(self, amount_of_neurons=0, amount_of_inputs=0):
        self.amount_of_neurons = 0
        self.amount_of_wages = 0
        self.amount_of_inputs = 0
        self.list_fo_neurons = []
        self.add_neuron(amount_of_neurons, amount_of_inputs)

    def add_neuron(self, amount_of_neurons, amount_of_inputs):
        self.amount_of_neurons = amount_of_neurons
        self.amount_of_wages = amount_of_inputs + 1
        self.amount_of_inputs = amount_of_inputs
        for i in range(amount_of_neurons):
            neuron = NewNeuron()
            self.list_fo_neurons.append(neuron)

        for i in range(amount_of_neurons):
            self.list_fo_neurons[i].add_wejscia(amount_of_inputs)

    def set_neuron_wagi(self, list_of_wags):
        for i in range(len(self.list_fo_neurons)):
            self.list_fo_neurons[i].set_wagi(list_of_wags[i])

    def set_neuron_popwagi(self, list_of_popwags):
        for i in range(len(self.list_fo_neurons)):
            self.list_fo_neurons[i].set_popwagi(list_of_popwags[i])

    def set_neuron_delta(self, list_of_delta):
        for i in range(len(self.list_fo_neurons)):
            self.list_fo_neurons[i].set_deltawag(list_of_delta[i])

    def use_neuron_input(self, list_of_input):
        for i in range(len(self.list_fo_neurons)):
            self.list_fo_neurons[i].use_wejscia(list_of_input)

    def use_neuron_input_one_to_one(self, list_of_input):
        for i in range(len(self.list_fo_neurons)):
            self.list_fo_neurons[i].use_wejscie_one(list_of_input[i])

    def calc_neurons_output(self):
        for i in self.list_fo_neurons:
            i.calc_output()

    def generate_list_of_outputs(self):
        output_list = []
        for i in self.list_fo_neurons:
            output_list.append(i.get_output())

        return output_list

    def generate_list_of_inputs(self):
        output_list = []
        for i in self.list_fo_neurons:
            output_list.append(i.get_wejscia())

        return output_list

    def generate_list_of_wspolczyniki_x_wagi(self, prev_neurons):     # ta metoda tez jest do poprawy
        output_list = []
        suma = 0
        for i in range(len(prev_neurons)):
            output_list.append(0)
            #output_list[k - 1] += self.list_fo_neurons[m].get_wspolczynik() * self.generate_wagas_table()[k - 1][k]

        #print("----------------------------------")
        #print(len(self.list_fo_neurons))
        #print(len(self.list_fo_neurons[0].get_wagas()))
        #print("++++++++++++++++++++++++++++++++++++++++++++")

        for m in range(len(self.list_fo_neurons)):
            k = 1
            while k < len(self.list_fo_neurons[0].get_wagas()):
                #print(str(k - 1) + " " + str(m) + " " + str(k))
                output_list[k - 1] += self.list_fo_neurons[m].calc_wspo_x_wag(k)
                k += 1

        #print("----------------------------------")
        return output_list

    def calc_pochodnas(self):
        for i in self.list_fo_neurons:
            i.calc_pochodna_2()

    def calc_wspoczynikas_wyjsciowy(self, list_of_correct_outputs):
        for i in range(len(self.list_fo_neurons)):
            self.list_fo_neurons[i].calc_wspolczynik_wyjsciowy(list_of_correct_outputs[i])

    def calc_wspoczynikas_posredni(self, list_suma_waga_x_wspolczynik):     # przez ta metode jest blad sieci
        for i in range(len(self.list_fo_neurons)):
            self.list_fo_neurons[i].calc_wspolczynik_posredni(list_suma_waga_x_wspolczynik[i])

    def update_wagas_in_layer(self):
        for i in self.list_fo_neurons:
            i.update_wagas()

    def get_outputs(self):
        output = []
        for i in self.list_fo_neurons:
            output.append(i.get_output())
        return output

    def generate_wagas_table(self):
        output_list = []
        for i in self.list_fo_neurons:
            output_list.append(i.get_wagas())
        return output_list

    def generate_popwagas_table(self):
        output_list = []
        for i in self.list_fo_neurons:
            output_list.append(i.get_popwagi())
        return output_list

    def generate_deltwag_table(self):
        output_list = []
        for i in self.list_fo_neurons:
            output_list.append(i.get_deltawag())
        return output_list
# ----------------------- To powino działać

    def get_amount_of_neurons(self):
        return self.amount_of_neurons

    def get_neurons(self):
        return self.list_fo_neurons

    def get_amount_of_wagas(self):
        return self.amount_of_wages
