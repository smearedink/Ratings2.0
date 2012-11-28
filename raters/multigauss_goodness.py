import utils
import base
from rating_classes import multigauss

class MultiGaussGoodnessOfFitRater(base.BaseRater):
    short_name = "multigauss_goodness"
    long_name = "Multi-Gauss Goodness of Fit"
    description = "Fit the profile with multiple Gaussians and " \
                  "report the goodness of the fit (reduced " \
                  "chi-square."
    version = 2

    rat_cls = multigauss.MultipleGaussianProfileClass()

    def _compute_rating(self, cand):
        """
        """
        profile = utils.get_scaled_profile(cand.profile, cand.pfd.varprof)
        mgauss = cand.multigaussfit
        chi2 = mgauss.get_chisqr(profile)
        dof = mgauss.get_dof(len(profile))
        return chi2/dof

Rater = MultiGaussGoodnessOfFitRater

