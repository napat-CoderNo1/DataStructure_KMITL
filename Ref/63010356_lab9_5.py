def maxIndex_points( a , index , n ):
    if index == n:
        return index 
    k = maxIndex_points(a, index + 1, n)   
    return (index if int(a[index]['points']) > int(a[k]['points']) else k)

def maxIndex_gd( a , index , n ):
    if index == n:
        return index 
    k = maxIndex_gd(a, index + 1, n)   
    return (k if int(a[index]['points']) == int(a[k]['points']) and int(a[index]['gd']) < int(a[k]['gd'] ) else index)
 
def sort_point(lst, n, index = 0): 
 
    if index == n:
        return -1    
    k = maxIndex_points(lst, index, n-1)  
    if k != index :
        lst[k], lst[index] = lst[index], lst[k]

    sort_point(lst, n, index + 1)

def sort_gd(lst, n, index = 0):
 
    if index == n:
        return -1    
    k = maxIndex_gd(lst, index, n-1)  
    
    if k != index  and lst[k]['points'] == lst[index]['points']:
        lst[k], lst[index] = lst[index], lst[k]

    sort_gd(lst, n, index + 1)

def checkpoints(lst,index = 0):
    if index == len(lst)-1:
        return True
    checkpoints(lst,index+1)
    if  lst[index]['points']  == lst[index+1]['points'] or lst[index]['points']  >= lst[index+1]['points'] or lst[index]['points']  == lst[index+1]['points']:
        return True
    else:
        return False

def Cal_score(team):
    score = 3 * team['wins'] + 0 * team['loss'] + 1 * team['draws']
    return score

def Cal_conceded(team):
    Goal_Difference = team['scored'] - team['conceded']
    return Goal_Difference

input_ball = input("Enter Input : ").split('/')
lst_team = []
for e in input_ball:
    team = {}
    lst = []
    lst =  e.split(',')
    team['name'] = lst[0]
    team['wins'] = int(lst[1])
    team['loss'] = int(lst[2])
    team['draws'] = int(lst[3])
    team['scored'] = int(lst[4])
    team['conceded'] = int(lst[5])
    lst_team.append(team)
lst_football = []
for i in lst_team:
    football = {}
    football['name'] = i['name']
    football['points'] = Cal_score(i)
    football['gd'] = Cal_conceded(i)
    lst_football.append(football)
sort_point(lst_football,len(lst_football))
if checkpoints(lst_football) is True:
    sort_gd(lst_football,len(lst_football))
lst_output_real = []
for i in lst_football:
    lst_output = []
    football_points = {}
    lst_output.append(i['name'])
    football_points['points'] = i['points']
    football_gd = {}
    football_gd['gd'] = i['gd']
    lst_output.append(football_points)
    lst_output.append(football_gd)
    lst_output_real.append(lst_output)
print('== results ==')
for i in lst_output_real:
    print(i)
