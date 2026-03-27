estacoes = {89.5: "Cocais", 91.5: "Mix", 94.1: "Boa", 99.1: "Clube"}
class RadioFM:
    def __init__(self, vol_max ,estacoes):
        self.__volume_min=0
        self.__volume_max=vol_max
        self.__freq_min=88
        self.__freq_max=108
        self.__estacoes=estacoes
        self.__volume=None
        self.__ligado=False
        self.__estacao_atual=None
        self.__frequencia_atual=None
        self.__antena_habilitada=False



    @property
    def ligar(self):
        return self.__ligado

    @ligar.setter
    def ligar(self):
        if self.__ligado == False:
            self.__ligado = True
            self.__volume = self.__volume_min
        else:
            return "O rádio já está ligado"
        

    def desligar(self):
        if self.__ligado == True:
            self.__ligado = False
        else:
            return "O rádio já está desligado"
        
    @property
    def volume(self):
        return self.__volume
    

    @volume.setter
    def aumentar_volume(self, valor=1):
        if valor != 1: 
            if self.__ligado == True and valor <= self.__volume_max:
                self.__volume = valor
            else:
                return "Rádio está desligado ou volume é muito alto!"

        else:
            if self.__ligado == True:
                self.__volume += valor

        
    
    def diminuir_volume(self, valor=-1):
        if valor != -1: 
            if self.__ligado == True and valor <= self.__volume_min:
                self.__volume = valor
            else:
                return "Rádio está desligado ou volume é muito baixo!"

        else:
            if self.__ligado == True:
                self.__volume =- valor

         
    @property
    def frequencia(self):
        return self.__frequencia_atual
    

    @frequencia.setter
    def mudar_frequencia(self, valor):
        if self.__ligado == True and self.__antena_habilitada == True:
            if valor >= self.__freq_min and valor <= self.__freq_max:
                if valor in self.__estacoes:
                    self.__frequencia_atual = valor
                else:
                    return "Frequencia não existe"
                
            else:
                return "Está fora do valor minimo e máximo"
            
        else:
            return "O rádio está desligado ou a antena está desabilitada!"



                


