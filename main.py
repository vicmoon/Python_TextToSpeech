from google.cloud import texttospeech 


#initialize client 
client = texttospeech.TextToSpeechClient()

with open("story.txt", "r") as file:
    text_content = file.read()

if not text_content.strip():
    print("No text found in the file ")
    exit()



text_input = texttospeech.SynthesisInput(text=text_content)


voice = texttospeech.VoiceSelectionParams(
    language_code="en-US", 
    ssml_gender=texttospeech.SsmlVoiceGender.MALE
)

audio_config = texttospeech.AudioConfig(
    audio_encoding=texttospeech.AudioEncoding.MP3
)

response = client.synthesize_speech(
    input=text_input, 
    voice=voice, 
    audio_config=audio_config
)

with open("output.mp3", "wb") as out:
    out.write(response.audio_content)
    print("Audio content written to the file output.mp3")