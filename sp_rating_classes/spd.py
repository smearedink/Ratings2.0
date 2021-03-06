import cand_info
import myprepfold as prepfold
import sp_utils

class SpdRatingClass(cand_info.CandInfoRatingClass):
    data_key = "spd"

    def _compute_data(self, cand):
        """Create an sp_utils.spd object for the candidate's 
            *.spd file

            Input:
                cand: A ratings2.0 SPCandidate object.

            Output:
                spd: The corresponding sp_utils.spd object.
        """
        spdfn = cand.info['spdfn']
        spd = sp_utils.spd(spdfn)
        return spd
