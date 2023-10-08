import PySimpleGUI as sg
import time
import backend as back
        
def main():
    # sg.theme('LightBlue7')

    # # Loading Screen
    # loading = [[sg.Text('Fun Fact')], [sg.Button('Start')]]
    # loadingWindow = sg.Window('Loading', loading, size=(500,500), element_justification='c')
            
    # #Loading Screen
    # loadingEvent, loadingValues = loadingWindow.read()
    # if (loadingEvent==sg.WIN_CLOSED or loadingEvent=="Start"):
    #     loadingWindow.close()
    main_menu()

def subwindow_handler(subwindow):
    subevent, subvalues = subwindow.read()
    if(subevent==sg.WIN_CLOSED):
        subwindow.close()
        main_menu()


def main_menu():
    #Home
    long, lat = back.return_longlat()
    city, province = back.findClosestCity(long, lat)

    back.redownload_lakes_excel()
    layout = [  [sg.Image('canadamap.png')],
                [sg.Button('Refresh'),],
                [sg.Text(f'Weather: {back.weather(city, province)}', font=("Helvetica", 11))],
                [sg.Text(f'Location: {back.findClosestCity(long, lat)}', font=("Helvetica", 11))],
                [sg.Text(f'Closest Body of Water: {back.findClosestLake(long, lat)}', font=("Helvetica", 11))],
                [sg.Text(f'Type of Water: {back.typeOfWater(long, lat)}', font=("Helvetica", 11))],
                [sg.Button('Water Safety Level'), sg.Button('Species Nearby')] ]

    window = sg.Window('Prokaryote', layout, size=(500,500), element_justification='c')

    #Water Safety
    water = [[sg.Text('Water Safety', font=("Helvetica", 11, "bold"))], [sg.Text(f'Drainage: {back.drainageToLake(long, lat)}')],
             [sg.Text('Natural Hydrology', font=("Helvetica", 11, "bold"))], 
             [sg.Text('In natural ecosystems, bodies of water often have natural drainage patterns, \n' 
                      'and these patterns play a crucial role in maintaining the health of \n'
                      'the ecosystem. High drainage can disrupt these natural patterns and \n' 
                      'may lead to negative consequences such as erosion, habitat loss, \n'
                      'and changes in water quality, which can be detrimental to the ecosystem.')],
             [sg.Text('\n')], [sg.Image('waterquality.png')]]

    #Animal Species
    animal = [[sg.Text('Animal Species')], [sg.Text("-Animal Fact")]]


    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            window.close()
            break
        if event == 'Water Safety Level':
            window.close()
            waterWindow = sg.Window('Water Health', water, size=(500,500), element_justification='c')
            subwindow_handler(waterWindow)
        if event == 'Species Nearby':
            window.close()
            animalWindow = sg.Window('Endangered Species Nearby', animal, size=(500,500), element_justification='c')
            subwindow_handler(animalWindow)
        if event == "Refresh":
            window.close()
            main_menu()
            break

main()
