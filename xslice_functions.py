import os

import matplotlib as mpl
import matplotlib.colors as colors
import matplotlib.pyplot as plt
import netCDF4 as nC
import numpy as np
from pathlib import Path

os.environ["PROJ_LIB"] = "C:\\Utilities\\Python\\Anaconda\\Library\\share"
from mpl_toolkits.basemap import Basemap

months = [
    "Jan",
    "Feb",
    "Mar",
    "Apr",
    "May",
    "Jun",
    "Jul",
    "Aug",
    "Sep",
    "Oct",
    "Nov",
    "Dec",
]
norm = colors.TwoSlopeNorm(vcenter=0.00)

subfolder = Path("images")
subfolder.mkdir(exist_ok=True)

# Create a dictionary for drawing lines on Basemap
def draw_countries(m):
    m.drawcountries()


def draw_rivers(m):
    m.drawrivers()


def draw_states(m):
    m.drawstates()


aesthetics = {"Countries": draw_countries, "Rivers": draw_rivers, "States": draw_states}


# Separating Hovmoller into Seasons
# def seasonal_cols(Year, Month):
#     all_col = np.zeros((3 * (Year[1] - Year[0]) - 2))
#     season = int(Month % 12 / 3)
#     if season == 0:  # winter
#         col = [0, 1, 11]
#     elif season == 1:  # spring
#         col = [2, 3, 4]
#     elif season == 2:  # summer
#         col = [5, 6, 7]
#     else:  # fall
#         col = [8, 9, 10]
#     for i in range(0, all_col.size):
#         if i % 3 == 0:
#             all_col[i] = col[0] + int(i / 3) * 12
#         elif i % 3 == 1:
#             all_col[i] = col[1] + int(i / 3) * 12
#         else:
#             all_col[i] = col[2] + int(i / 3) * 12
#     if Month % 3 == 1:
#         all_col = all_col[1:]
#     if Month % 3 == 2:
#         all_col = all_col[2:]
#     return all_col.astype(int)


# homvoller graph
# def hov(cs, interval, variables, year, month, depth, lat, lon, clrs, font_dic, align):
#     file = nC.Dataset("godas_" + variables + ".nc")
#     time = np.linspace(year[0], year[1], (year[1] - year[0]) * 12 + 1)
#     if interval == "Annual":
#         time = time[::12]
#
#     if cs == "latitudinal":
#         zz = file.variables[variables][
#              (year[0] - 1980) * 12: (year[1] - 1980) * 12 + month,
#              depth[0],
#              lat[0]: lat[-1] + 1,
#              lon[0],
#              ]
#         x = file.variables["lat"][lat[0]: lat[-1] + 1]
#         plt.xlabel("Latitude", size=10)
#     elif cs == "longitudinal":
#         zz = file.variables[variables][
#              (year[0] - 1980) * 12: (year[1] - 1980) * 12 + month,
#              depth[0],
#              lat[0],
#              lon[0]: lon[-1] + 1,
#              ]
#         x = file.variables["lon"][lon[0]: lon[-1] + 1]
#         plt.xlabel("Longitude", size=10)
#     else:
#         x = file.variables["level"][depth[0]: depth[-1] + 1]
#         zz = file.variables[variables][
#              (year[0] - 1980) * 12: (year[1] - 1980) * 12 + month,
#              depth[0]: depth[-1] + 1,
#              lat[0],
#              lon[0],
#              ]
#         plt.xlabel("Depth [m]")
#
#     if interval == "Seasonal":
#         cols = seasonal_cols(year, month)
#         time = time[cols]
#         zz = zz[cols, :]
#     else:
#         zz = zz[month - 1:, :]
#         if interval == "Annual":
#             zz = zz[::12, :]
#     xx, tt = np.meshgrid(x, time)
#     if variables in ["ucur", "vcur"]:
#         plt.contourf(xx, tt, zz, norm=norm, levels=100, cmap=clrs)
#     else:
#         plt.contourf(xx, tt, zz, levels=100, cmap=clrs)
#     plt.colorbar()
#     plt.ylabel("Year", size=10)
#     title = hov_title(cs, variables, interval, month, depth, lat, lon)
#     plt.title(title, font=font_dic, loc=align)
#
#
# def hov_title(cs, variables, interval, month, depth, lat, lon):
#     file = nC.Dataset("godas_" + variables + ".nc")
#     if cs == "latitudinal":
#         u, v = file.variables["level"][:], file.variables["lon"][:]
#         title = (
#                 variables + " at " + str(u[depth[0]]) + "m and Longitude " + str(v[lon[0]])
#         )
#     elif cs == "longitudinal":
#         u, v = file.variables["level"][:], file.variables["lat"][:]
#         title = (
#                 variables + " at " + str(u[depth[0]]) + "m and Latitude " + str(v[lat[0]])
#         )
#     else:
#         u, v = file.variables["lat"][:], file.variables["lon"][:]
#         title = (
#                 variables
#                 + " at Latitude "
#                 + str(u[lat[0]])
#                 + " and Longitude "
#                 + str(v[lon[0]])
#         )
#     if interval == "Annual":
#         title = months[month - 1] + " " + title
#     elif interval == "Seasonal":
#         season = int(month % 12 / 3)
#         if season == 0:
#             title = "Winter " + title
#         elif season == 1:
#             title = "Spring " + title
#         elif season == 2:
#             title = "Summer " + title
#         else:
#             title = "Fall " + title
#     return title
#

