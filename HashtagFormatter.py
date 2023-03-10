import PySimpleGUI as sg

def gui():
    sg.theme('Dark Blue 3')
    app_name = 'SocialTagFormatter'

    layout = [
                [sg.Text(app_name, font=("Helvetica", 25))],

                [sg.Text('Title', font=("Helvetica", 15))],
                [sg.InputText(key='Title')],

                [sg.Text('Tags', font=("Helvetica", 15))],
                [sg.InputText(key='Tags')],
                [sg.Button('Go', key='bGO')],

                [sg.Text('YouTube', font=("Helvetica", 15))],
                [sg.InputText(key='tYT')],
                [sg.Button('Copy', key='bYT')],

                [sg.Text('TikTok, Instagram & Twitter', font=("Helvetica", 15))],
                [sg.InputText(key='tTT')],
                [sg.Button('Copy', key='bTT')],

                [sg.Text('Facebook & Patreon', font=("Helvetica", 15))],
                [sg.InputText(key='tFB1')],
                [sg.Button('Copy', key='bFB1')],
                [sg.InputText(key='tFB2')],
                [sg.Button('Copy', key='bFB2')],
                [sg.InputText(key='tFB3')],
                [sg.Button('Copy', key='bFB3')],
                [sg.InputText(key='tFB4')],
                [sg.Button('Copy', key='bFB4')],
                [sg.InputText(key='tFB5')],
                [sg.Button('Copy', key='bFB5')],
                [sg.InputText(key='tFB6')],
                [sg.Button('Copy', key='bFB6')],
                [sg.InputText(key='tFB7')],
                [sg.Button('Copy', key='bFB7')],
                [sg.InputText(key='tFB8')],
                [sg.Button('Copy', key='bFB8')],
            ]

    window = sg.Window(app_name, layout)

    while True:
        event, values = window.read()
        if event == 'bGO':
            tags = window['Tags'].Get()
            facebook_tags = split_tags(tags, ',', False, True)

            window['tYT'].update(split_tags(tags, ',', False, False))
            window['tTT'].update(window['Title'].Get() + ' ' + split_tags(tags, '#', True, False))
            i = 0
            for tag in facebook_tags:
                if i >= 8:
                    break
                i += 1
                window['tFB'+ str(i)].update(tag.strip())
        # elif event[1] == 'b':  # a button clicked
        #     sg.clipboard_set(window['t' + event[1:]].Get()) # get associated text field value
        if event == 'bYT':  # YouTube button clicked
            sg.clipboard_set(window['tYT'].Get()) # get associated text field value
        if event == 'bTT':  # TikTok button clicked
            sg.clipboard_set(window['tTT'].Get()) # get associated text field value
        if event[:-1] == 'bFB':  # Facebook button clicked
            sg.clipboard_set(window['tFB' + event[-1]].Get()) # get associated text field value

def split_tags(text, hash, singles, facebook):
    tags = text.split(',')
    tags_new = ''

    if facebook:
        tags_new = tags
    else:
        for tag in tags:
            tag = tag.strip()
            if singles and (' ' in tag):
                tag = tag[0] + tag.title()[1:] #capitalise all but first char
                tag = tag.replace(' ', '')
            if hash == '#':
                tags_new += ' ' + hash + tag
            else:
                tags_new += tag + hash

        if hash == '#':
            tags_new = tags_new[1:]
        else:
            tags_new = tags_new[:-1]

    return tags_new
    # print(text.split(','))

gui()