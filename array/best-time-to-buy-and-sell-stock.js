/**
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function(prices) {
    let min_price = Infinity, max_profit = 0;
    for(let price of prices){
        max_profit = Math.max(max_profit, price-min_price);
        min_price = Math.min(min_price, price);
    }
    return max_profit;
};