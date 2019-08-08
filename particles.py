def particles(speed, initial_state):
    initial_state_left = [i for i, e in enumerate(initial_state) if e == 'L']
    initial_state_right = [i for i, e in enumerate(initial_state) if e == 'R']
    chamber_size = len(initial_state)

    while True:
        chamber = list('.' * chamber_size)
        for i in initial_state_left:
            if i >= 0:
                chamber[i] = 'X'

        for i in initial_state_right:
            if i < len(chamber):
                chamber[i] = 'X'

        initial_state_left = [i - speed for i in initial_state_left]
        initial_state_right = [i + speed for i in initial_state_right]

        print("".join(chamber))
        if chamber == list('.' * chamber_size):
            break