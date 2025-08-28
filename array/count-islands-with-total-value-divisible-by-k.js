/**
 * @param {number[][]} grid
 * @param {number} k
 * @return {number}
 */
var countIslands = function(grid, k) {
    const m = grid.length, n = grid[0].length;
    const dirs = [[0, 1], [1, 0], [-1, 0], [0, -1]];
    let dfs = (x, y) => {
        if(x<0||x>m-1||y<0||y>n-1||grid[x][y]===0) return 0;
        let sum = grid[x][y];
        grid[x][y] = 0;
        for(const [dx, dy] of dirs){
            let nx = x + dx, ny = y + dy;
            sum += dfs(nx, ny);
        }
        return sum;
    };
    let count = 0;
    for(let x=0;x<m;x++){
        for(let y=0;y<n;y++){
            if(grid[x][y]!==0){
                sum = dfs(x, y);
                if(sum%k===0){
                    count++;
                }
            }
        }
    }
    return count;
};