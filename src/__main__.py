import os
import sys
import api
import constants
import functions
import excel_functions
import modules
import PySimpleGUI as sg

# TODO Check for bugs


def main():

    main_elements = [
        [
            sg.Frame("Search", modules.search_column, expand_x=True, expand_y=True,
                     ),
            sg.Frame("Poster", modules.poster_column, expand_x=True, expand_y=True,
                     ),
            sg.Frame("Info", modules.item_column,
                     expand_x=True, expand_y=True,)

        ]
    ]

    tools_elements = [
        [
            sg.Column(modules.tools_info_column)
        ]
    ]

    otpions_elements = [
        [
            sg.Column(modules.options_column)
        ]
    ]

    main_tab = [
        [
            sg.Tab("Main", main_elements),
            sg.Tab("Tools", tools_elements),
            sg.Tab("Options", otpions_elements)
        ]
    ]

    layout = [
        [
            sg.TabGroup(main_tab, "top", title_color=(
                "black"), expand_x=True, expand_y=True, )
        ]
    ]

    window = sg.Window("Experience Rating", layout, resizable=True,)

    resultNumber = constants.DEAFULT_RESULT_NUMBER

    elements = None
    genre_list = None
    info = {
        "name": "",
        "release_date": "",
        "genre": "",
        "vote": "",

    }

    while (True):

        event, values = window.read()

        if event == "Exit" or event == sg.WIN_CLOSED:
            break

        if event == "-SEARCH-":
            if not values["-SEARCH_BAR-"] or values["-SEARCH_BAR-"].isspace():
                print("Empty search string")
            else:
                movieRequest = api.api_req(
                    constants.MOVIE_URL, values["-SEARCH_BAR-"])
                elements = api.get_list(
                    movieRequest, resultNumber, "movie", window)

                window["-ITEM_LIST-"].update(elements["title"])

        if event == "-ITEM_LIST-":

            try:
                window["-ERROR-"].update("", text_color="black")
                index = elements["title"].index(window["-ITEM_LIST-"].get()[0])
                window["-ITEM_NAME-"].update(elements["title"][index])
                window["-ITEM_DATE-"].update(elements["release_date"][index])

                #! TODO MAXIMUM 2
                i = 0
                for x in elements["genres"][index]:
                    if not genre_list:
                        genre_list = x
                    elif i < 1:
                        genre_list += "/" + x
                        i += 1

                window["-ITEM_GENRE-"].update(genre_list)
                window["-ITEM_OVERVIEW-"].update(elements["overview"][index])
                window["-POSTER-"].update(data=elements["poster"][index])
                genre_list = None
            except Exception as e:
                print("Error:", e)

        if event == "-ADD_MOVIE-":

            window["-ERROR-"].update("Adding...", text_color="black")
            filename = window["-EXCEL_INPUT-"].get()
            info["name"] = window["-ITEM_NAME-"].DisplayText
            info["release_date"] = window["-ITEM_DATE-"].DisplayText
            info["genre"] = window["-ITEM_GENRE-"].DisplayText
            info["vote"] = values["-VOTE-"]
            try:
                excel_functions.add_movie(info, filename)
                window["-ERROR-"].update("Success!", text_color="green")
            except:
                window["-ERROR-"].update("Error!", text_color="red")

        if event == "-CLEAN_DUPLICATES-":
            try:
                filename = window["-EXCEL_INPUT-"].get()
                excel_functions.remove_duplicate(filename)
            except Exception as e:
                print("Error:", e)

        if event == "-CHANGE_THEME-":
            functions.changeTheme(values["-INFO_THEMES-"])
            os.execv(sys.executable, ['python'] + sys.argv)

        if event == "-CHANGE_MOVIE_SHEET-":
            functions.changeTheme(values["-INFO_THEMES-"])
            os.execv(sys.executable, ['python'] + sys.argv)


#! Testing purposes
main()
