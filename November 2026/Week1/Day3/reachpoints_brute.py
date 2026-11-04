def reachpoints(sx,sy,tx,ty):
    def solve(x,y):
        if x==tx and y==ty:
            return True
        if x>tx or y>ty:
            return False
        return solve(x+y,y) or solve(x,x+y)
    return solve(sx,sy)