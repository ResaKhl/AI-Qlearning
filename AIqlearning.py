import numpy
import copy

def make_policy_mat(obstacles, start, end, size):
    size = int(size)
    delta = 10**8 # I am still not sure if this should be infinity or
zero, I guess that it should be zero.
    reward_mat = build_reward_matrix(obstacles, end, size)
    current_policy = [[0]*size for _ in range(size)]
    direction_mat = [[[j,i] for i in range(size)] for j in range(size)]
    direction_mat_char = [['h' for i in range(size)] for j in range(size)]
    # print current_policy
    # print reward_mat
    while(delta>(0.1**2)/0.9):
        delta = 0
        tempmatrix = copy.deepcopy(current_policy)
        for i in range(size):
            for j in range(size):
                current_cell_val = current_policy[i][j]
                calculate_policy(i, j, reward_mat, tempmatrix,
current_policy, direction_mat, direction_mat_char)
                if(current_policy[i][j]!=99 and not(i==end[0] and j==end[1])):
                    if(abs(tempmatrix[i][j]-current_cell_val) > delta):
                        # print '\n&&&&&&'
                        # print delta
                        # print '\n&&&&&&'
                        delta = abs(tempmatrix[i][j] - current_cell_val)
                        # print '\n******'
                        # print delta
                        # print '\n******'
                else: tempmatrix[i][j] = 99
        # print '**************'
        current_policy = copy.deepcopy(tempmatrix)
        # print direction_mat
    # print '\n******'
    # print direction_mat_char
    # print '\n******'
    return [current_policy, direction_mat, direction_mat_char]

def build_reward_matrix(obstacles, end, size):
    reward_matrix = [[-1]*size for _ in range(size)]
    for i in range(len(obstacles)):
        reward_matrix[obstacles[i][0]][obstacles[i][1]] -= 100
    reward_matrix[end[0]][end[1]]+=100
    return reward_matrix

def my_max_index(numlist):
    max=numlist[0]
    max_index = 0
    for i in range(len(numlist)):
        if numlist[i] > max:
            max = numlist[i]
            max_index = i
    return [max, max_index]


