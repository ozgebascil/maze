P = 'X'
E = '.'
W = '#'
EX = 'O'
R = 'R'
L = 'L'
U = 'U'
D = 'D'


def print_maze(maze):
    for row in maze:
        print ' '.join(row)


def get_input():
    direction = raw_input("Please enter direction l:left, r:right, u:up, d:down:")
    direction = direction.upper().strip()
    if direction not in [L, R, U, D]:
        print "This is not direction!"
        return get_input()
    return direction



def update_maze():
    pass


def check_maze():
    pass


def run_game():
    pass


if __name__ == "__main__":
    #print_maze([[W, W, W, W, W, W],
        #[W, E, E, E, P, W],
        #[W, W, E, E, E, W],
        #[W, E, E, W, W, W],
        #[W, W, E, E, EX, W],
        #[W, W, W, W, W, W]])

    print get_input()
