"""
Lei updated on Feb 8, 2020;
Used to find the corresponding demand/solar/wind input data given year and region name; 
Also re-calculate the total days of that year.
"""


from Preprocess_Input import read_csv_dated_data_file
import numpy as np, sys
import datetime

from scipy import signal
def highpass_filter(var, approach, highpass):
    fs = 1
    if approach == 'butter':
        npt = 10
        cutoff_period = highpass
        cutoff_freque = (1/cutoff_period) / (fs/2)
        z, p, k = signal.butter(npt, cutoff_freque, 'highpass', output="zpk")
        smoothed0 = signal.zpk2sos(z, p, k)
        output_highpass = signal.sosfiltfilt(smoothed0, var)
    if approach == 'fft':
        length = len(var)
        cutoff_period = highpass
        cutoff_freque = (1/cutoff_period)
        input_fft = np.fft.fft(var)
        input_fre = np.fft.fftfreq(length)
        input_fft[np.abs(input_fre)<=cutoff_freque] = 0.
        output_highpass = np.fft.ifft(input_fft).real      
    return output_highpass
def lowpass_filter(var, approach, lowpass):
    fs = 1
    if approach == 'butter':
        npt = 10
        cutoff_period = lowpass
        cutoff_freque = (1/cutoff_period) / (fs/2)
        z, p, k = signal.butter(npt, cutoff_freque, 'lowpass', output="zpk")
        smoothed0 = signal.zpk2sos(z, p, k)
        output_lowpass = signal.sosfiltfilt(smoothed0, var)
    if approach == 'fft':
        length = len(var)
        cutoff_period = lowpass
        cutoff_freque = (1/cutoff_period)
        input_fft = np.fft.fft(var)
        input_fre = np.fft.fftfreq(length)
        input_fft[np.abs(input_fre)>=cutoff_freque] = 0.
        output_lowpass = np.fft.ifft(input_fft).real      
    return output_lowpass




def update_series(case_dic, tech_dic, delta_t=-1):
    series = read_csv_dated_data_file(case_dic['year_start'], case_dic['month_start'], case_dic['day_start'], case_dic['hour_start'],
                                      case_dic['year_end'],   case_dic['month_end'],   case_dic['day_end'],   case_dic['hour_end'],
                                      case_dic['data_path'],  tech_dic['series_file'])
    # Remove Feb 29 if exists
    if len(series) != 8760:
        print (len(series))
        series = np.r_[series[:1416], series[1440:]]
        if len(series) != 8760:
            print ('error removing Feb 29')
            sys.exit()
    
    # if delta_t != -1:
    #     if delta_t != -2:
    #         mean_series = np.average(series)
    #         series = lowpass_filter(series, 'fft', delta_t)
    #         # if np.average(series) < 1:
    #         #     series = series + mean_series
    #     elif delta_t == -2:
    #         series = np.ones(8760) * np.mean(series)

    # Normalization the demand curve
    if 'normalization' in tech_dic:
        if tech_dic['normalization'] >= 0.0:
            series = series * tech_dic['normalization']/np.average(series)

    tech_dic['series'] = series
    mean_series = np.mean(series)
    return mean_series

def update_timenum(case_dic):
    num_time_periods = (24 * (
            datetime.date(case_dic['year_end'],case_dic['month_end'],case_dic['day_end']) - 
            datetime.date(case_dic['year_start'],case_dic['month_start'],case_dic['day_start'])
            ).days +
            (case_dic['hour_end'] - case_dic['hour_start'] ) + 1)
    return num_time_periods


