class LoyaltyPoint:
    POINTS_2_PAISA = 1   # 1 point = 1 paisa
    @staticmethod
    def calculate(payment):
        return int(payment.amount/100)
 
    @staticmethod
    def calculate_paisa(points):
        return int(points*LoyaltyPoint.POINTS_2_PAISA)       