def f(
        #hovmoller,
        #interval,
        cross_section,
        variables,
        yr,
        month,
        depth,
        lat,
        lon,
        clrs,
        file_format,
        dark,
        features,
        hatches,
        text_size,
        font,
        align,
):
    font_dic = {
        "family": font,
        "weight": "normal",
        "size": text_size,
    }
    if dark:
        plt.style.use("dark_background")
    else:
        mpl.rcParams.update(mpl.rcParamsDefault)
    # if hovmoller:
    #     hov(
    #         cross_section,
    #         interval,
    #         variables,
    #         yr,
    #         month,
    #         depth,
    #         lat,
    #         lon,
    #         clrs,
    #         font,
    #         align,
    #     )
    #     title = hov_title(cross_section, variables, interval, month, depth, lat, lon)
    #else:
    file = nC.Dataset(f'https://downloads.psl.noaa.gov/Datasets/godas/{variables}.{yr}.nc#mode=bytes')
    data = file.variables[variables][month - 1]
    if variables == "salt":
        data = data*1000
    lons = file.variables["lon"][:]
    lats = file.variables["lat"][:]
    depths = file.variables["level"][:]
    new_hatch = []
    for c in hatches:
        for i in range(0, 20):
            new_hatch.append(c)
    if cross_section == "latitudinal":
        fig = plt.figure(figsize=(20, 8))
        xx, yy = np.meshgrid(
            lons[lon[0]: lon[-1]], 0 - depths[depth[0]: depth[-1]]
        )
        zz = data[depth[0]: depth[-1], lat[0], lon[0]: lon[-1]]
        if variables in ["ucur", "vcur"]:
            plt.contourf(
                    xx, yy, zz, norm=norm, cmap=clrs, hatches=new_hatch, levels=100
            )
        else:
            plt.contourf(xx, yy, zz, levels=100, hatches=new_hatch, cmap=clrs)

        title = (
                    months[month - 1]
                    + " "
                    + str(yr)
                    + " "
                    + variables
                    + " at Latitude "
                    + str(lats[lat[0]])
        )
        plt.title(title + r"$^\circ$", font=font_dic, loc=align)
        plt.xlabel("Longitude", size=20)
        plt.ylabel("depth [m]", size=20)
        cb = plt.colorbar()
        cb.ax.tick_params(labelsize=20)

    elif cross_section == "longitudinal":
        fig = plt.figure(figsize=(12, 8))
        xx, yy = np.meshgrid(
            lats[lat[0]: lat[-1]], 0 - depths[depth[0]: depth[-1]]
        )
        zz = data[depth[0]: depth[-1], lat[0]: lat[-1], lon[0]]
        if variables in ["ucur", "vcur"]:
            plt.contourf(
                    xx, yy, zz, levels=100, norm=norm, hatches=new_hatch, cmap=clrs
            )
        else:

            plt.contourf(xx, yy, zz, levels=100, hatches=new_hatch, cmap=clrs)
        title = (
                    months[month - 1]
                    + " "
                    + str(yr)
                    + " "
                    + variables
                    + " at Longitude "
                    + str(lons[lon[0]])
        )
        plt.title(title + r"$^\circ$", font=font_dic, loc=align)
        plt.xlabel("Latitude", size=20)
        plt.ylabel("depth [m]", size=20)
        cb = plt.colorbar(
            format=mpl.ticker.ScalarFormatter(useMathText=True)
        )
        cb.ax.tick_params(labelsize=20)

    else:
        xx, yy = np.meshgrid(lons[lon[0]: lon[-1]], lats[lat[0]: lat[-1]])
        ig = plt.figure(figsize=(20, 8))
        m = Basemap(
                projection="cyl",
                lat_ts=10,
                llcrnrlon=lons[lon[0]],
                urcrnrlon=lons[lon[-1]],
                llcrnrlat=lats[lat[0]],
                urcrnrlat=lats[lat[-1]],
        )
        zz = data[depth[0], lat[0]: lat[-1], lon[0]: lon[-1]]
        if variables in ["ucur", "vcur"]:
            m.pcolormesh(xx, yy, zz, shading="auto", norm=norm, cmap=clrs)
        else:
            m.pcolormesh(xx, yy, zz, shading="auto", cmap=clrs)
        cb = m.colorbar(location="right")
        cb.ax.tick_params(labelsize=20)
        cb.formatter.set_powerlimits((-7, 3))
        for feature in features:
            aesthetics[feature](m)
        m.drawcoastlines()
        m.drawmapboundary()
        m.drawparallels(np.arange(-90, 90, 30), labels=[1, 0, 0, 0], size=20)
        m.drawmeridians(np.arange(-180, 180, 60), labels=[0, 0, 0, 1], size=20)
        title = (
                months[month - 1]
                    + " "
                    + str(yr)
                    + " "
                    + variables
                    + " at "
                    + str(depths[depth[0]])
                    + "m."
            )
        plt.title(title, font=font_dic, loc=align)
    plt.xticks(size=20)
    plt.yticks(size=20)

    if file_format != "NONE":
        plt.savefig("images/" + title + file_format)
    plt.show()
