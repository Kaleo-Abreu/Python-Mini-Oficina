estacoes = {86.5:'Cocais', 91.5: 'Mix', 94.1:'Boa', 99.1:'Clube'}

class RadioFM:
    def __init__(self, vol_max, estacoes):
        self.__volume_min = 0
        self.__volume_max = vol_max
        self.__freq_min = 88
        self.__freq_max = 108
        self.__estacoes = estacoes
        self.__volume = None
        self.__ligado = False
        self.__estacao_atual = None
        self.__frequencia_atual = None
        self.__antena_habilitada = False

    # ---------------- PROPRIEDADES ----------------
    @property
    def ligado(self):
        return self.__ligado

    @property
    def volume(self):
        return self.__volume

    @property
    def estacao_atual(self):
        return self.__estacao_atual

    @property
    def frequencia_atual(self):
        return self.__frequencia_atual

    # ---------------- LIGAR/DESLIGAR ----------------
    def ligar(self):
        if not self.__ligado:
            if not self.__antena_habilitada:
                return "A antena não está habilitada!"
            
            self.__ligado = True
            self.__volume = self.__volume_min

            # define primeira estação
            primeira_freq = list(self.__estacoes.keys())[0]
            self.__frequencia_atual = primeira_freq
            self.__estacao_atual = self.__estacoes[primeira_freq]
        else:
            return "O rádio já está ligado"

    def desligar(self):
        if self.__ligado:
            self.__ligado = False
            self.__volume = None
            self.__frequencia_atual = None
            self.__estacao_atual = None
        else:
            return "O rádio já está desligado!"

    # ---------------- ANTENA ----------------
    def habilitar_antena(self):
        self.__antena_habilitada = True

    def desabilitar_antena(self):
        self.__antena_habilitada = False

    # ---------------- VOLUME ----------------
    @volume.setter
    def volume(self, valor):
        if not self.__ligado:
            return "Rádio está desligado!"

        if self.__volume_min <= valor <= self.__volume_max:
            self.__volume = valor
        else:
            return "Volume fora do limite!"

    def aumentar_volume(self, passo=1):
        if not self.__ligado:
            return "Rádio está desligado!"

        novo_volume = self.__volume + passo
        self.__volume = min(novo_volume, self.__volume_max)

    def diminuir_volume(self, passo=1):
        if not self.__ligado:
            return "Rádio está desligado!"

        novo_volume = self.__volume - passo
        self.__volume = max(novo_volume, self.__volume_min)

    # ---------------- FREQUÊNCIA ----------------
    @frequencia_atual.setter
    def frequencia_atual(self, valor):
        if not (self.__ligado and self.__antena_habilitada):
            return "O rádio está desligado ou a antena está desabilitada!"

        if valor in self.__estacoes:
            self.__frequencia_atual = valor
            self.__estacao_atual = self.__estacoes[valor]
        else:
            return "Estação inexistente"

    def proxima_estacao(self):
        if not (self.__ligado and self.__antena_habilitada):
            return "O rádio está desligado ou a antena está desabilitada!"

        chaves = list(self.__estacoes.keys())
        idx = chaves.index(self.__frequencia_atual)
        proximo_idx = (idx + 1) % len(chaves)

        self.__frequencia_atual = chaves[proximo_idx]
        self.__estacao_atual = self.__estacoes[self.__frequencia_atual]
