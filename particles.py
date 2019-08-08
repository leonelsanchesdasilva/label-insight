def animate(speed, initial_state):
    if not isinstance(speed, int):
        raise ValueError('Speed parameter should be an integer value.')

    if speed <= 0:
        raise ValueError('Speed parameter should be greater than zero.')

    if len(initial_state) < 1:
        raise ValueError('Initial Chamber State should not be empty')

    initial_state_left = [i for i, e in enumerate(initial_state) if e == 'L']
    initial_state_right = [i for i, e in enumerate(initial_state) if e == 'R']
    chamber_size = len(initial_state)

    chamber_states = []

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

        chamber_states.append("".join(chamber))
        if chamber == list('.' * chamber_size):
            break

    return chamber_states