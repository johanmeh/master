import xarray as xr
import matplotlib.pyplot as plt
import numpy as np
import cartopy.crs as ccrs
import matplotlib.ticker as mticker
from cartopy.mpl.gridliner import LONGITUDE_FORMATTER, LATITUDE_FORMATTER



def fourplot_two_cb(ds5, ds6, ds7, ds8,
                    tl1, tl2, tl3, tl4,
                    vmin1, vmax1, vmin2, vmax2, label):
    proj = ccrs.PlateCarree(central_longitude = 0)
    fig, axs = plt.subplots(2, 2, figsize=(15, 9),
                                           subplot_kw={'projection':proj})
    xticks = [60, 80, 100]
    yticks = [0, 10, 20, 30, 40]
    cm = 'RdBu_r'
    font_size = 12

    #ax1 plot
    im5 = ds5.plot(ax=axs[0,0], cmap=cm, vmin=vmin1, vmax=vmax1, transform=ccrs.PlateCarree(central_longitude=0),
            add_colorbar = False)
    axs[0,0].set_title(tl1)
    cb1 = plt.colorbar(im5,ax=axs[0,:]) #, orientation="horizontal")
    cb1.set_label(label=label, size='large')
    cb1.ax.tick_params(labelsize=font_size)

    # ax3 plot
    ds6.plot(ax=axs[0,1], cmap=cm, vmin=vmin1, vmax=vmax1, transform=ccrs.PlateCarree(central_longitude=0),
            add_colorbar = False)
    axs[0,1].set_title(tl2)


        # ax2 plot
    im7 = ds7.plot(ax=axs[1,0], cmap=cm, vmin=vmin2, vmax=vmax2, transform=ccrs.PlateCarree(central_longitude=0),
            add_colorbar = False)
    axs[1,0].set_title(tl3)
    cb2 = plt.colorbar(im7,ax=axs[1,:])
    cb2.set_label(label='diff hPa', size='large')
    font_size = 12 # Adjust as appropriate.
    cb2.ax.tick_params(labelsize=font_size)

    #ax4 plot
    ds8.plot(ax=axs[1,1], cmap=cm, vmin=vmin2, vmax=vmax2, transform=ccrs.PlateCarree(central_longitude=0),
            add_colorbar = False)
    axs[1,1].set_title(tl4)




    for i in range(0,2):
        for j in range(0,2):
            axs[i,j].coastlines()
            gl  = axs[i,j].gridlines(xlocs=xticks, ylocs=yticks, draw_labels= True, alpha = 0.01, color = 'gray', linestyle = '--')
            gl.xlabels_top = False
            gl.ylabels_right = False
            gl.xlabel_style = {'size': 12}
            gl.ylabel_style = {'size': 12}
            gl.xformatter = LONGITUDE_FORMATTER
            gl.yformatter = LATITUDE_FORMATTER

    return fig


def fourplot_four_cb(ds1, ds2, ds3, ds4,
                        tl1, tl2, tl3, tl4,
                        vmin1,vmax1, vmin2, vmax2,
                        vmin3, vmax3, vmin4, vmax4):

    proj = ccrs.PlateCarree(central_longitude = 0)
    fig, axs = plt.subplots(2, 2, figsize=(15, 9),
                                           subplot_kw={'projection':proj})
    xticks = [60, 80, 100]
    yticks = [0, 10, 20, 30, 40]
    cm = 'RdBu_r'
    font_size = 12


    #ax1 plot
    im1 = ds1.plot.pcolormesh(ax=axs[0,0], cmap=cm, vmin=vmin1, vmax=vmax1, transform=ccrs.PlateCarree(central_longitude=0),
            add_colorbar=False)
    cb1 = plt.colorbar(im1,ax=axs[0,0]) #, orientation="horizontal")
    cb1.set_label(label='Temp diff [K]', fontsize=12)
    cb1.ax.tick_params(labelsize=font_size)
    axs[0,0].set_title(tl1)
    # ax3 plot
    im2 = ds2.plot.pcolormesh(ax=axs[0,1], cmap=cm, vmin=vmin2, vmax=vmax2, transform=ccrs.PlateCarree(central_longitude=0),
            add_colorbar=False)
    cb2 = plt.colorbar(im2, ax=axs[0,1])
    cb2.set_label(label='Temp diff [K]', fontsize=12)
    cb2.ax.tick_params(labelsize=font_size)

    axs[0,1].set_title(tl2)

    im3 = ds3.plot.pcolormesh(ax=axs[1,0], cmap=cm, vmin=vmin3, vmax=vmax3, transform=ccrs.PlateCarree(central_longitude=0),
            add_colorbar=False)
    cb3  = plt.colorbar(im3, ax=axs[1,0])
    cb3.set_label(label='Pressure diff [hPa]', fontsize=12)
    cb3.ax.tick_params(labelsize=font_size)
    axs[1,0].set_title(tl3)

    #ax4 plot
    im4 = ds4.plot.pcolormesh(ax=axs[1,1], cmap=cm, vmin=vmin4, vmax=vmax4, transform=ccrs.PlateCarree(central_longitude=0),
            add_colorbar=False)
    cb4 = plt.colorbar(im4, ax=axs[1,1])
    cb4.set_label(label = 'Pressure diff [hPa]', fontsize=12)
    cb4.ax.tick_params(labelsize=font_size)
    axs[1,1].set_title(tl4)

    for i in range(0,2):
        for j in range(0,2):
            axs[i,j].coastlines()
            gl  = axs[i,j].gridlines(xlocs=xticks, ylocs=yticks, draw_labels= True, alpha = 0.01, color = 'gray', linestyle = '--')
            gl.xlabels_top = False
            gl.ylabels_right = False
            gl.xlabel_style = {'size': 12}
            gl.ylabel_style = {'size': 12}
            gl.xformatter = LONGITUDE_FORMATTER
            gl.yformatter = LATITUDE_FORMATTER

    plt.subplots_adjust(hspace=0.3)

    return fig
