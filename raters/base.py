import rating_value
import rating_classes

class BaseRater(object):
    short_name = NotImplemented
    long_name = NotImplemented
    description = NotImplemented
    version = NotImplemented
    
    rat_cls = NotImplemented

    def __init__(self):
        super(BaseRater, self).__init__()
        self._setup()

    def _setup(self):
        """A setup method to be called when the Rater is initialised
        
            Inputs:
                None

            Outputs:
                None
        """
        pass

    def rate(self, cand):
        """Give a candidate rate it and return the rating value.

            Input:
                cand: A Candidate object to rate.

            Output:
                ratval: A RatingValue object.
        """
        self.rat_cls.add_data(cand)
        value = self._compute_rating(cand)
        ratval = rating_value.RatingValue(self.long_name, self.version, \
                                    self.description, value)
        return ratval

    def _compute_rating(self, cand):
        """Give a candidate rate it and return the rating value.

            Input:
                cand: A Candidate object to rate.

            Output:
                value: A floating-point value - the rating value.
        """
        raise NotImplementedError("The '_compute_rating' method of " \
                                  "BaseRater should be overshadowed by " \
                                  "a full implementation by subclasses " \
                                  "of BaseRater.")
