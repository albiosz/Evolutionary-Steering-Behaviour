# Evolutionary-Steering-Behaviour
# Brief description
During the simulation Vehicles evolve to stay alive longer and longer. Genetic algorithm is used to transfer best attributes of the longes
living Vehicles to new Entities of a new generation. It may happen that even one Vehicle has quite good attributes it hasn't lived for a
long time. That's the reson why chance is given to the short living Vehicles to tranfer their attributes, because they may live longer in
different conditions. To keep some variety mutation is used with some probability.

# How to run
It was tested with Python 3.7.4 with Tkinter installed (graphic library)
python main.py


# Constants
It is possible to adjust parameters of the simulation in Constants.py file.
Most "interesting":
NUM_OF_FOOD (number of food entities on board, default = 20)
NUM_OF_POISON (number of poison on board, default = 20)
NUM_OF_VEHICLES (number of vehicles on board, default = 10)

MUTATATION_RATE (the probability of mutation to happen, default = 0.1)
MUTATION_IMPACT (how the mutation can impact attributes, default = 0.05)

# Do I need to wait long to receive some results?
The answer is no. You can always change number of calculations per frame in simulation window.
