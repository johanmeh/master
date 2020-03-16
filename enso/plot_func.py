"""
Make function to plot three maps based on xarray and cartopy,
projection = Plate Carree

"""
import matplotlib.pyplot as plt
import xarray as xr
import numpy as np
import cartopy.crs as ccrs

def three_plot_contour(ds1, ds2, ct2, ds3, ct3, tl1, tl2, tl3, vmin, vmax, cm=None):
    proj = ccrs.PlateCarree(central_longitude = 0)
    f, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(20, 10), subplot_kw={'projection':proj})
    xticks = [-180,-120, -60, 0, 60, 120, 180]
    yticks = [-20, -10, 0, 10, 20]

    if cm == None:
        cm = 'coolwarm'
    else:
        cm = cm

    #ax1 = always observations
    ds1.plot(ax=ax1, cmap=cm)
    #ct1.plot.contour(ax=ax1)
    ax1.coastlines()
    gl = ax1.gridlines(xlocs=xticks, ylocs=yticks, draw_labels=True, alpha=0.2, color='gray', linestyle='--')
    gl.xlabels_top=False
    gl.ylabels_right=False
    ax1.set_title(tl1, fontsize = 16)
    gl.xlabel_style = {'size':12}
    gl.ylabel_style = {'size':12}

    # ax2 = always era5 - observations
    ds2.plot(ax=ax2, vmin=vmin, vmax=vmax, cmap=cm)
    ctl = ct2.plot.contour(ax=ax2,levels=4,colors='w')
    ax2.clabel(ctl, fontsize=18)

    ax2.coastlines()
    gl  = ax2.gridlines(xlocs=xticks, ylocs=yticks, draw_labels= True, alpha = 0.2, color = 'gray', linestyle = '--')
    gl.xlabels_top = False
    gl.ylabels_right = False
    gl.xlabel_style = {'size': 12}
    gl.ylabel_style = {'size': 12}
    ax2.set_title(tl2, fontsize = 18)


    #ax3 = always erai - observations
    ds3.plot(ax=ax3, vmin=vmin, vmax=vmax, cmap=cm)
    ctl2 = ct3.plot.contour(ax=ax3,levels=8, colors='w')
    ax3.clabel(ctl2, fontsize=18)
    ax3.coastlines()
    gl = ax3.gridlines(xlocs=xticks, ylocs=yticks, draw_labels= True, alpha = 0.2, color = 'gray', linestyle = '--')
    gl.xlabels_top = False
    gl.ylabels_right = False
    gl.xlabel_style = {'size': 12}
    gl.ylabel_style = {'size': 12}
    ax3.set_title(tl3, fontsize=18)

    return f


def three_plot(ds1, ds2, ds3, tl1, tl2, tl3, vmin2, vmax2, cm=None, enso = False):
    proj = ccrs.PlateCarree(central_longitude = 180)
    f, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(20, 10), subplot_kw={'projection':proj})
    xticks = [-120, -60, 0, 60, 120, 180]
    yticks = [-20, -10, 0, 10, 20]

    if cm == None:
        cm = 'RdBu_r'
    else:
        cm = cm

    #ax1 = always observations
    if enso == True:
        ds1.plot(ax=ax1, cmap=cm, transform=ccrs.PlateCarree(central_longitude=0))
    else:
        ds1.plot(ax=ax1, cmap=cm, transform=ccrs.PlateCarree(central_longitude=0),vmin=vmin2, vmax=vmax2)
    ax1.coastlines()
    gl = ax1.gridlines(xlocs=xticks, ylocs=yticks, draw_labels=True, alpha=0.2, color='gray', linestyle='--')
    gl.xlabels_top=False
    gl.ylabels_right=False
    ax1.set_title(tl1, fontsize = 16)
    gl.xlabel_style = {'size':12}
    gl.ylabel_style = {'size':12}

    # ax2 = always era5 - observations
    if enso == True:
        ds2.plot(ax=ax2, cmap=cm, transform=ccrs.PlateCarree(central_longitude=0))
    else:
        ds2.plot(ax=ax2, cmap=cm, transform=ccrs.PlateCarree(central_longitude=0), vmin=vmin2, vmax=vmax2)

    ax2.coastlines()
    gl  = ax2.gridlines(xlocs=xticks, ylocs=yticks, draw_labels= True, alpha = 0.2, color = 'gray', linestyle = '--')
    gl.xlabels_top = False
    gl.ylabels_right = False
    gl.xlabel_style = {'size': 12}
    gl.ylabel_style = {'size': 12}
    ax2.set_title(tl2, fontsize = 16)


    #ax3 = always erai - observations
    ds3.plot(ax=ax3, vmin=vmin2, vmax=vmax2, cmap=cm, transform=ccrs.PlateCarree(central_longitude=0))
    ax3.coastlines()
    gl = ax3.gridlines(xlocs=xticks, ylocs=yticks, draw_labels= True, alpha = 0.2, color = 'gray', linestyle = '--')
    gl.xlabels_top = False
    gl.ylabels_right = False
    gl.xlabel_style = {'size': 12}
    gl.ylabel_style = {'size': 12}
    ax3.set_title(tl3, fontsize=16)

    plt.tight_layout()
    plt.subplots_adjust(hspace=0.5)

    return f

def enso_maxmin(ds1, tl1, ds2, tl2, vmin, vmax):
    proj = ccrs.PlateCarree(central_longitude = 180)
    f, (ax1, ax2) = plt.subplots(2, 1, figsize=(20, 10), subplot_kw={'projection':proj})
    xticks = [-120, -60, 0, 60, 120, 180]
    yticks = [-20, -10, 0, 10, 20]
    cm = 'RdBu_r'

    #ax1 plot
    ds1.plot(ax=ax1, cmap=cm,vmin=vmin, vmax=vmax, transform=ccrs.PlateCarree(central_longitude=0))
    ax1.coastlines()
    gl = ax1.gridlines(xlocs=xticks, ylocs=yticks, draw_labels=True, alpha=0.2, color='gray', linestyle='--')
    gl.xlabels_top=False
    gl.ylabels_right=False
    ax1.set_title(tl1, fontsize = 16)
    gl.xlabel_style = {'size':12}
    gl.ylabel_style = {'size':12}

    ds2.plot(ax=ax2, cmap=cm, vmin = vmin, vmax=vmax, transform=ccrs.PlateCarree(central_longitude=0))
    ax2.coastlines()
    gl  = ax2.gridlines(xlocs=xticks, ylocs=yticks, draw_labels= True, alpha = 0.2, color = 'gray', linestyle = '--')
    gl.xlabels_top = False
    gl.ylabels_right = False
    gl.xlabel_style = {'size': 12}
    gl.ylabel_style = {'size': 12}
    ax2.set_title(tl2, fontsize = 16)

    return f
