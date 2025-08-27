/**
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function(prices) {
    let min_price = Infinity, max_profit = -Infinity;
    for(let price of prices){
        max_profit = Math.max(max_profit, price-min_price);
        min_price = Math.min(min_price, price);
    }
    return Math.max(0, max_profit);
};