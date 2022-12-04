class ErrorCalculation():
    @staticmethod
    def average(data_array):
        sum = 0
        for i in range(0, len(data_array)):
            sum += data_array[i]
        return sum/len(data_array)