import pyttsx3
import speech_recognition as sr
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from spotipy.oauth2 import SpotifyOAuth

client_id = "85ee62f65ba34c3189a447d7465de40d"
client_secret = "a650150996ee4965a2f6111c0c8b9de1"
redirect_uri = 'https://localhost:5550/callback'
scope = 'user-library-read user-read-private'

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id, 
                                       client_secret=client_secret,
                                       redirect_uri=redirect_uri,
                                       scope=scope))


voz = pyttsx3.init()

r = sr.Recognizer()



def get_opcao():
    opcoes = ['0', '1', '2', '3', '4']
    opcao = input ("Você escolheu a opção {opcao}: ")
    while opcao not in opcoes:
        opcao = input("Opção Inválida, digite novamente")
    return opcao

def menu_principal():
    print("===== Menu Principal =====")
    print("=                        =")
    print("= 1 - Qualquer coisa     =")
    print("= 2 - Buscar Album       =")
    print("= 3 - Buscar Genero      =")
    print("= 0 - Sair               =")
    print("==========================")
    voz.say("Opção um, Qualquer coisa. Opção dois, buscar álbum. Opção três, Buscar gênero. Opção zero, Sair.")
    voz.runAndWait()
    
    
while True:
    menu_principal()
    
    with sr.Microphone() as source:
        audio_data = r.record(source, duration=5)
        text = str(r.recognize_google(audio_data, language="pt-BR"))
        try:
            text = str(r.recognize_google(audio_data, language="pt-BR"))
        except sr.UnknownValueError:
            print("Não consegui entender sua fala.")
            voz.say("Não consegui entender sua fala.")
            voz.runAndWait()
            continue
        except sr.RequestError:
            print("Erro ao tentar se conectar ao serviço de reconhecimento.")
            voz.say("Erro ao tentar se conectar ao serviço de reconhecimento.")
            voz.runAndWait()
            continue
        
    if  text.strip() in ['1','2','3','0']:
        opcao = text.strip()
    else:
        opcao = get_opcao()
    
    if opcao == "0":
        break
    
    if opcao == "1":
        print("========= Menu 1 =========")
        print("=                        =")
        print("====   Nome artista   ====")
        print("= 0 - Sair               =")
        print("==========================")
        voz.say("Esse é o menu artistas, qual artista deseja procurar?.")
        voz.runAndWait()
        break
    
    if opcao == "2":
        album_name = input("Digite o nome do album: ")
        
        results = sp.search(q="album" + album_name, type="album")
        albums = results["albums"]["items"]
        
        if albums:
            for album in albums:
                print("nome do album: ", album["name"])
                print("Link: ", album["external_urls"]["spotify"])
                print("quantidade de faixas: ", album["total_tracks"])
                print("-------")
        break
    if opcao == "3":
        user_info = sp.current_user()
        print(user_info)