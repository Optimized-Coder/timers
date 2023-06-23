from timer import start_timer

def main(pomodoro_target):
    '''
    Function: Uses the timer function to run a pomodoro program
    Parameters: pomodoro_target (int); how many times you want the program to run
    Returns: None 
    '''
    num_pomodoro = 0
    print(f'You are doing {pomodoro_target} pomodoros')
    while num_pomodoro < pomodoro_target:
        print(f'Get to work. Pomodoro {num_pomodoro+1}')
        start_timer(0,25,0)
        num_pomodoro += 1
        if num_pomodoro < pomodoro_target:
            print('Take a break')
            start_timer(0,5,0)
    print(f'Done. Completed: {num_pomodoro} pomodoros')
        

if __name__ == '__main__':
    main(1)