def calculate_policy(x, y, reward_mat, tempmatrix, current_policy,
direction_mat, direction_mat_char):
    size = len(current_policy)
    if(x==0 or y==0):
        if(x==0):
            if(y==0):
                max_mix = my_max_index(
                    # up, left
                    [0.8 * current_policy[x][y] + 0.1 *
current_policy[x][y + 1] + 0.1 * current_policy[x + 1][y],
                    # down
                    0.7 * current_policy[x + 1][y] + 0.2 *
current_policy[x][y] + 0.1 * current_policy[x][y + 1],
                    # right
                    0.7 * current_policy[x][y + 1] + 0.2 *
current_policy[x][y] + 0.1 * current_policy[x + 1][y]
                    ])

                tempmatrix[x][y] = reward_mat[x][y] + 0.9 * max_mix[0]
                if(max_mix[1]==0):
                    direction_mat[x][y] = [x, y]
                    direction_mat_char[x][y] = 'h'
                if(max_mix[1]==1):
                    direction_mat[x][y] = [x+1, y]
                    direction_mat_char[x][y] = 's'
                if(max_mix[1]==2):
                    direction_mat[x][y] = [x, y+1]
                    direction_mat_char[x][y] = 'e'
                return

            elif(y!=0 and y!=size-1):
                max_mix = my_max_index([
                    # up
                    0.7 * current_policy[x][y] + 0.1 *
current_policy[x][y - 1] + 0.1 * current_policy[x][
                        y + 1] + 0.1 * current_policy[x + 1][y],
                    # down
                    0.7 * current_policy[x + 1][y] + 0.1 *
current_policy[x][y] + 0.1 * current_policy[x][
                        y - 1] + 0.1 * current_policy[x][y + 1],
                    # left
                    0.7 * current_policy[x][y - 1] + 0.1 *
current_policy[x][y] + 0.1 * current_policy[x][
                        y + 1] + 0.1 * current_policy[x + 1][y],
                    # right
                    0.7 * current_policy[x][y + 1] + 0.1 *
current_policy[x][y] + 0.1 * current_policy[x][
                        y - 1] + 0.1 * current_policy[x + 1][y],
                ])
                tempmatrix[x][y] = reward_mat[x][y] + 0.9 * max_mix[0]
                if (max_mix[1] == 0):
                    direction_mat[x][y] = [x, y]
                    direction_mat_char[x][y] = 'h'
                if (max_mix[1] == 1):
                    direction_mat[x][y] = [x + 1, y]
                    direction_mat_char[x][y] = 's'
                if (max_mix[1] == 2):
                    direction_mat[x][y] = [x, y - 1]
                    direction_mat_char[x][y] = 'w'
                if (max_mix[1] == 3):
                    direction_mat[x][y] = [x, y + 1]
                    direction_mat_char[x][y] = 'e'
                return

            elif(y==size-1):
                max_mix = my_max_index([
                    # up, right
                    0.8 * current_policy[x][y] + 0.1 *
current_policy[x][y - 1] + 0.1 * current_policy[x + 1][y],
                    # down
                    0.7 * current_policy[x + 1][y] + 0.2 *
current_policy[x][y] + 0.1 * current_policy[x][
                        y - 1],
                    # left
                    0.7 * current_policy[x - 1][y] + 0.2 *
current_policy[x][y] + 0.1 * current_policy[x + 1][y],
                ])
                tempmatrix[x][y] = reward_mat[x][y] + 0.9 * max_mix[0]
                if (max_mix[1] == 0):
                    direction_mat[x][y] = [x, y]
                    direction_mat_char[x][y] = 'h'
                if (max_mix[1] == 1):
                    direction_mat[x][y] = [x + 1, y]
                    direction_mat_char[x][y] = 's'
                if (max_mix[1] == 2):
                    direction_mat[x][y] = [x, y - 1]
                    direction_mat_char[x][y] = 'w'
                return

        elif(x!=0 and y==0):
            if(x!=size-1):
                max_mix = my_max_index([
                    # up
                    0.7 * current_policy[x - 1][y] + 0.1 *
current_policy[x][y] + 0.1 * current_policy[x][
                        y + 1] + 0.1 * current_policy[x + 1][y],
                    # down
                    0.7 * current_policy[x + 1][y] + 0.1 *
current_policy[x][y] + 0.1 * current_policy[x - 1][
                        y] + 0.1 * current_policy[x][y + 1],
                    # left
                    0.7 * current_policy[x][y] + 0.1 *
current_policy[x - 1][y] + 0.1 * current_policy[x][
                        y + 1] + 0.1 * current_policy[x + 1][y],
                    # right
                    0.7 * current_policy[x][y + 1] + 0.1 *
current_policy[x][y] + 0.1 * current_policy[x - 1][
                        y] + 0.1 * current_policy[x + 1][y],
                ])
                tempmatrix[x][y] = reward_mat[x][y] + 0.9 * max_mix[0]
                if (max_mix[1] == 0):
                    direction_mat[x][y] = [x - 1, y]
                    direction_mat_char[x][y] = 'n'
                if (max_mix[1] == 1):
                    direction_mat[x][y] = [x + 1, y]
                    direction_mat_char[x][y] = 's'
                if (max_mix[1] == 2):
                    direction_mat[x][y] = [x, y]
                    direction_mat_char[x][y] = 'h'
                if (max_mix[1] == 3):
                    direction_mat[x][y] = [x, y + 1]
                    direction_mat_char[x][y] = 'e'
                return

            elif(x==size-1):
                max_mix = my_max_index([
                    # down, left
                    0.8 * current_policy[x][y] + 0.1 *
current_policy[x][y + 1] + 0.1 * current_policy[x - 1][y],
                    # up
                    0.7 * current_policy[x - 1][y] + 0.2 *
current_policy[x][y] + 0.1 * current_policy[x][
                        y + 1],
                    # right
                    0.7 * current_policy[x][y + 1] + 0.2 *
current_policy[x][y] + 0.1 * current_policy[x - 1][y],
                ])
                tempmatrix[x][y] = reward_mat[x][y] + 0.9 * max_mix[0]
                if (max_mix[1] == 0):
                    direction_mat[x][y] = [x, y]
                    direction_mat_char[x][y] = 'h'
                if (max_mix[1] == 1):
                    direction_mat[x][y] = [x - 1, y]
                    direction_mat_char[x][y] = 'n'
                if (max_mix[1] == 2):
                    direction_mat[x][y] = [x, y+1]
                    direction_mat_char[x][y] = 'e'
                return

    elif(x==size-1):
        if(y!=size-1 and y!=0):
            max_mix = my_max_index([
                # up
                0.7 * current_policy[x - 1][y] + 0.1 *
current_policy[x][y] + 0.1 * current_policy[x][
                    y + 1] + 0.1 * current_policy[x][y - 1],
                # down
                0.7 * current_policy[x][y] + 0.1 * current_policy[x -
1][y] + 0.1 * current_policy[x][
                    y + 1] + 0.1 * current_policy[x][y - 1],
                # left
                0.7 * current_policy[x][y - 1] + 0.1 *
current_policy[x - 1][y] + 0.1 * current_policy[x][
                    y + 1] + 0.1 * current_policy[x][y],
                # right
                0.7 * current_policy[x][y + 1] + 0.1 *
current_policy[x][y] + 0.1 * current_policy[x - 1][
                    y] + 0.1 * current_policy[x][y + 1],
            ])
            tempmatrix[x][y] = reward_mat[x][y] + 0.9 * max_mix[0]
            if (max_mix[1] == 0):
                direction_mat[x][y] = [x - 1, y]
                direction_mat_char[x][y] = 'n'
            if (max_mix[1] == 1):
                direction_mat[x][y] = [x, y]
                direction_mat_char[x][y] = 'h'
            if (max_mix[1] == 2):
                direction_mat[x][y] = [x, y - 1]
                direction_mat_char[x][y] = 'w'
            if (max_mix[1] == 3):
                direction_mat[x][y] = [x, y + 1]
                direction_mat_char[x][y] = 'e'
            return

        if(y==size-1):
            max_mix = my_max_index([
                # down, right
                0.8 * current_policy[x][y] + 0.1 * current_policy[x][y
- 1] + 0.1 * current_policy[x - 1][y],
                # up
                0.7 * current_policy[x - 1][y] + 0.2 *
current_policy[x][y] + 0.1 * current_policy[x][
                    y - 1],
                # left
                0.7 * current_policy[x][y - 1] + 0.2 *
current_policy[x][y] + 0.1 * current_policy[x - 1][y],
            ])
            tempmatrix[x][y] = reward_mat[x][y] + 0.9 * max_mix[0]
            if (max_mix[1] == 0):
                direction_mat[x][y] = [x, y]
                direction_mat_char[x][y] = 'h'
            if (max_mix[1] == 1):
                direction_mat[x][y] = [x - 1, y]
                direction_mat_char[x][y] = 'n'
            if (max_mix[1] == 2):
                direction_mat[x][y] = [x, y - 1]
                direction_mat_char[x][y] = 'w'
            return

    elif(x!=0 and x!=size-1 and y==size-1):
        max_mix = my_max_index([
            # up
            0.7 * current_policy[x - 1][y] + 0.1 * current_policy[x +
1][y] + 0.1 * current_policy[x][
                y] + 0.1 * current_policy[x][y - 1],
            # down
            0.7 * current_policy[x + 1][y] + 0.1 * current_policy[x -
1][y] + 0.1 * current_policy[x][
                y] + 0.1 * current_policy[x][y - 1],
            # left
            0.7 * current_policy[x][y - 1] + 0.1 * current_policy[x -
1][y] + 0.1 * current_policy[x][
                y] + 0.1 * current_policy[x + 1][y],
            # right
            0.7 * current_policy[x][y] + 0.1 * current_policy[x][y -
1] + 0.1 * current_policy[x - 1][
                y] + 0.1 * current_policy[x + 1][y],
        ])
        tempmatrix[x][y] = reward_mat[x][y] + 0.9 * max_mix[0]
        if (max_mix[1] == 0):
            direction_mat[x][y] = [x - 1, y]
            direction_mat_char[x][y] = 'n'
        if (max_mix[1] == 1):
            direction_mat[x][y] = [x + 1, y]
            direction_mat_char[x][y] = 's'
        if (max_mix[1] == 2):
            direction_mat[x][y] = [x, y - 1]
            direction_mat_char[x][y] = 'w'
        if (max_mix[1] == 3):
            direction_mat[x][y] = [x, y]
            direction_mat_char[x][y] = 'h'
        return

    elif(x!=0 and x!=size-1 and y!=0 and y!=size-1):
        # up = , down = , left = , right =
        max_mix = my_max_index([
            # up
            0.7 * current_policy[x - 1][y] + 0.1 * current_policy[x][y
- 1] + 0.1 * current_policy[x][y + 1] + 0.1 *
            current_policy[x + 1][y],
            # down
            0.7 * current_policy[x + 1][y] + 0.1 * current_policy[x][y
- 1] + 0.1 * current_policy[x][y + 1] + 0.1 *
            current_policy[x - 1][y],
            # left
            0.7 * current_policy[x][y - 1] + 0.1 * current_policy[x -
1][y] + 0.1 * current_policy[x][y + 1] + 0.1 *
            current_policy[x + 1][y],
            # right
            0.7 * current_policy[x][y + 1] + 0.1 * current_policy[x -
1][y] + 0.1 * current_policy[x][y - 1] + 0.1 *
            current_policy[x + 1][y],
        ])
        tempmatrix[x][y] = reward_mat[x][y] + 0.9 * max_mix[0]
        if (max_mix[1] == 0):
            direction_mat[x][y] = [x - 1, y]
            direction_mat_char[x][y] = 'n'
        if (max_mix[1] == 1):
            direction_mat[x][y] = [x + 1, y]
            direction_mat_char[x][y] = 's'
        if (max_mix[1] == 2):
            direction_mat[x][y] = [x, y - 1]
            direction_mat_char[x][y] = 'w'
        if (max_mix[1] == 3):
            direction_mat[x][y] = [x, y + 1]
            direction_mat_char[x][y] = 'e'
        return

