from Presciption_data import *

trial_patients = ["Denise", "Eddie", "Frank", "Georgia", "Kenny"]

# remove warfarin and add edoxaban
for patient in trial_patients:
    prescription = patients[patient]
    if warfarin in prescription:
        prescription.remove(warfarin)
        prescription.add(edoxaban)
    else:
        print(f"Patient {patient} is not taking Warfarin"
              f"Please remove {patient} from the trial")
    print(patient, prescription)