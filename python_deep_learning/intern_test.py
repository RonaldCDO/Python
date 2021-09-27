import math as mt # biblioteca que utilizei para a função pow()
from os import path # biblioteca que utilizei para passar o caminho de um folder
import audiosegment # biblioteca que utilizei para converter os arquivos e para definir   
                    # a taxa de amostragem do sinal de áudio

#@author RonaldCDO


"""
@param audio: Esse parâmetro se refere ao nome do arquivo que está na pasta audio que está 
              em formato MP3, o nome a ser passado não precisa conter o .mp3, caso contrário,
              a função não irá funcionar
@param db: Esse parâmetro se refere ao volume, caso não seja passado esse argumento,
           por default o audio estará em seu volume normal, caso contrário, o volume será acrescido 
           ou decrescido do valor que for selecionado a partir do sinal positivo ou negativo
@return: A função tem como retorno um audio no formato WAV que será salvo em disco com o mesmo
         nome do arquivo mp3, porém com a extensão .wav
"""
def mp3_conversion(mp3_file, db = None):
    source = path.join('audio', mp3_file + '.' + 'mp3')
    destination = f"{mp3_file}.wav"
    if not type(mp3_file) is str:
        raise TypeError("Only String names are allowed")
    if db != None:
        if not type(db) is int:
            raise TypeError("Only int values are allowed")
    
    if db == None:
        audio = audiosegment.from_file(source).resample(sample_rate_Hz = 16*mt.pow(10,3),
                                                        sample_width = 1, channels = 1)
    else:
        audio = audiosegment.from_file(source).resample(sample_rate_Hz = 16*mt.pow(10,3),
                                                        sample_width = 1, channels = 1)
        audio = audio + db
    return audio.export(destination, format="wav")

# Exemplos de chamadas das funções de conversão
# mp3_conversion('nome-do-arquivo')
# mp3_conversion('hello-world', +10)
# mp3_conversion('hello-world', -10)

