import ipywidgets as widgets
import numpy as np
#LOGO
file = open("XSLICE LOGO.PNG", "rb")
image = file.read()
logo = widgets.Image(
    value=image,
    format='png',
    width=1500,
    height=400,
)
# WIDGETS
# Tab 1
# Variable Selection Widget
variable_butt = widgets.Select(
    options=["pottmp", "salt", "ucur", "vcur"], description="variables:", disabled=False
)
# Mean maker widget
mean_butt = widgets.Select(
    options=["None", "Mean Subtracted", "Standardized Anomalies"],
    description="Alter: ",
    disabled=False,
)
# Tab 2
# Cross Section Widget
cs_toggle = widgets.ToggleButtons(
    options=["depth", "longitudinal", "latitudinal"],
    description="Cut: ",
    disabled=False,
    button_style="",
    icon=["bed"],
)
# Selection Slider range
levels = widgets.SelectionRangeSlider(
    options=np.arange(0, 40),
    index=(0, 39),
    description="depth",
    disabled=False,
    continuous_update=False,
)
lat_w = widgets.SelectionRangeSlider(
    options=np.arange(0, 418),
    index=(0, 417),
    description=" Latitude ",
    disabled=False,
    continuous_update=False,
)
lon_w = widgets.SelectionRangeSlider(
    options=np.arange(0, 360),
    index=(0, 359),
    description=" Longitude ",
    disabled=False,
    continuous_update=False,
)
# Time Widgets
year_w = widgets.IntSlider(
    value=1980,
    min=1980,
    max=2022,
    description="Year: ",
    disabled=False,
    continuous_update=False
)
month_w = widgets.IntSlider(
    value=1,
    min=1,
    max=12,
    description="Month: ",
    disabled=False,
    continuous_update=False,
    orientation="horizontal",
    readout=True,
)
# HOVMOLLER WIDGETS
# hovmoller = widgets.ToggleButton(
#     value=False,
#     description="Hovmoller",
#     disabled=False,
#     button_style="",  # 'success', 'info', 'warning', 'danger' or ''
#     tooltip="Description",
#     icon="hourglass",  # (FontAwesome names without the `fa-` prefix)
# )
# hov_interval = widgets.Dropdown(
#     options=["Monthly", "Seasonal", "Annual"],
#     value="Monthly",
#     description="Cycle:",
#     disabled=False,
# )

# Aesthetics Widgets
# Color Widgets
# Dark Mode
dark_mode = widgets.ToggleButton(
    value=False,
    description="Dark Mode",
    disabled=False,
    button_style="",  # 'success', 'info', 'warning', 'danger' or ''
    tooltip="Description",
    icon="bed",  # (FontAwesome names without the `fa-` prefix)
)
# CMAP
color_drop = widgets.Dropdown(
    options=[
        "jet",
        "Greys",
        "seismic",
        "rainbow",
        "twilight_shifted",
        "viridis",
        "hot_r",
    ],
    value="jet",
    description="Colorscale:",
    disabled=False,
)
# Hatch marks
hatch_w = widgets.Dropdown(
    options=[" ", "./-\\*"],
    value=" ",
    description="Hatches:",
    disabled=False,
)
file_format = widgets.Dropdown(
    options=["NONE", ".png", ".pdf", ".jpg"],
    value="NONE",
    description="SAVE AS:",
    disabled=False,
)
# Text Widgets
# Changing Font Sizes
text_size = widgets.BoundedFloatText(
    value=20, min=0, max=50, step=0.5, description="Font Size:", disabled=False
)
# Changing Fonts
# fonts = widgets.Dropdown(
#     options=[
#         "Arial",
#         "Bookman Old Style",
#         "Broadway",
#         "Brush Script M7",
#         "Century",
#         "Century Gothic",
#         "Comic Sans",
#         "Courier New",
#         "Elephant",
#         "Franklin Gothic Heavy",
#         "Garamond",
#         "Georgia",
#         "Impact",
#         "Ink Free",
#         "Magneto",
#         "Old English Text MT",
#         "Papyrus",
#         "Sans Serif",
#         "Stencil",
#         "Times New Roman",
#         "Vivaldi",
#     ],
#     value="Courier New",
#     description="Fonts:",
#     disabled=False,
# )
# Alignment
align = widgets.Dropdown(
    options=[
        "left",
        "center",
        "right",
    ],
    value="center",
    description="Align:",
    disabled=False,
)
# Put display features here
features = widgets.SelectMultiple(
    options=["Countries", "Rivers", "States"], description="Features", disabled=False
)


def ui():
    tabs = widgets.Tab()
    tab1 = variable_butt#widgets.HBox([variable_butt, mean_butt])

    # Second tab is the main interface for operations

    # Separate Accordion for Hovmoller which will be used less
    #tab2_accord1 = widgets.HBox([hovmoller, hov_interval])
    t2a2r1 = cs_toggle  # tab 2, accordion 2, row 1
    t2a2r2 = widgets.HTML(  # Some HTML to make it prettier
        value="<h4><b><center>TIME</center></b></h4>",
        placeholder="",
        description="",
    )
    t2a2r3 = widgets.HBox([month_w, year_w])  # Tab 2 accordion 2, row 3
    t2a2r4 = widgets.HTML(  # Some HTML to make it prettier
        value="<h4><b><center>AXES</center></b></h4>",
        placeholder="",
        description="",
    )
    t2a2r5 = widgets.HBox([levels, lat_w, lon_w])  # Tab 2, accordion 2, row 5
    tab2_accord2 = widgets.VBox(
        [t2a2r1, t2a2r2, t2a2r3, t2a2r4, t2a2r5]
    )  # Combining into 1 accordion
    # Combining accordions to make the tab
    tab2 = tab2_accord2 # widgets.Accordion(children=[tab2_accord1, tab2_accord2], selected_index=1)
    # adding names
    # accordion_titles = ["Hovmoller", "Cross Section"]
    # [tab2.set_title(i, title) for i, title in enumerate(accordion_titles)]
    # Final Tab
    color_accord = widgets.HBox([dark_mode, color_drop, hatch_w])
    text_accord = widgets.HBox([text_size, align])#fonts,
    t3_accord = widgets.Accordion(children=[color_accord, text_accord])
    accordion_titles = ["Color", "Text"]
    [t3_accord.set_title(i, title) for i, title in enumerate(accordion_titles)]
    t3r3 = widgets.HBox([features, file_format])
    tab3 = widgets.VBox([t3_accord, t3r3])
    # Putting it all together
    tabs.children = [tab1, tab2, tab3]
    tab_titles = ["Data", "Main", "Display and Export"]
    [tabs.set_title(i, title) for i, title in enumerate(tab_titles)]
    ui = widgets.VBox([logo, tabs])
    return ui
