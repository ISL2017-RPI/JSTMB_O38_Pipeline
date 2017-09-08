import sys
import JSTMB_O38
import numpy as np

def JMISTMB(data_file, target_file):
    jstmb = JSTMB_O38.initialize()
    feat = jstmb.JSTMB_primitive_O38(data_file, target_file)
    return feat


if __name__ == "__main__":
    data = 'trainData.csv'
    target = 'trainTargets.csv'
    selected_feature = np.array(JMISTMB(data, target), dtype=np.int16)
    np.savetxt('Features_O38_JSTMB.csv', selected_feature, delimiter=',')
    print selected_feature
