class Superhero:
    """Represents a superhero with unique abilities and traits."""

    def __init__(self, name, alias, power, weakness):
        """
        Initializes a new Superhero object.

        Args:
            name (str): The superhero's real name.
            alias (str): The superhero's public alias.
            power (str): The superhero's primary superpower.
            weakness (str): The superhero's main weakness.
        """
        self.name = name
        self.alias = alias
        self.power = power
        self.weakness = weakness
        self.is_flying = False  # Added an attribute to track flying status

    def reveal_identity(self):
        """Prints the superhero's real identity (for dramatic effect!)."""
        print(f"The amazing {self.alias} is actually the one and only {self.name}!")

    def use_power(self):
        """Demonstrates the superhero using their power."""
        print(f"{self.alias} unleashes their incredible {self.power}!")

    def fly(self):
        """Allows the superhero to take flight."""
        if "flight" in self.power.lower():
            self.is_flying = True
            print(f"{self.alias} soars through the sky!")
        else:
            print(f"{self.alias} can't fly with their current powers.")

    def land(self):
        """Allows the superhero to land."""
        if self.is_flying:
            self.is_flying = False
            print(f"{self.alias} touches down gracefully.")
        else:
            print(f"{self.alias} is already on the ground.")

# Creating instances of the Superhero class
superman = Superhero("Clark Kent", "Superman", "flight, super strength, heat vision", "kryptonite")
wonder_woman = Superhero("Diana Prince", "Wonder Woman", "super strength, agility, lasso of truth", "vulnerability to piercing weapons")

superman.reveal_identity()
superman.use_power()
superman.fly()
wonder_woman.use_power()
wonder_woman.fly() # Wonder Woman doesn't explicitly have "flight" in her power, so this will print accordingly