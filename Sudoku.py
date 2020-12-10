import PySimpleGUI as sg

from bruteForce import *
from helpers import * 

arr=[
[0,3,9,2,0,8,7,1,5],
[6,0,8,0,0,1,0,0,0],
[0,5,0,9,3,0,8,4,6],
[7,0,4,0,1,0,0,5,8],
[8,1,0,6,4,0,3,7,0],
[0,2,0,8,0,5,1,0,4],
[5,0,3,0,9,0,0,2,1],
[0,4,1,5,0,3,0,0,7],
[9,0,0,1,2,0,5,8,0]]

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
        window.Refresh()
        (event, values) = window.Read()
        if event =='EXIT' or event is None:
            break
        if event =='Run':
            boardPrinter(arr)
    window.Close()

main()