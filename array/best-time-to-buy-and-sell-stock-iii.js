/**
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function(prices) {
    let min_price1 = Infinity, max_profit1 = 0, min_price2 = Infinity, max_profit2 = 0;
    for(price of prices){
        min_price1 = Math.min(min_price1, price);
        max_profit1 = Math.max(max_profit1, price - min_price1);
        min_price2 = Math.min(min_price2, price - max_profit1);
        max_profit2 = Math.max(max_profit2, price - min_price2);
    }
    return max_profit2;
};