class Engine:

    def __init__(self, spoints: int, pwn: int, pwp: int, plp: int, pln: int):
        """

        :param spoints: players starting points
        :param pwn: if the player won with negative decision
        :param pwp: if the player won with positive decision
        :param plp: if the player lost with positive decision
        :param pln: if the player lost with negative decision
        """
        self.pln = pln
        self.plp = plp
        self.pwp = pwp
        self.pwn = pwn
        self.spoints = spoints

