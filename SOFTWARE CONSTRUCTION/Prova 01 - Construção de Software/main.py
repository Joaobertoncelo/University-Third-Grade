class Relogio24Horas:
    def __init__(self):
        self.horas = 0
        self.minutos = 0
        self.segundos = 0

    def tique(self):
        self.segundos += 1
        if self.segundos == 60:
            self.segundos = 0
            self.minutos += 1
        if self.minutos == 60:
            self.minutos = 0
            self.horas += 1
        if self.horas == 24:
            self.horas = 0

    def compare(self, outro_relogio):
        self_total_minutes = self.horas * 60 + self.minutos
        outro_relogio_total_minutes = outro_relogio.horas * 60 + outro_relogio.minutos

        if self_total_minutes < outro_relogio_total_minutes:
            return -1  
        elif self_total_minutes > outro_relogio_total_minutes:
            return 1  
        else:
            return 0 

    def add(self, outro_relogio):
        new_relogio = Relogio24Horas() 
        new_relogio.horas = self.horas + outro_relogio.horas
        new_relogio.minutos = self.minutos + outro_relogio.minutos
        new_relogio.segundos = self.segundos + outro_relogio.segundos

        if new_relogio.segundos >= 60:
            new_relogio.segundos -= 60
            new_relogio.minutos += 1
        if new_relogio.minutos >= 60:
            new_relogio.minutos -= 60
            new_relogio.horas += 1
        if new_relogio.horas >= 24:
            new_relogio.horas -= 24

        return new_relogio
    
    def subtraction(self, outro_relogio):
        new_relogio = Relogio24Horas()  
        new_relogio.horas = self.horas - outro_relogio.horas
        new_relogio.minutos = self.minutos - outro_relogio.minutos
        new_relogio.segundos = self.segundos - outro_relogio.segundos

        if new_relogio.segundos < 0:
            new_relogio.segundos += 60
            new_relogio.minutos -= 1
        if new_relogio.minutos < 0:
            new_relogio.minutos += 60
            new_relogio.horas -= 1
        if new_relogio.horas < 0:
            new_relogio.horas += 24

        return new_relogio