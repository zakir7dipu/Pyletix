class Seeder:
    def run(self):
        raise NotImplementedError("Seeder must implement run method")

    def call(self, seeder_class):
        seeder = seeder_class()
        seeder.run()
