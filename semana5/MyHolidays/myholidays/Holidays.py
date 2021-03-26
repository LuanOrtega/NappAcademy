from datetime import date, datetime
import sys
class MyCalendar:
    feriados = []
    def __init__(self, *args):
        self.datas = []
       
        for i in range(0, len(args)):
            try:
                if type(args[i]) == date:
                    if args[i] in self.datas:
                        pass
                    else:
                        self.datas.append(args[i])
                else:
                    if datetime.strptime(args[i], '%d/%m/%Y').date() in self.datas:
                        pass
                    else:
                        self.datas.append(datetime.strptime(args[i], '%d/%m/%Y').date())
            except:
                pass

    def add_holiday(self, *args):
        
        for i in range(0, len(args)):
            try:
                if type(args[i]) == date:
                    if args[i] in self.feriados:
                        pass
                    else:
                        self.feriados.append(args[i])

                    if args[i] in self.datas:
                        pass
                    else:
                        self.datas.append(args[i])
                else:
                    if datetime.strptime(args[i], '%d/%m/%Y').date() in self.feriados:
                        pass
                    else:
                        self.feriados.append(datetime.strptime(args[i], '%d/%m/%Y').date())

                    if datetime.strptime(args[i], '%d/%m/%Y').date() in self.datas:
                        pass
                    else:
                        self.datas.append(datetime.strptime(args[i], '%d/%m/%Y').date())
            except:
                pass

        print('feriados: ',self.feriados)
        

    def check_holiday(self, *args):
        
        for i in range(0, len(args)):
            
            try:
                if type(args[i]) == date:
                    if args[i] in self.feriados:
                        return True
                    else:
                        return False
                else:
                    if datetime.strptime(args[i], '%d/%m/%Y').date() in self.feriados:
                        return True
                    else:
                        return False
            except:
                return False