class SpaceAge(object):
    earth_orbital_period = 31557600  # in seconds

    # planets and orbital periods in Earth years
    planets = {
        'mercury': 0.2408467,
        'venus': 0.61519726,
        'earth': 1.0,
        'mars': 1.8808158,
        'jupiter': 11.862615,
        'saturn': 29.447498,
        'uranus': 84.016846,
        'neptune': 164.79132
    }

    def __init__(self, seconds):
        self.seconds = seconds

    def __getattr__(self, planet):
        def calculate_age():
            orbital_period = self.planets[planet[3:]]
            age = self.seconds / orbital_period / self.earth_orbital_period
            return round(age, 2)

        return calculate_age
