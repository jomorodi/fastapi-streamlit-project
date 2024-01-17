#pip install -q torchaudio omegaconf



from enum import Enum

model_setting = {"english": ("en_0", "https://models.silero.ai/models/tts/en/v3_en.pt") , "german":("eva_k" , "https://models.silero.ai/models/tts/de/v3_de.pt") ,"spanish" :("es_0" , "https://models.silero.ai/models/tts/es/v3_es.pt"), "french" :("fr_0" , "https://models.silero.ai/models/tts/fr/v3_fr.pt")}

class ModelLanguage(str, Enum):
    english = "english"
    russian = "russian"
    
    german = "german"
    spanish = "spanish"
    french = "french"
    
"""    
language = 'en'
speaker = 'lj_16khz'
device = torch.device('cpu')
model, symbols, sample_rate, example_text, apply_tts = torch.hub.load(repo_or_dir='snakers4/silero-models',
                                                                      model='silero_tts',
                                                                      language=language,
                                                                      speaker=speaker)
model = model.to(device)  # gpu or cpu
audio = apply_tts(texts=[example_text],
                  model=model,
                  sample_rate=sample_rate,
                  symbols=symbols,
                  device=device)
speaker_id = ["v3_en", "v3_1_ru" , "v3_de" ,"v3_es" , "v3_fr" ]

def modelSelect (inp : ModelLanguage):
    if inp is ModelLanguage.english:
        return ('en' , "v3_en")
    if inp is ModelLanguage.russian:
        return ('ru' ,"v3_1_ru")
    if inp is ModelLanguage.german:
        return ('de', "v3_de")
    if inp is ModelLanguage.spanish:
        return ('es' ,"v3_es" )
    if inp is ModelLanguage.french:
        return ('fr' , "v3_fr")



    
def process (inp : ModelLanguage):
    setting = modelSelect (inp )
    language = setting [0]
    speaker = 'random'
    device = torch.device('cpu')
    model, symbols, sample_rate, example_text, apply_tts = torch.hub.load(repo_or_dir='snakers4/silero-models',
                                                                          model='silero_tts',
                                                                          language=language,
                                                                          speaker=setting[1])
    model = model.to(device)  # gpu or cpu
    audio = apply_tts(texts=[example_text],
                      model=model,
                      sample_rate=sample_rate,
                      speaker = speaker ,
                      symbols=symbols,
                      device=device)
    return audio
    
"""

def select (inp : ModelLanguage):
    return model_setting [inp]

def tospeech (txt , inp):
    import torch
    #import simpleaudio as sa
    import os


    device = torch.device('cpu')
    torch.set_num_threads(4)
    local_file = f'model{select (inp)[0]}.pt'

    if not os.path.isfile(local_file):
        torch.hub.download_url_to_file(select (inp)[1],
                                       local_file)  

    model = torch.package.PackageImporter(local_file).load_pickle("tts_models", "model")
    model.to(device)

    
    sample_rate = 48000
    speaker='random'


    audio_paths = model.save_wav(text=txt,
                                 speaker=speaker,
                                 sample_rate=sample_rate)
    with open (audio_paths , 'rb') as fi :
        result = fi.read()
        return result
        
    



#print (dir(model))
#print (audio_paths)
#play_obj = sa.play_buffer(audio, 2, 2, 44100)
#play_obj.wait_done()

#https://models.silero.ai/models/tts/en/v3_en.pt
#https://models.silero.ai/models/tts/ru/v3_1_ru.pt    