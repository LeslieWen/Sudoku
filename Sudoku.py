import subprocess
import sys
import PySimpleGUI as sg


#Define the window layout
sg.theme('DarkBlack1')
def main():
    layout=[
        [sg.Text("This program solves Sudoku puzzles by brute force.")],
        [sg.Output(size=(100,30), background_color='teal', text_color='white')],
        #[sg.T('Prompt> '),sg.Input(key='-IN-', do_not_clear=False)],
        [sg.Button('Run',bind_return_key=True)],
    ]

    window=sg.Window("Sudoku",layout)

    #Event loop

    while True:
        event, values = window.read()
        #End program if user closes window or
        #presses the OK button
        if event == sg.WIN_CLOSED:
            break
        elif event == 'Run':
            runCommand(cmd=values['py -c \'from testers import test1; test1()\''],window=window)
    window.close()

def runCommand(cmd,timeout=None,window=None):
    nop=None
    p=subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
    output=''
    for line in p.stdout:
        line=line.decode(errors='replace' if (sys.version_info)< (3,5) else 'backslashreplace').rstrip()
        outplut+=line
        print(line)
        window.refresh() if window else nop
    retval = p.wait(timeout)
    return (retval, output)

main()