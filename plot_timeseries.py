"""
Funksjon som plotter tidsserie av forskjell mellom rean-gpsro,
gi latitudegrenser for forskjellig plot

"""
import matplotlib.pyplot as plt
import xarray as xr
import pandas as pd
import numpy as np


def time_series_plot(ds1, ds2,obs, latmin, latmax, tl1, tl2):

    diff1_cpt = ds1.ctpt.sel(lat=slice(latmin, latmax)).mean(axis=(1,2)) \
    - obs.CP_T.sel(lat=slice(latmin, latmax)).mean(axis=(1,2))

    diff2_lrt = ds1.tpt.sel(lat=slice(latmin, latmax)).mean(axis=(1,2)) \
    - obs.LR_T.sel(lat=slice(latmin, latmax)).mean(axis=(1,2))

    diff3_cpt = ds2.ctpt.sel(lat=slice(latmin, latmax)).mean(axis=(1,2)) \
    - obs.CP_T.sel(lat=slice(latmin, latmax)).mean(axis=(1,2))

    diff4_lrt = ds2.tpt.sel(lat=slice(latmin, latmax)).mean(axis=(1,2)) \
    - obs.LR_T.sel(lat=slice(latmin, latmax)).mean(axis=(1,2))

    fig, axs = plt.subplots(2,1, figsize=(16,12))

    diff1_cpt.plot(ax=axs[0], label = 'ERA5 CPT', lw=2.5)
    diff1_cpt.rolling(time=10, center=True).mean().plot(ax=axs[0],
            label = 'CPT rolling mean', lw=2.5)

    diff2_lrt.plot(ax=axs[0], label = 'ERA5 LRT', lw=2.5)
    diff2_lrt.rolling(time=10, center=True).mean().plot(ax=axs[0],
            label = 'LRT rolling mean', lw=2.5)

    diff3_cpt.plot(ax=axs[1], label = 'ERA-Interim CPT', lw=2.5)
    diff3_cpt.rolling(time=10, center=True).mean().plot(ax=axs[1],
            label='CPT rolling mean', lw=2.5)

    diff4_lrt.plot(ax=axs[1], label = 'ERA-Interim LRT', lw=2.5)
    diff4_lrt.rolling(time=10, center=True).mean().plot(ax=axs[1],
            label='LRT rolling mean', lw=2.5)

    axs[0].set_title(tl1,fontsize=14)
    axs[1].set_title(tl2,fontsize=14)

    for ax in axs:
        ax.legend(ncol = 2, fontsize=12)
        ax.grid()
        ax.set_ylabel('Temperature difference', fontsize=14)
        ax.set_xlabel('Time', fontsize=14)

    plt.tight_layout()
    return fig