def move_cars(cars, obstacles, start_locations, terminal_locations):
    list_to_write = []
    for i in range(cars):
        print 'hello'
        temp = make_policy_mat(obstacles, start_locations[i],
terminal_locations[i], size_of_grid)
        policy = temp[0]
        direction = temp[1]
        direction_char = temp[2]
        sum_of_rewards = 0
        for j in range(10):
            numpy.random.seed(j+1)
            swerve = numpy.random.random_sample(10**6)
            total_reward = policy[start_locations[i][0]][start_locations[i][1]]
            k=0
            pos = start_locations[i]
            move = direction[pos[0]][pos[1]]
            while (not (pos[0] == terminal_locations[i][0] and
pos[1]==terminal_locations[i][1])):
                move_char = direction_char[pos[0]][pos[1]]
                if(swerve[k]>0.7):
                    if(swerve[k]>0.8):
                        if (swerve[k] > 0.9):
                            move=turn_left_2wice(move, pos,
direction_char, int(size_of_grid))
                        else:
                            move = turn_left(move, pos,
direction_char, int(size_of_grid))
                    else:
                        move = turn_right(move, pos, direction_char,
int(size_of_grid))
                else:
                    move = direction[pos[0]][pos[1]]
                pos = [move[0], move[1]]
                total_reward += policy[move[0]][move[1]]
                k+=1
            sum_of_rewards +=total_reward
        simulation_output = sum_of_rewards/10 #output of simulation for car i
        to_write_amount = numpy.floor(simulation_output)
        list_to_write.append(to_write_amount)


    with open('output.txt', 'w') as f2:
        for xx in list_to_write:
            str_to_write = int(xx).__str__()
            f2.write(str_to_write+'\n')


