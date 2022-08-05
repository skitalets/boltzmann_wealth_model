import mesa

class MoneyAgent(mesa.Agent):
    """An agent with fixed initial wealth."""

    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.wealth = 1

    def step(self):
        # The agent's step will go here.
        # For demonstration purposes we will print the agent's unique_id

        if self.wealth == 0:
            return

        other_agent = self.random.choice(self.model.schedule.agents)
        other_agent.wealth = other_agent.wealth + 1
        self.wealth = self.wealth - 1

        print("Hi, I am agent " + str(self.unique_id) + " and my wealth is " + str(self.wealth) + ".")

class MoneyModel(mesa.Model):
    """A model with some number of agents."""

    def __init__(self, N):
        self.num_agents = N
        self.schedule = mesa.time.RandomActivation(self)

        # Create agents
        for i in range(self.num_agents):
            a = MoneyAgent(i, self)
            self.schedule.add(a)

    def step(self):
        """Advance the model one step."""

        self.schedule.step()
