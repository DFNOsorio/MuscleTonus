from Muscle_Tonus import *
import seaborn
import matplotlib.pyplot as plt
import numpy as np

def max_of_normalization(dataset):
        temp_ = []
        for i in range(0, np.shape(dataset.RMS_EMGs_Normalized)[1]):
            temp_.append(max(dataset.RMS_EMGs_Normalized[:, i]))
        return temp_

MVC_Data = load_data_h5('EMGs/h5/MVC')
Arms_Extensions_Data = load_data_h5('EMGs/h5/Arms_Extensions')
Rest_Data = load_data_h5('EMGs/h5/Rest')
Right_Foot_Data = load_data_h5('EMGs/h5/Right_Foot')
Left_Foot_Data = load_data_h5('EMGs/h5/Left_Foot')
Two_Feet_Data = load_data_h5('EMGs/h5/Two_Feet')

max_values = np.zeros((6, 4))

#MVC - 0 to 8 seconds
print "MVC"
MVC_Data.set_data_window(0, 8)
MVC_Data.average_out()
MVC_Data.window_rms(0.5)
MVC_Data.normalize_RMS(MVC_Data.get_max_RMS_values())
max_values[0, :] = max_of_normalization(MVC_Data)

#Arms Extensions
print "Arms Extensions"
Arms_Extensions_Data.average_out()
Arms_Extensions_Data.window_rms(0.5)
Arms_Extensions_Data.normalize_RMS(MVC_Data.get_max_RMS_values())
max_values[1, :] = max_of_normalization(Arms_Extensions_Data)

#Rest
print "Rest"
Rest_Data.set_data_window(0, 20)
Rest_Data.average_out()
Rest_Data.window_rms(0.5)
Rest_Data.normalize_RMS(MVC_Data.get_max_RMS_values())
max_values[2, :] = max_of_normalization(Rest_Data)

#Right_Foot_Data
print "Right_Foot_Data"

Right_Foot_Data.average_out()
Right_Foot_Data.window_rms(0.5)
Right_Foot_Data.normalize_RMS(MVC_Data.get_max_RMS_values())
max_values[3, :] = max_of_normalization(Right_Foot_Data)

#Left_Foot_Data
print "Left_Foot_Data"
Left_Foot_Data.average_out()
Left_Foot_Data.window_rms(0.5)
Left_Foot_Data.normalize_RMS(MVC_Data.get_max_RMS_values())
max_values[4, :] = max_of_normalization(Left_Foot_Data)

#Two_Feet_Data
print "Two_Feet_Data"

Two_Feet_Data.average_out()
Two_Feet_Data.window_rms(0.5)
Two_Feet_Data.normalize_RMS(MVC_Data.get_max_RMS_values())
max_values[5, :] = max_of_normalization(Two_Feet_Data)

#plt.figure()
#plt.subplot(221)
#plt.plot(MVC_Data.true_EMG_time, MVC_Data.averaged_out[:, 0],'r')
#plt.plot(MVC_Data.true_EMG_time[0: len(MVC_Data.RMS_EMGs[:, 0])], MVC_Data.RMS_EMGs[:, 0])
#plt.title(MVC_Data.EMG_labels[0])
#plt.subplot(222)
#plt.plot(MVC_Data.true_EMG_time, MVC_Data.averaged_out[:, 1],'r')
#plt.plot(MVC_Data.true_EMG_time[0: len(MVC_Data.RMS_EMGs[:, 1])], MVC_Data.RMS_EMGs[:, 1])
#plt.title(MVC_Data.EMG_labels[1])
#plt.subplot(223)
#plt.plot(MVC_Data.true_EMG_time, MVC_Data.averaged_out[:, 2],'r')
#plt.plot(MVC_Data.true_EMG_time[0: len(MVC_Data.RMS_EMGs[:, 2])], MVC_Data.RMS_EMGs[:, 2])
#plt.title(MVC_Data.EMG_labels[2])
#plt.subplot(224)
#plt.plot(MVC_Data.true_EMG_time, MVC_Data.averaged_out[:, 3],'r')
#plt.plot(MVC_Data.true_EMG_time[0: len(MVC_Data.RMS_EMGs[:, 3])], MVC_Data.RMS_EMGs[:, 3])
#plt.title(MVC_Data.EMG_labels[3])
#plt.suptitle("MVC")

plt.figure()

for i in range(0, 4):
    plt.subplot(2,2, i+1)
    plt.plot(MVC_Data.true_EMG_time[0: len(MVC_Data.RMS_EMGs_Normalized[:, i])], MVC_Data.RMS_EMGs_Normalized[:, i])
    plt.plot(Arms_Extensions_Data.EMG_time[0: len(Arms_Extensions_Data.RMS_EMGs_Normalized[:, i])], Arms_Extensions_Data.RMS_EMGs_Normalized[:, i])
    plt.plot(Rest_Data.EMG_time[0: len(Rest_Data.RMS_EMGs_Normalized[:, i])], Rest_Data.RMS_EMGs_Normalized[:, 2])
    plt.plot(Right_Foot_Data.EMG_time[0: len(Right_Foot_Data.RMS_EMGs_Normalized[:, i])], Right_Foot_Data.RMS_EMGs_Normalized[:, i])
    plt.plot(Left_Foot_Data.EMG_time[0: len(Left_Foot_Data.RMS_EMGs_Normalized[:, i])], Left_Foot_Data.RMS_EMGs_Normalized[:, i])
    plt.plot(Two_Feet_Data.EMG_time[0: len(Two_Feet_Data.RMS_EMGs_Normalized[:, i])], Two_Feet_Data.RMS_EMGs_Normalized[:, i])
    plt.title(MVC_Data.EMG_labels[i], fontsize=20)
    plt.xlabel("Time (s)")
    plt.ylabel("Percentage from MVC maximum (%)")
    plt.grid(b=False)
    plt.legend(["MVC", "Arms Extension", "Rest", "Right Foot", "Left Foot", "Both Feet"])
    plt.xlim([0, 20])

plt.suptitle("Maximum for each test", fontsize=24)


plt.figure()
for i in range(0, 4):
    plt.subplot(2,2, i+1)
    plt.plot(Right_Foot_Data.EMG_time[0: len(Right_Foot_Data.RMS_EMGs_Normalized[:, i])], Right_Foot_Data.RMS_EMGs_Normalized[:, i])
    plt.plot(Left_Foot_Data.EMG_time[0: len(Left_Foot_Data.RMS_EMGs_Normalized[:, i])], Left_Foot_Data.RMS_EMGs_Normalized[:, i])
    plt.title(MVC_Data.EMG_labels[i], fontsize=20)
    plt.legend(["Right Foot", "Left Foot"])
    plt.xlabel("Time (s)")
    plt.ylabel("Percentage from MVC maximum (%)")
    plt.grid(b=False)
    plt.xlim([0, 20])
plt.suptitle("Right and Left test", fontsize=24)

plt.figure()
for i in range(0, 4):
    plt.subplot(2,2, i+1)
    ind = np.arange(6)
    width = 0.95
    plt.bar(ind, max_values[:, i], width)
    plt.xticks(ind + width/2.0, ("MVC", "Arms Extension", "Rest", "Right Foot", "Left Foot", "Both Feet"))
    plt.title(MVC_Data.EMG_labels[i], fontsize=20)
    plt.ylabel("Percentage from MVC maximum (%)")

plt.suptitle("Maximum for each test", fontsize=24)
plt.show()
