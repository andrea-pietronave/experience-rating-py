import PySimpleGUI as sg
import functions
import constants


functions.createConfig()
config = functions.getConfig()
theme = config["THEME"]["themename"]
sg.theme(theme)

search_column = [
    [
        sg.In(size=(25, 1), enable_events=True,
              key="-SEARCH_BAR-", focus=True, ),
        sg.Submit(size=(10, 1), key="-SEARCH-", button_text="Search")
    ],
    [
        sg.Listbox(
            values=[], enable_events=True, size=(36, 10), key="-ITEM_LIST-", expand_x=True, expand_y=True, )
    ],
    [
        sg.In(size=(25, 1), enable_events=True,
              key="-EXCEL_INPUT-"),
        sg.FileBrowse(file_types=(("Excel Files", "*.xlsx"),)),
    ]
]

poster_column = [
    [
        sg.Image(filename="", key="-POSTER-", expand_x=True, expand_y=True)
    ],
]

item_column = [
    [
        sg.Text(size=(6, 1),
                text="Name:",),
        sg.Text(size=(30, 1),
                key="-ITEM_NAME-",),

    ],
    [
        sg.Text(size=(6, 1),
                text="Date:",),
        sg.Text(size=(30, 1),
                key="-ITEM_DATE-",),

    ],
    [
        sg.Text(size=(6, 1),
                text="Genre:",),
        sg.Text(size=(30, 1),
                key="-ITEM_GENRE-",),

    ],
    [
        sg.Text(size=(6, 1),
                text="Overview:",),
        sg.Multiline(size=(30, 10), disabled=True,
                     key="-ITEM_OVERVIEW-",  expand_x=True, expand_y=True),

    ],
    [
        sg.Spin(values=constants.VOTE_VALUES,
                enable_events=True, key="-VOTE-", size=(5, 1)),
        sg.Submit(size=(10, 1), key="-ADD_MOVIE-", button_text="Add movie"),
        sg.Text(size=(15, 1), key="-ERROR-", font=('Courier', 10),)

    ],
    [
        sg.ProgressBar(100, key="-PROGRESS_BAR-",
                       bar_color=("green", "white"), border_width=1, expand_x=True, size=(0, 15))
    ]

]

tools_info_column = [
    [
        sg.Button(key="-CLEAN_DUPLICATES", button_text="Clean duplicates"),
        sg.Multiline(size=(50, 10), disabled=True,
                     key="-INFO_TOOLS-"),
    ],
]

options_column = [
    [
        sg.Text(size=(10, 1),
                text="Theme:",),
        sg.Combo(auto_size_text=True, readonly=True, default_value=theme,
                 key="-INFO_THEMES-", values=sorted(constants.THEMES_LIST)),

        sg.Button(key="-CHANGE_THEME-",
                  button_text="Change theme(requires restart)"),



    ],
    [
        sg.Text(size=(10, 1),
                text="Movie sheet:",),
        sg.In(size=(25, 1), enable_events=True,
              key="-MOVIE_SHEET-", focus=True, ),

        sg.Submit(size=(10, 1), key="-CHANGE_MOVIE_SHEET-",
                  button_text="Change")
    ]
]