def turn_left(move, pos, direction_char, size):
    next_dir = ''
    if(direction_char=='h'):
        next_dir = 'w'
    if(direction_char=='n'):
        next_dir = 'w'
    if(direction_char=='w'):
        next_dir = 's'
    if(direction_char=='s'):
        next_dir = 'e'
    if(direction_char=='e'):
        next_dir = 'n'
    return next_pos(move, pos, direction_char, size)

def turn_left_2wice(move, pos, direction_char, size):
    next_dir = ''
    if (direction_char == 'h'):
        next_dir = 's'
    if (direction_char == 'n'):
        next_dir = 's'
    if (direction_char == 'w'):
        next_dir = 'e'
    if (direction_char == 's'):
        next_dir = 'n'
    if (direction_char == 'e'):
        next_dir = 'w'
    return next_pos(move, pos, direction_char, size)

def turn_right(move, pos, direction_char, size):
    next_dir = ''
    if (direction_char == 'h'):
        next_dir = 'e'
    if (direction_char == 'n'):
        next_dir = 'e'
    if (direction_char == 'w'):
        next_dir = 'n'
    if (direction_char == 's'):
        next_dir = 'w'
    if (direction_char == 'e'):
        next_dir = 's'
    return next_pos(move, pos, direction_char, size)

def next_pos(move, pos, direction_char, size):
    if(pos[0]==0 or pos[1]==0):
        if(pos[0]==0):
            if(pos[1]==0):
                if(direction_char=='n' or direction_char=='w'): move =
