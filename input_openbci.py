from pyOpenBCI import OpenBCICyton
import sys
import datetime
import time

save_list = []
ANA3 = 0
name = ""
s_name = ""
bci_count = 0

def product(list):
    uVolts_per_count = (4500000)/24/(2**23-1)
    return list * uVolts_per_count

def print_raw(sample):
    global save_list, ANA3, bci_count
    EEG_to_uVolts = map(product, sample.channels_data)
    save_list.append(list(EEG_to_uVolts))
    print(list(EEG_to_uVolts))
    if datetime.datetime.now().second == 0 or datetime.datetime.now().second == 20 or datetime.datetime.now().second == 40:
        if ANA3 == 0:
            ANA3 = 1
            with open(f"./{name}/{s_name}/openbci/openbci_output_{bci_count}.txt", "w") as f:
                for d in save_list:
                    f.write("%s\n" % d)
            bci_count = bci_count + 1
            save_list = []
            time.sleep(1)
        else:
            if ANA3 == 1:
                ANA3 = 0
    
def main(a, b):
    global name, s_name
    name = a
    s_name = b
    board = OpenBCICyton(port="")
    board.start_stream(print_raw)

if __name__ == "__main__":
    args = sys.argv
    main(args[1], args[2])


# print(board.port)
# oard = OpenBCICyton(daisy=True)

