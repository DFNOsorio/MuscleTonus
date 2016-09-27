import h5py
import numpy as np
import copy

def load_data_h5(filename):
    f = h5py.File(filename + '.h5','r')

    EMG_Macs = f.keys()[0]

    EMG_data_group = f[EMG_Macs + "/raw"]

    EMG_def = [f[EMG_Macs].attrs["sampling rate"]*1.0, f[EMG_Macs].attrs["resolution"]*1.0]

    EMG_data = np.zeros((f[EMG_Macs].attrs["nsamples"], len(EMG_data_group)-1))
    EMG_time = EMG_data_group['nSeq'][:, 0] / EMG_def[0]

    EMG_labels = []
    for i in range(0, len(EMG_data_group)-1):

        EMG_labels.append(EMG_data_group['channel_' + str(i+1)].attrs['label'])
        EMG_data[:, i] = EMG_data_group['channel_' + str(i+1)][:, 0]


    return EMG_Data(EMG_data, EMG_time, EMG_labels, EMG_def)

class EMG_Data:

    def __init__(self, EMG_data, EMG_time, EMG_labels, EMG_def):

        self.EMG_data    = EMG_data
        self.EMG_time    = EMG_time
        self.EMG_labels  = EMG_labels
        self.EMG_def     = EMG_def
        self.data_window = False

    def set_data_window(self, start, end):

        self.initial_index  = start * self.EMG_def[0]
        self.end_index      = end   * self.EMG_def[0]

        self.true_EMG_data = self.EMG_data[self.initial_index:self.end_index, :]
        self.true_EMG_time = self.EMG_time[self.initial_index:self.end_index]

        self.data_window   = True

    def average_out(self, use_data_window=True):
        print "Start Average"
        if use_data_window and self.data_window:
            self.averaged_out = copy.deepcopy(self.true_EMG_data)
            for i in range(0, np.shape(self.true_EMG_data)[1]):
                self.averaged_out[:, i] = self.true_EMG_data[:, i] - np.mean(self.true_EMG_data[:, i])

        else:
            self.averaged_out = copy.deepcopy(self.EMG_data)
            for i in range(0, np.shape(self.EMG_data)[1]):
                self.averaged_out[:, i] = self.EMG_data[:, i] - np.mean(self.EMG_data[:, i])
        print "End Average"


    def window_rms(self, window_size):
        print "Start RMS"
        window_size = window_size * self.EMG_def[0]
        lower_index = 0
        upper_index = window_size
        if hasattr(self, 'end_index') == False:
            self.end_index = len(self.EMG_data[:, 0])

        self.RMS_EMGs = np.zeros((1, 4))
        while (self.end_index) >= upper_index-1:
            temp_ = []
            for i in range(0, np.shape(self.averaged_out)[1]):
                current_points = self.averaged_out[lower_index:upper_index, i]
                temp_.append(np.sqrt((np.sum(np.power(current_points, 2))/window_size)))
            self.RMS_EMGs = np.vstack([self.RMS_EMGs, temp_])
            upper_index += 1
            lower_index += 1

        self.RMS_EMGs =  self.RMS_EMGs[1:, :]
        print "End RMS"

    def normalize_RMS(self, max_values):
        self.RMS_EMGs_Normalized = copy.deepcopy(self.RMS_EMGs)
        for i in range(0, np.shape(self.RMS_EMGs)[1]):
            self.RMS_EMGs_Normalized[:, i] = self.RMS_EMGs[:, i]/max_values[i] * 100.0

    def get_max_RMS_values(self):
        temp_ = []
        for i in range(0, np.shape(self.RMS_EMGs)[1]):
            temp_.append(max(self.RMS_EMGs[:, i]))
        return temp_
