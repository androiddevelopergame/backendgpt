from openai import AsyncOpenAI
from dotenv import load_dotenv
import base64
import os


# Загрузка переменных окружения
load_dotenv()
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")


# Базовая функция взаимодействия с OpenAI
async def answer_gpt(query: str,
                     model='gpt-4o-mini',
                     temp=0.1):
    messages = [
        {"role": "system", "content": 'Ответь на вопрос'},
        {"role": "user", "content": query}]
    return await AsyncOpenAI().chat.completions.create(
        model=model,
        messages=messages,
        temperature=temp)


# Распознавание изображений
async def image_recognition(image_path: str,
                            picture_prompt='Распознай изображение и опиши что ты видишь. \
                                            Если на изображении есть текст, выведи. \
                                            Если в тексте есть вопрос, ответь на вопрос',
                            model='gpt-4o'):
    with open(image_path, "rb") as image_file:
        base64_image = base64.b64encode(image_file.read()).decode('utf-8')
    messages = [{"role": "user", "content":
                 [{"type": "text", "text": picture_prompt},
                  {"type": "image_url",
                   "image_url": {"url": f"data:image/jpeg;base64,{base64_image}"}}]}]
    return await AsyncOpenAI().chat.completions.create(
        model=model,
        messages=messages)


# STT Звук в текст
async def stt_whisper_online(voice_file: str,
                             model='whisper-1'):
    with open(voice_file, "rb") as audio_file:
        return await AsyncOpenAI().audio.transcriptions.create(
            model=model,
            file=audio_file)
