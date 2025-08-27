/**
 * @param {number} numCourses
 * @param {number[][]} prerequisites
 * @return {number[]}
 */
var findOrder = function(numCourses, prerequisites) {
    var build_adj_list = (n, edges) => {
        let adj_list = Array.from({length:n}, ()=>[]);
        for(const edge of edges){
            adj_list[edge[0]].push(edge[1]);
        }
        return adj_list;
    }
    const adj_list = build_adj_list(numCourses, prerequisites);
    const visited = new Array(numCourses).fill(0);
    const result = new Array();
    var dfs = (i) => {
        if(visited[i]==-1) return false;
        if(visited[i]==1) return true;
        visited[i] = -1;
        for(const neighbor of adj_list[i]){
            if(!dfs(neighbor)){
                return false;
            }
        }    
        visited[i] = 1;
        result.push(i);
        return true;
        }
    
    for(let i=0;i<numCourses;i++){
        if(visited[i] == 0)
            if(dfs(i) == false)
                return []
    }
    return result;
};