[pos[0], pos[1]]
                if(direction_char=='s'): move = [pos[0]+1, pos[1]]
                if(direction_char=='e'): move = [pos[0], pos[1]+1]
                return move
            elif(pos[1]!=0 and pos[1]!=size-1):
                if (direction_char == 'n'): move = [pos[0], pos[1]]
                if (direction_char == 'w'): move = [pos[0], pos[1]-1]
                if (direction_char == 's'): move = [pos[0], pos[1]]
                if (direction_char == 'e'): move = [pos[0], pos[1] + 1]
                return  move
            elif(pos[1]==size-1):
                if (direction_char == 'n' or direction_char == 'e'):
move = [pos[0], pos[1]]
                if (direction_char == 'w'): move = [pos[0], pos[1]-1]
                if (direction_char == 's'): move = [pos[0]+1, pos[1]]
                return move
        elif(pos[0]!=0 and pos[0]!=size-1):
            if(pos[1]==0): #could be ommited
                if (direction_char == 'n'): move = [pos[0]-1, 0]
                if (direction_char == 'w'): move = [pos[0], 0]
                if (direction_char == 's'): move = [pos[0]+1, 0]
                if (direction_char == 'e'): move = [pos[0], 1]
                return  move
        elif(pos[0]==size-1):
            if (pos[1] == 0): #could be ommited
                if (direction_char == 'n'): move = [pos[0] - 1, pos[1]]
                if (direction_char == 'w' or direction_char == 's'):
move = [pos[0], pos[1]]
                if (direction_char == 'e'): move = [pos[0], pos[1]+1]
                return move
    elif(pos[0]==size-1):
        if(pos[1]!=0 and pos[1]!=size-1):
            if (direction_char == 'n'): move = [pos[0] - 1, pos[1]]
            if (direction_char == 'w'): move = [pos[0], pos[1] - 1]
            if (direction_char == 's'): move = [pos[0], pos[1]]
            if (direction_char == 'e'): move = [pos[0], pos[1]+1]
            return move
        if(pos[1]==size-1):
            if (direction_char == 'n'): move = [pos[0] - 1, pos[1]]
            if (direction_char == 'w'): move = [pos[0], pos[1] - 1]
            if (direction_char == 's' and direction_char == 'e'): move
= [pos[0], pos[1]]
            return move
    elif(pos[1]==size-1):
        if(pos[0]!=0 and pos[0]!=size-1):
            if (direction_char == 'n'): move = [pos[0] - 1, pos[1]]
            if (direction_char == 'w'): move = [pos[0], pos[1] - 1]
            if (direction_char == 's'): move = [pos[0]+1, pos[1]]
            if (direction_char == 'e'): move = [pos[0], pos[1]]
            return move
    else:
        if (direction_char == 'n'): move = [pos[0] - 1, pos[1]]
        if (direction_char == 'w'): move = [pos[0], pos[1] - 1]
        if (direction_char == 's'): move = [pos[0] + 1, pos[1]]
        if (direction_char == 'e'): move = [pos[0], pos[1] + 1]
        return move


if __name__ == '__main__':
    with open('input1.txt', 'r') as f:
        size_of_grid = f.readline()
        number_of_cars = f.readline()
        number_of_obstacles = f.readline()
        obstacles = []
        start_locations = []
        terminal_locations = []
        # obstacles
        for x in range(int(number_of_obstacles)):
            str = f.readline()
            obstacles.append([int(str[0]), int(str[2])])
        # start-mat
        for x in range(int(number_of_cars)):
            str = f.readline()
            start_locations.append([int(str[0]), int(str[2])])
        # terminal-mat
        for x in range(int(number_of_cars)):
            str = f.readline()
            terminal_locations.append([int(str[0]), int(str[2])])
        move_cars(int(number_of_cars), obstacles, start_locations,
terminal_locations)
    #         pos = cars[i]
    #         numpy.random.seed(j+1)
    #         swerve = numpy.random.random_sample(100000)
    #         k=0
    #         while(pos != ends[i]):
    #             move = policies[i][pos]
    #             if(swerve[k]>0.7):
    #                 if(swerve[k]>0.8):
    #                     if (swerve[k] > 0.9):
    #                         move=turn_left(turn_left(move))
    #                     else:
    #                         move = turn_left(move)
    #                 else:
    #                     move = turn_right(move)
    #             k+=1
