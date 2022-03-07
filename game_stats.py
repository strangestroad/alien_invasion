class GameStats():
    """Track statistics for Alien Invasion"""

    def __init__(self,s):
        """Initialize statistics"""
        self.s=s
        self.reset_stats()
        #Start Alien Invasion in an active state
        self.game_active=False
        #High score
        self.high_score=0

    def reset_stats(self):
        """Initialize statistics that can change during game"""
        self.ships_left=self.s.ship_limit
        self.score=0
        self.level=1
