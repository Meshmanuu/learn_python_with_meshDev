class Smartphone:
    """Represents a smartphone with various attributes and functionalities."""

    def __init__(self, brand, model, imei, storage_gb, battery_mah):
        """
        Initializes a new Smartphone object.

        Args:
            brand (str): The brand of the smartphone.
            model (str): The model name of the smartphone.
            imei (str): The unique International Mobile Equipment Identity.
            storage_gb (int): The storage capacity in gigabytes.
            battery_mah (int): The battery capacity in milliampere-hours.
        """
        self.brand = brand
        self.model = model
        self.imei = imei
        self.storage_gb = storage_gb
        self.battery_mah = battery_mah
        self.battery_level = 100
        self.is_on = False
        self.current_app = None

    def power_on(self):
        """Powers on the smartphone."""
        if not self.is_on:
            self.is_on = True
            print(f"{self.brand} {self.model} is powering on.")
        else:
            print(f"{self.brand} {self.model} is already on.")

    def power_off(self):
        """Powers off the smartphone."""
        if self.is_on:
            self.is_on = False
            self.current_app = None
            print(f"{self.brand} {self.model} is powering off.")
        else:
            print(f"{self.brand} {self.model} is already off.")

    def install_app(self, app_name):
        """Simulates installing an app."""
        print(f"Installing '{app_name}' on {self.brand} {self.model}.")

    def open_app(self, app_name):
        """Opens the specified app."""
        if self.is_on:
            self.current_app = app_name
            print(f"Opening '{app_name}' on {self.brand} {self.model}.")
        else:
            print(f"Please power on {self.brand} {self.model} first.")

    def close_app(self):
        """Closes the currently open app."""
        if self.is_on and self.current_app:
            print(f"Closing '{self.current_app}' on {self.brand} {self.model}.")
            self.current_app = None
        elif not self.is_on:
            print(f"Please power on {self.brand} {self.model} first.")
        else:
            print("No app is currently open.")

    def charge(self, percentage):
        """Simulates charging the battery."""
        if self.is_on:
            self.battery_level = min(100, self.battery_level + percentage)
            print(f"Charging {self.brand} {self.model}. Battery level: {self.battery_level}%")
        else:
            print(f"Please power on {self.brand} {self.model} to see the battery level.")


class GamingSmartphone(Smartphone):
    """Represents a smartphone specifically designed for gaming."""

    def __init__(self, brand, model, imei, storage_gb, battery_mah, dedicated_gpu, cooling_system):
        """
        Initializes a new GamingSmartphone object.

        Args:
            brand (str): The brand of the gaming smartphone.
            model (str): The model name.
            imei (str): The IMEI.
            storage_gb (int): Storage capacity.
            battery_mah (int): Battery capacity.
            dedicated_gpu (str): The dedicated graphics processing unit.
            cooling_system (str): The type of cooling system.
        """
        super().__init__(brand, model, imei, storage_gb, battery_mah)
        self.dedicated_gpu = dedicated_gpu
        self.cooling_system = cooling_system
        self.is_gaming = False

    def start_game(self, game_name):
        """Starts the specified game."""
        if self.is_on:
            self.current_app = game_name
            self.is_gaming = True
            print(f"Starting '{game_name}' on {self.brand} {self.model} with {self.dedicated_gpu}.")
        else:
            print(f"Please power on {self.brand} {self.model} first.")

    def stop_game(self):
        """Stops the currently running game."""
        if self.is_on and self.is_gaming:
            print(f"Stopping '{self.current_app}' on {self.brand} {self.model}.")
            self.current_app = None
            self.is_gaming = False
        elif not self.is_on:
            print(f"Please power on {self.brand} {self.model} first.")
        else:
            print("No game is currently running.")


if __name__ == "__main__":
    my_phone = Smartphone("Samsung", "Galaxy S21", "123456789012345", 128, 4000)
    work_phone = Smartphone("Nokia", "3310", "987654321098765", 0, 1200)
    my_gaming_phone = GamingSmartphone("ROG", "Phone 7", "019283746501928", 512, 6000, "Adreno 750", "Vapor Chamber")

    my_phone.power_on()
    my_phone.install_app("WhatsApp")
    my_phone.open_app("Camera")
    my_phone.close_app()
    my_phone.charge(20)
    my_phone.power_off()

    work_phone.power_on()
    work_phone.install_app("Snake")
    work_phone.open_app("Snake")
    work_phone.power_off()

    my_gaming_phone.power_on()
    my_gaming_phone.start_game("Asphalt 9")
    my_gaming_phone.charge(50)
    my_gaming_phone.stop_game()
    my_gaming_phone.power_off()