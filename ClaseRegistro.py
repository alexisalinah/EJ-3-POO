class registro: 
    __temperatura = 0
    __humedad =  0
    __presion = 0
    def __init__(self, temperatura, humedad, presion):
        self.__temperatura=temperatura
        self.__humedad=humedad
        self.__presion=presion
    def get_temp(self):
        return self.__temperatura
    def get_humedad(self):
        return self.__humedad
    def get_presion(self):
        return self.__presion