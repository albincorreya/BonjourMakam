import numpy as np

def convert_to_cent(pitch_hz, tonic):
    """Converting the pitch values from frequency to cent

        Parameters
        ----------
        pitch_hz : numpy.array
            Frequency values of the pitch
        tonic : float or str
            Tonic frequency to use

        Returns
        -------
        cent_val : numpy.array
            Cent values of the pitch relative to the tonic
    """
    cent_val = 1200 * np.log2(pitch_hz / np.float(tonic))

    # folding the values into the range (0, 1200)
    for k in range(0, cent_val.size):
        while cent_val[k] < 0:
            cent_val[k] = cent_val[k] + 1200
        while cent_val[k] >= 1200:
            cent_val[k] = cent_val[k] - 1200

    return {'cent_val': cent_val}
