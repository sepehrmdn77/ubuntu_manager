from flet import *
import subprocess
from time import sleep

blue1 = '#000B49'
blue2 = '#000D6B'
blue3 = '#0C1E7F'
bg1 = '#1D1B38'
bg2 = '#060930'
navy = '#7FA1C3'
orange = '#FB773C'

def main(page: Page):
    page.horizontal_alignment="center"
    # page.vertical_alignment='center'
    page.title="Linux sys admin"
    page.bgcolor = blue1
    page.window.height=900
    page.window.width=600
    
    page_name = TextField(value='Welcome to Linux system administration application',
                          read_only=True,
                          width=550,
                          border_radius=15,
                          border_color='transparent',
                          text_align='center',
                          text_size=21,
                          helper_text='Ubuntu',
                          )
    
    monitor = Column(controls=[Text(value='',bgcolor='',size=20)],scroll='auto')
    
    def click_1(e):
            if e.control.content.value == 'pwd':
                monitor.controls[0].value = ''
                page.update()
                monitor.controls[0].value = subprocess.check_output('pwd',shell=True,text=True)
                page.update()
                # sleep(5)
                # monitor.controls[0].value = ''
                page.update()
            elif e.control.content.value == 'whoami':
                monitor.controls[0].value = ''
                page.update()
                monitor.controls[0].value = subprocess.check_output('whoami',shell=True,text=True)
                page.update()
                # sleep(5)
                # monitor.controls[0].value = ''
                # page.update()
            elif e.control.content.value == "pakages update & upgrade":
                monitor.controls[0].value = ''
                page.update()
                monitor.controls[0].value = 'Updating repositories...'
                page.update()
                subprocess.run('sudo apt update',shell=True,text=True)
                monitor.controls[0].value = 'Upgrading packages...'
                page.update()
                subprocess.run('sudo apt upgrade -y',shell=True,text=True)
                monitor.controls[0].value = 'Done!'
                page.update()
                # sleep(5)
                # monitor.controls[0].value = ''
                # page.update()
            elif e.control.content.value == 'date':
                monitor.controls[0].value = ''
                page.update()
                monitor.controls[0].value = subprocess.check_output('date',shell=True,text=True)
                page.update()
                # sleep(5)
                # monitor.controls[0].value = ''
                # page.update()
            elif e.control.content.value == 'who':
                monitor.controls[0].value = ''
                page.update()
                monitor.controls[0].value = subprocess.check_output('who',shell=True,text=True)
                page.update()
                # sleep(5)
                # monitor.controls[0].value = ''
                # page.update()
            elif e.control.content.value == 'nmcli':
                monitor.controls[0].value = ''
                page.update()
                monitor.controls[0].value = subprocess.check_output('nmcli',shell=True,text=True)
                page.update()
            elif e.control.content.value == 'Hard disk usage':
                monitor.controls[0].value = ''
                page.update()
                monitor.controls[0].value = subprocess.check_output('../scripts/hard_disk_manger.sh',shell=True, text=True)
                page.update()
                # sleep(5)
                # monitor.controls[0].value = ''
                # page.update()
            elif e.control.content.value == 'ifconfig':
                monitor.controls[0].value = ''
                page.update()
                monitor.controls[0].value = subprocess.check_output('ifconfig',shell=True, text=True)
                page.update()
            # elif e.control.content.value == 'journalctl':
            #     monitor.controls[0].value = ''
            #     page.update()
            #     monitor.controls[0].value = subprocess.check_output('journalctl',shell=True, text=True)
            #     page.update()

            elif e.control.content.value == 'Welcome screen':
                monitor.controls[0].value = 'Enter a command below to\nrun the command without\nengaging with CLI.\nYou can adjust this screen\ntext size with - and + below. '
                page.update()

            elif e.control.content.value == 'Clear screen':
                monitor.controls[0].value = ''
                page.update()


    main_container = Column(controls=[Container(
            content=Container(
                    content=monitor,
                    margin=5,
                    padding=5,
                    alignment=alignment.center,
                    bgcolor=bg2,
                    height=250,
                    width=450,
                    border_radius=15
                    )
                ,width=500,
                height=250,
                bgcolor='grey',
                border_radius=15
                )
            ]
        )
    main_tile = ExpansionTile(
        title=Text(value="Commands",text_align='center'),
        bgcolor=('white12'),
        opacity=0.8,
        width=480,
        collapsed_bgcolor=bg2,
        subtitle=Text(value="Choose the command below",text_align='center'),
        affinity=TileAffinity.PLATFORM,
        maintain_state=True,
        collapsed_text_color=Colors.WHITE,
        text_color=Colors.WHITE,
        controls=[
                Divider(color=bg2,height=1,opacity=0.5),
                Row(controls=[Container(
                                            content=ElevatedButton(
                                                 content=Text("pwd",color='black'),on_click=click_1,height=35,width=55,color='white',bgcolor=navy)
                                            ,padding=10)
                                ,Container(
                                            content=ElevatedButton(
                                                 content=Text("whoami",color='black'),on_click=click_1,height=35,width=75,color='white',bgcolor=navy)
                                            ,padding=10)
                                ,Container(
                                            content=ElevatedButton(
                                                 content=Text("date",color='black'),on_click=click_1,height=35,width=55,color='white',bgcolor=navy)
                                            ,padding=10)
                                ,Container(
                                            content=ElevatedButton(
                                                 content=Text("who",color='black'),on_click=click_1,height=35,width=55,color='white',bgcolor=navy)
                                            ,padding=10)
                                ]
                    ,spacing=1
                    ,alignment='center'
                    ),
                Divider(color=bg2,height=1,opacity=0.5),
                Row(controls=[Container(
                                            content=ElevatedButton(
                                                 content=Text("pakages update & upgrade",color='black'),on_click=click_1,height=35,width=200,color='white',bgcolor=navy)
                                            ,padding=5)
                               ]
                    ,spacing=1
                    ,alignment='center'
                    ),
                Divider(color=bg2,height=1,opacity=0.5),
                Row(controls=[Container(
                                            content=ElevatedButton(
                                                 content=Text("nmcli",color='black'),on_click=click_1,height=35,width=75,color='white',bgcolor=navy)
                                            ,padding=10)
                                ,Container(
                                            content=ElevatedButton(
                                                 content=Text("ifconfig",color='black'),on_click=click_1,height=35,width=75,color='white',bgcolor=navy)
                                            ,padding=10)
                                ]
                    ,spacing=1
                    ,alignment='center'
                    ),
                Divider(color=bg2,height=1,opacity=0.5),
                Container(
                                            content=ElevatedButton(
                                                 content=Text("Hard disk usage",color='black'),on_click=click_1,height=35,width=150,color='white',bgcolor=navy)
                                            ,padding=5),
                # Divider(color=bg2,height=1,opacity=0.5),
                # Container(
                #                             content=ElevatedButton(
                #                                  content=Text("welcome screen",color='black'),on_click=click_1,height=35,width=100,color='white',bgcolor=navy)
                #                             ,padding=5),
                Divider(color=bg2,height=1,opacity=0.5),
                Row(controls=[Container(
                                            content=ElevatedButton(
                                                 content=Text("Clear screen",color='white',weight='W800',size=17),on_click=click_1,height=35,width=150,color='',bgcolor='#FF8225')
                                            ,padding=10),
                            Container(
                                            content=ElevatedButton(
                                                 content=Text("Welcome screen",color='black'),on_click=click_1,height=35,width=150,color='white',bgcolor='white')
                                            ,padding=5),
                Divider(color=bg2,height=1,opacity=0.5),
                                ]
                    ,spacing=1
                    ,alignment='center'
                    ),
            ],
        )


    in_1 = Container(content=main_tile)

    # def sudo(e):
        # subprocess.run('sudo su',shell=True, text=True)
        
    #echo "YourPassword" | sudo -S su

    def save_pass(e):
            if not pass_field.value:
                monitor.controls[0].value = 'Please enter a valid sudo password!'
                page.update()
                sleep(5)
                monitor.controls[0].value = ''
                page.update()
            else:
                password = pass_field.value
                subprocess.run(['sudo su'],shell=True, text=True)
                monitor.controls[0].value = 'You have logined successfully!'
                page.update()
                monitor.controls[0].value = ''
                page.update()


            # print(e.control[0].value)
    pass_field = TextField(
                                        width=250,
                                        height=50,
                                        label="sudo password",
                                        border_radius=15,
                                        bgcolor='whte12',
                                        password=True
                                    )
    pass_btn = Container(
                                        content=Text('Go sudo',text_align='center',size=12),
                                        ink=True,
                                        padding=4,
                                        height=45,
                                        width=45,
                                        border_radius=15,
                                        bgcolor='white12',
                                        on_click=save_pass,
                                    )
    sudo_pass = Row(
                    controls=[
                            pass_field,
                            pass_btn
                            ],
                    alignment='center',
                    )
    
    hint = TextField(
                    value='Hint: Use this app as sudo',
                    text_align='center',text_size=17,
                    bgcolor='white12',
                    width=480,
                    border_color='transparent',
                    border_radius=15,
                    read_only=True
                    )

    space = Container(height=10)

    def minus_click(e):
         monitor.controls[0].size -= 1
         page.update()
    def plus_click(e):
         monitor.controls[0].size += 1
         page.update()


    text_size_m = Row(
            [
                IconButton(Icons.REMOVE, on_click=minus_click,bgcolor='white12'),
                TextField(value='Monitor text size',text_align='center',read_only=True,width=170,border_color='transparent'),
                IconButton(Icons.ADD, on_click=plus_click,bgcolor='white12'),
            ],
            alignment=MainAxisAlignment.CENTER,
        )

    page.add(page_name,main_container,text_size_m,hint,in_1)
    page.update()

    # Welcomer
    help = 'Enter a command below to\nrun the command without\nengaging with CLI.\nYou can adjust this screen\ntext size with - and + below. '
    monitor.controls[0].value = help
    page.update()
    sleep(15)
    monitor.controls[0].value = ''
    page.update()


app(target=main)