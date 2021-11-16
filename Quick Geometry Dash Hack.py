import PySimpleGUI as sg
from gd import memory
import gd as gd
import keyboard
import gdrpc

memory = memory.get_memory()
client = gd.Client()
get_speed = memory.get_speed()


class TelaPython():
    def __init__(self):
        sg.theme('Default')

        layout = [
            [sg.Text("meu nome é Rahony :3", justification='center', size=(70, 1))],
            [sg.Button('misc'), sg.Button('Editor'), sg.Button(
                'enable Anticheat'), sg.Button('disable Anticheat'), sg.Button('user info')],
            [sg.P()],
            [sg.Text("Hacks padrões", justification='center',
                     font='PUSAB 20', text_color='RoyalBlue', size=(33, 1))],
            [sg.CBox('Ativar NoClip', size=(20, 0), key='noclipone'),
             sg.Text("Desativa a colisão do jogador")],
            [sg.CBox('Desativar rotação', size=(20, 0), key='rotacao'),
             sg.Text("Desativa a rotação do jogador")],
            [sg.CBox('Pratice music bypass', size=(20, 0), key='praticeMusic'), sg.Text(
                "Desativa a musica padrão do modo pratica")],
            [sg.CBox('Ativar Discord RPC', size=(20, 0), key='discordrpc'),
             sg.Text("Ativa o discord Rich Presence")],
            [sg.CBox("Freezar Player", size=(20, 0), key='playerfreeze'),
             sg.Text("Faz com que o jogador pare")],
            [sg.CBox("Level Edit Bypass", size=(20, 0), key='levelEditBypass'),
             sg.Text("Permite editar qualquer nível")],
            [sg.CBox("Porcentagem Precisa", size=(20, 0), key='porcentagem'),
             sg.Text("Mostra a portentagem precisa do nível")],
            [sg.CBox("Copiar Nível", size=(20, 0), key='levelCopy'),
             sg.Text("Permite Copiar qualquer nível")],
            [sg.Button('atualizar cheats', size=(40, 1))]

        ]
        layout2 = [
            [sg.Text("MISC", justification='center', font='PUSAB 20',
                     text_color='RoyalBlue', size=(33, 1))],
            [sg.CBox('ativar Discord RPC', size=(20, 0)), sg.Text(
                "Mostra o que você está fazendo no Geometry Dash")],
            [sg.CBox('modo plataforma', size=(20, 0), key='plataformauwu'),
             sg.Text("ativa o modo plataforma no jogo")],
            [sg.Button("ativar cheats")]
        ]

        self.janela = sg.Window("Mega Hack V7 fodase", layout, size=(500, 400))
        self.miscelanos = sg.Window("Mega Hack V7 Misc", layout2)

    def Iniciar(self):
        while True:
            self.event, self.values = self.janela.read()
            noclipone = self.values['noclipone']
            noclipon = memory.enable_noclip
            noclipoff = memory.disable_noclip

            rotacao = self.values['rotacao']
            rotacaoon = memory.player_lock_jump_rotation()
            rotacaooff = memory.player_unlock_jump_rotation()

            pmusica = self.values['praticeMusic']
            pmusicaon = memory.enable_practice_song()
            pmusicaoff = memory.disable_practice_song()

            congelar = self.values['playerfreeze']
            player_freeze = memory.player_freeze()
            player_unfreeze = memory.player_unfreeze()
            
            leveledit = self.values['levelEditBypass']
            enable_level_edit = memory.enable_level_edit()
            disable_level_edit = memory.disable_level_edit()
            
            porcentagem = self.values['porcentagem']
            enable_accurate_percent = memory.enable_accurate_percent()
            disable_accurate_percent = memory.disable_accurate_percent()
            
            levelcopy = self.values['levelCopy']
            enable_level_copy = memory.enable_level_copy()
            disable_level_copy = memory.disable_level_copy()
            
            
            
            if self.event == sg.WINDOW_CLOSED:
                break




        # Ativar/Desativar Anticheat
            if self.event == ('enable Anticheat'):
                enable_anticheat = memory.enable_anticheat()
                enable_anticheat
                print("anticheat ativado")
            elif self.event == ('disable Anticheat'):
                disable_anticheat = memory.disable_anticheat()
                disable_anticheat
                print("anticheat desativado")

        # Comando NoClip
            if noclipone == True:
                noclipon = memory.enable_noclip()
                noclipon
                print("noClip ativado")
            elif noclipone == False:
                noclipoff = memory.disable_noclip()
                noclipoff

        # comando de Rotação
            if rotacao == True:
                rotacaoon = memory.player_lock_jump_rotation()
                rotacaoon
            elif rotacao == False:
                rotacaooff = memory.player_unlock_jump_rotation()
                rotacaooff

        # Comando do Practice Hack
            if pmusica == True:
                pmusicaon = memory.enable_practice_song()
                pmusicaon
            elif pmusica == False:
                pmusicaoff = memory.disable_practice_song()
                pmusicaoff

        # coisas da barra MISC
            if self.event == ('misc'):
                sg.popup(
                    "os misc estão desativados por conter vários bugs, desculpe :c")
            #     self.event2, self.values2 = self.miscelanos.read()
            #     plataforma = self.values2['plataformauwu']
            # #modo plataforma
            #     if plataforma == True:
            #         if keyboard.is_pressed ("left"):
            #             set_speed = memory.set_speed_value(-1.0)
            #         elif keyboard.is_pressed ("right"):
            #             set_speed = memory.set_speed_value(1.0)
            #         else:
            #             velocidade = 0.0
            #             set_speed = memory.set_speed_value(velocidade)

            #         if keyboard.is_pressed ("1"):
            #             set_gravity = memory.set_gravity(gravity=1.0)
            #         elif keyboard.is_pressed("2"):
            #             set_gravity = memory.set_gravity(gravity=-1.0)
            #     else:
            #         pass

        # comando do ping do servidor do gd
            if self.event == ('user info'):
                nome = gd.Level.name
                sg.popup(f"nome: {nome}")
                
        # parar o jogador
            if congelar == True:
                player_freeze = memory.player_freeze()
                player_freeze
            elif congelar == False:
                player_unfreeze = memory.player_unfreeze()
                player_unfreeze
                
        # Editar níveis
            if leveledit == True:
                enable_level_edit = memory.enable_level_edit()
                enable_level_edit
            elif leveledit == False:
                disable_level_edit = memory.disable_level_edit()
                disable_level_edit
                
        #Mostra porcentagem Precisa
            if porcentagem == True: 
                enable_accurate_percent = memory.enable_accurate_percent()
                enable_accurate_percent
            elif porcentagem == False:
                disable_accurate_percent = memory.disable_accurate_percent()
                disable_accurate_percent
                
        #another
            if levelcopy == True:   
                enable_level_copy = memory.enable_level_copy()
                enable_level_copy
            elif levelcopy == False:
                disable_level_copy = memory.disable_level_copy()       
                disable_level_copy         
                
                

        # Deixe isso por ultimo sempre
            print("yay >w<")


tela = TelaPython()
tela.Iniciar()
