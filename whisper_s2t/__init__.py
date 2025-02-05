import os
from platformdirs import user_cache_dir


BASE_PATH = os.path.dirname(__file__)

CACHE_DIR = user_cache_dir("whisper_s2t")
os.makedirs(CACHE_DIR, exist_ok=True)


def load_model(model_identifier="large-v2", 
               backend='CTranslate2', 
               **model_kwargs):
    
    if backend.lower() in ["ctranslate2", "ct2"]:
        from .backends.ctranslate2.model import WhisperModelCT2 as WhisperModel

    elif backend.lower() in ["huggingface", "hf"]:
        from .backends.huggingface.model import WhisperModelHF as WhisperModel
        model_identifier = f"openai/whisper-{model_identifier}"

    elif backend.lower() in ["openai", "oai"]:
        from .backends.openai.model import WhisperModelOAI as WhisperModel

    else:
        raise ValueError(f"Backend name '{backend}' is invalid. Only following options are available: ['CTranslate2', 'HuggingFace', 'OpenAI']")
        
    return WhisperModel(model_identifier, **model_kwargs)
        