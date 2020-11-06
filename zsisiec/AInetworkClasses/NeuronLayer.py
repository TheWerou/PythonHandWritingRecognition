from zsisiec.AInetworkClasses.NewNeuron import NewNeuron


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
            for k in range(self.amount_of_wages):
                self.list_fo_neurons[i].set_wagi(list_of_wags[i])

    def use_neuron_input(self, list_of_input):
        for i in range(len(self.list_fo_neurons)):
            for k in range(self.amount_of_wages):
                self.list_fo_neurons[i].use_wejscia(list_of_input)

    def use_neuron_input_one_to_one(self, list_of_input):
        for i in range(len(self.list_fo_neurons)):
            self.list_fo_neurons[i].use_wejscia(list_of_input[i])

    def calc_neurons_output(self):
        for i in self.list_fo_neurons:
            i.calc_output()

    def generate_list_of_outputs(self):
        output_list = []
        for i in self.list_fo_neurons:
            output_list.append(i.get_output())

        return output_list

    def generate_list_of_wspolczyniki_x_wagi(self, nr_of_prev_neurons):     # ta metoda tez jest do poprawy
        output_list = []
        suma = 0
        for i in range(nr_of_prev_neurons):
            output_list.append(0)

        for i in range(len(self.list_fo_neurons)):
            k = 1
            while k < self.amount_of_wages:
                suma += self.list_fo_neurons[i].calc_wspo_x_wag(k)
                output_list[k - 1] += suma
                k += 1
                suma = 0

        return output_list

    def calc_pochodnas(self):
        for i in self.list_fo_neurons:
            i.calc_pochodna_2()

    def calc_wspoczynikas_wyjsciowy(self, list_of_correct_outputs):
        a = 0
        for i in self.list_fo_neurons:
            i.calc_wspolczynik_wyjsciowy(list_of_correct_outputs[a])
            a += 0

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

    def get_amount_of_neurons(self):
        return self.amount_of_neurons
