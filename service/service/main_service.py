import time
import json
from loguru import logger
from service.constants import mensagens

class CountPrimesService():

    def __init__(self):
        logger.debug(mensagens.INICIO_LOAD_SERVICO)

    def executar_rest(self, texts):
        logger.debug(mensagens.INICIO_COUNT)
        start_time = time.time()

        response_predicts = self.countPrimes(texts['number'])

        logger.debug(mensagens.FIM_COUNT)
        logger.debug(f"Fim da contagem em: {time.time() - start_time}")

        response = { "primeNumbers": response_predicts }

        return response

    def countPrimes(self, n):
        logger.debug('Iniciando a contagem de primos')

        if n < 2: return []

        A = [True for i in range(n)]
        p = 2

        while (p ** 2 <= n):
            if A[p]:
                for i in range(p ** 2, n, p):
                    A[i] = False
            p += 1
    
        return [i for i in range(2, len(A)) if A[i]]