/**
 * @param {number[][]} obstacleGrid
 * @return {number}
 */
var uniquePathsWithObstacles = function(obstacleGrid) {
    if(obstacleGrid[0][0] == 1) return 0;
    m = obstacleGrid.length;
    n = obstacleGrid[0].length;
    const dp = Array.from({length: m}, () => Array(n).fill(0));
    dp[0][0] = 1;
    for(let i=0;i<m;i++){
        if(obstacleGrid[i][0]==1) break;
        dp[i][0] = 1;
    }
    for(let j=0;j<n;j++){
        if(obstacleGrid[0][j]==1) break;
        dp[0][j] = 1;
    }
    for(let i=1;i<m;i++){
        for(let j=1;j<n;j++){
            if(obstacleGrid[i][j]==1) dp[i][j] = 0;
            else{
                dp[i][j] = dp[i-1][j] + dp[i][j-1];
            }
        }
    }
    return dp[m-1][n-1];
};