import PySimpleGUI as sg

func = {'button_color':('white', '#696969'), 'size':(5,2), 'font':("Arial", 24), 'pad':(0,0)}
numb = {'button_color':('white', 'black'), 'size':(5,2), 'font':("Arial", 24), 'pad':(0,0)}
equal = {'button_color':('white', 'black'), 'size':(9,2), 'font':("Arial", 24), 'pad':(0,0)}

# Define the window's contents
layout = [
     [sg.Text('Python Calculator', font=('Arial',15), size=(20,1), justification='left', background_color='black', text_color='white')],
     [sg.Text('', font=('Arial',20), size=(23,1), justification='right', background_color='black', text_color='white', key="__VALUEDISP__")],
     [sg.Text('0',font=('Arial',50), size=(10,1), justification='right', background_color='black', text_color='white', key="__DISPLAY__")],
     [sg.Button('%', **func), sg.Button('CE', **func), sg.Button('C',**func), sg.Button('/', **func)],
     [sg.Button('7', **numb), sg.Button('8', **numb), sg.Button('9',**numb), sg.Button('*', **func)],
     [sg.Button('4', **numb), sg.Button('5', **numb), sg.Button('6', **numb), sg.Button('-', **func)],
     [sg.Button('1', **numb), sg.Button('2', **numb), sg.Button('3', **numb), sg.Button('+', **func)],
     [sg.Button('0', **numb), sg.Button(',', **numb), sg.Button('', **numb), sg.Button('=', **func)]]


# Create the window
window = sg.Window('Calculadora ', layout=layout, background_color='black', return_keyboard_events=True)



#FUNCTIONS
var = {'main':[], 'back': [], 'x_val': 0, 'y_val': 0, 'operator': '', 'result': 0, 'decimal': False}

def format_number():
    if var['decimal'] == True:
        return float(''.join(var['main']) + '.' + ''.join(var['back']))
    else:
        return int(''.join(var['main']))


#--------updates display--------
def update_display(display_value: str):
    try:
        window['__DISPLAY__'].update(value='{:,.4f}'.format(display_value))
    except:
        window['__DISPLAY__'].update(value=display_value)


#--------Number click function--------
def click_number(event: str):
    global var
    if var['decimal']:
        var['back'].append(event)
    else: 
        var['main'].append(event)
    update_display(format_number())

#--------Operator click function--------
def operator_click(event: str):
    global var
    var['operator'] = event
    var['x_val'] = format_number()
    clear_display()

def calculate_click():
    global var
    var['y_val'] = format_number()

    try:
        var['result'] = eval(str(var['x_val']) + var['operator'] + str(var['y_val']))
        update_display(var['result'])
        clear_display()
    except:
        update_display("Error! Div/0")
        clear_display()
    

def clear_display():
    global var
    var['main'].clear()
    var['back'].clear()
    var['decimal'] = False

# interact with the Window using an Event Loop
while True:
    event, values = window.read()
    print(event)
    # See if user wants to quit or window was closed
    if event is None:
        break
    if event in ['0','1','2','3','4','5','6','7','8','9']:
        click_number(event)
    if event in ['C', 'CE', '<<<']:
        clear_display()
        update_display(0)

    if event in['+', '-', '*', '/']:
        operator_click(event)
    if event == '=':
        calculate_click()
    if event == '':
        clear_display()
        update_display('Try again!')
    if event == ',':
        var['decimal'] = True
    
    if event == '%':
        update_display(var['result'] / 100)
    
   
        
    

    


# Finish up by removing from the screen
window.close()

#https://pysimplegui.readthedocs.io/en/latest/