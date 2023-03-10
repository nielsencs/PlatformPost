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

                [sg.Text('Facebook', font=("Helvetica", 15))],
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

                [sg.Text('Patreon', font=("Helvetica", 15))],
                [sg.InputText(key='tPA')],
                [sg.Button('Copy', key='bPA')],

                [sg.Submit(), sg.Cancel()]
            ]

    window = sg.Window(app_name, layout)
    bDoit = True
    while bDoit:
        event, values = window.read()
        if event == 'bGO':
            tags = window['Tags'].Get()
            facebook_tags = split_tags(tags, ',', False, True)

            window['tYT'].update(split_tags(tags, ',', False, False))
            window['tTT'].update(window['Title'].Get() + ' ' + split_tags(tags, '#', True, False))
            window['tFB1'].update(facebook_tags[0])
            window['tFB2'].update(facebook_tags[1])
            window['tFB3'].update(facebook_tags[2])
            window['tFB4'].update(facebook_tags[3])
            window['tFB5'].update(facebook_tags[4])
            window['tFB6'].update(facebook_tags[5])
            window['tFB7'].update(facebook_tags[6])
            window['tFB8'].update(facebook_tags[7])
            window['tPA'].update(split_tags(tags, '#', True, False))
        # elif event[1] == 'b':  # a button clicked
        #     sg.clipboard_set(window['t' + event[1:]].Get()) # get associated text field value
        if event[1] == 'bYT':  # YouTube button clicked
            sg.clipboard_set(window['tYT'].Get()) # get associated text field value
        if event[1] == 'bTT':  # YouTube button clicked
            sg.clipboard_set(window['tTT'].Get()) # get associated text field value
        if event[1] == 'bTW':  # YouTube button clicked
            sg.clipboard_set(window['tFB'].Get()) # get associated text field value
        if event[1] == 'bPA':  # YouTube button clicked
            sg.clipboard_set(window['tPA'].Get()) # get associated text field value
        # sg.popup('Title',
        #         'The results of the window.',
        #         'The button clicked was "{}"'.format(event),
        #         'The values are', values)

        if event == 'Submit' or event == 'Cancel':
            bDoit = False

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