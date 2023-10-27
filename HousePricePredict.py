import pickle

modeline = pickle.load(open("HousePricePredictionModel.pkl", "rb"))

def predictPrice(longitude: float, latitude: float, housingMedianAge: float, totalRooms: float, totalBedrooms: float,
                 population: float, households: float, medianIncome: float, oceanProximity: str, bedroom_ratio: float,
                 household_rooms: float):

        price = 0
        if oceanProximity == "INLAND":
            price = modeline.predict([[longitude, latitude, housingMedianAge, totalRooms, totalBedrooms, population,
                                       households, medianIncome, 0, 1, 0, 0, 0, bedroom_ratio, household_rooms]])
        elif oceanProximity == "ISLAND":
            price = modeline.predict([[longitude, latitude, housingMedianAge, totalRooms, totalBedrooms, population,
                                       households, medianIncome, 0, 0, 1, 0, 0, bedroom_ratio, household_rooms]])
        elif oceanProximity == "NEAR BAY":
            price = modeline.predict([[longitude, latitude, housingMedianAge, totalRooms, totalBedrooms, population,
                                       households, medianIncome, 0, 0, 0, 1, 0, bedroom_ratio, household_rooms]])
        elif oceanProximity == "NEAR OCEAN":
            price = modeline.predict([[longitude, latitude, housingMedianAge, totalRooms, totalBedrooms, population,
                                       households, medianIncome, 0, 0, 0, 0, 1, bedroom_ratio, household_rooms]])
        else:
            price = modeline.predict([[longitude, latitude, housingMedianAge, totalRooms, totalBedrooms, population,
                                       households, medianIncome, 1, 0, 0, 0, 0, bedroom_ratio, household_rooms]])
        return price

