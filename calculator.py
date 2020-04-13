class ProfitCalculator:

    def __init__(self):
        self.result = {
            "proceeds": 0.0,
            "cost": 0,
            "total_purchase_price": 0,
            "buy_commission": 0,
            "sell_commission": 0,
            "capital_tax_gain": 0,
            "net_profit": 0,
            "roi": 0,
            "break_even": 0
        }

    def calculate_profit(self, data):
        allotment = float(data.get('allotment'))
        final_share_price = float(data.get('final_share_price'))
        sell_commission = float(data.get('sell_commission'))
        initial_share_price = float(data.get('initial_share_price'))
        buy_commission = float(data.get('buy_commission'))
        capital_gain_rate = float(data.get('capital_gain_rate'))

        # Proceeds from the Selling of Shares (Allotment x Final share price)
        proceeds = allotment * final_share_price
        total_purchase_price = allotment * initial_share_price
        commissions = sell_commission + buy_commission

        gross_profit = total_purchase_price + commissions
        capital_gain_tax = (capital_gain_rate / 100) * (proceeds - gross_profit)

        net_profit = (proceeds - gross_profit) - capital_gain_tax
        cost = proceeds - net_profit

        # Return on investment (in %), Net Profit / Total Investment * 100.
        roi = round((net_profit / cost) * 100, 2)

        # Minimum Break even price for Selling:
        break_even = (total_purchase_price + commissions) / 100

        self.result["proceeds"] = proceeds
        self.result["total_purchase_price"] = total_purchase_price
        self.result["cost"] = cost
        self.result["sell_commission"] = sell_commission
        self.result["buy_commission"] = buy_commission
        self.result["capital_tax_gain"] = capital_gain_tax
        self.result["net_profit"] = net_profit
        self.result["roi"] = roi
        self.result["break_even"] = break_even

        return self.result
