import re

class AIRReader:

    def __init__(self, filename):

        try:
            #Open the file
            file = open(filename, 'r')
            values = file.read().split("\n")

            #Create custom dict to save the 2004
            self.data = {}

            #For loop counter
            self.counter = 0

            #Main keys
            self.keys = ["dist_num", "num", "type", "heigth", "lat", "lon", "time", "date", "reserve1", "reserve2"]

            #Pressure keys
            for ps in [1000, 925, 850, 700, 500, 400, 300, 250, 200, 150, 100, 70, 50, 30, 20, 10]:
                for val in ["H", "t", "DD", "ddd", "ff"]:
                    self.keys.append(val + "-" + str(ps))

            #Main keys again
            self.keys.extend(["Sr", "Ra", "Nz", "Nt", "Nw", "P-e", "t-e", "DD-e", "ff-e", "ddd"])

            # Create empty tuples
            for key in self.keys:
                self.data[key] = []

            #Read the 2004
            for key in values:
                value = re.findall(r"[-+]?\d*\.\d+|\d+", key)
                if len(value) == 150:
                    count = 0
                    for subkey in value:
                        if subkey != "" and count < len(self.keys):
                            self.data[self.keys[count]].append(float(subkey))
                        count += 1
                    self.counter += 1

            #If file was empty
            if self.counter == 0:
                self.noProblem = False
                return


        except IOError:
            self.noProblem = False

    def convertData(self):
        """
        Converts the values from the AIR specification to normal values
        """
        for key, val in self.data.items():
            if "-" in key:
                subkey = key[:key.find("-")]
            else:
                subkey = key

            for num in range(0, self.data[key].__len__()):
                if self.data[key][num] != -9999.0:
                    self.data[key][num] = self.__convert(subkey, self.data[key][num])

    #Returns converted value for the key
    def __convert(self, key, value):
        return {
            "lat": value / 100.0,
            "lon": value / 100.0,
            "H": value - 1000.0,
            "t": (value - 1000.0) / 10.0,
            "DD": value / 10.0,
        }.get(key, value)

    # Returns the array bt given key
    def __getitem__(self, item):
        return self.data[item]

    # Check if values is or not empty
    def isNull(self, values, num):
        """
        Checks if value not equal to zero of the parameter from the station.

        :param values: list of the keys
        :type values: tuple
        :param num: number in the list in range(0, counter)
        :type num: int
        :return: False if not empty
        :rtype: bool
        """

        # Local counter
        count = 0

        # Loop throug all arguments
        for value in values:
            if self.data[value][num] != -9999.0:
                count += 1

        # Check the value of out counter
        if values.__len__() == count:
            return False
        else:
            return True