class Schedule:
    def __init__(self, day, startTime, endtime, classroom):
        self.set_day(day)
        self.set_startTime(startTime)
        self.set_endtime(endtime)
        self.set_classroom(classroom)

    def get_day(self):
        return self._day

    def set_day(self, day):
        if day != "":
            self._day = day
        else:
            raise ValueError("El día no puede estar vacío")
        
    def get_startTime(self):
        return self._startTime

    def set_startTime(self, startTime):
        if startTime != "":
            self._startTime = startTime
        else:
            raise ValueError("La hora de inicio no puede estar vacía")

    def get_endtime(self):
        return self._endtime

    def set_endtime(self, endtime):
        if endtime != "":
            self._endtime = endtime
        else:
            raise ValueError("La hora de finalización no puede estar vacía")
        
    def get_classroom(self):
        return self._classroom

    def set_classroom(self, classroom):
        if classroom != "":
            self._classroom = classroom
        else:
            raise ValueError("El aula no puede estar vacía")

    def show_info(self):
        return f"Día: {self.get_day()} - Hora de inicio: {self.get_startTime()} - Hora de finalización: {self.get_endtime()} - Salón: {self.get_classroom()}"