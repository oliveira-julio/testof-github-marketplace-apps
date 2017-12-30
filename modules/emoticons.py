class Emoticon:
    @classmethod
    def smile(cls, s):
        return ":D {}".format(s)
    @classmethod
    def cry(cls, s):
        return ":'( {}".format(s)