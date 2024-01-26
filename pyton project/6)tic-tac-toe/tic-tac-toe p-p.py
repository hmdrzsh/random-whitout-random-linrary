def board_game(board): # تابع ساخت دوز
    print(board[0] + '|' + board[1] + '|' + board[2])
    print(board[3] + '|' + board[4] + '|' + board[5])
    print(board[6] + '|' + board[7] + '|' + board[8])

def check_winner(board, player): # تابع شرایط بردن بازی
    win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)] # انواع موقعیت برد در بازی
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] == player:
            return True
    return False

def tic_tac_toe(): # تابع اصلی بازی
    print('به بازی دوز خوش آمدید! ')
    print('در این بازی میتونید به صورت دو نفره با دوست خود بازی کنید...')
    print('همین الان شروع کنید!')
    board = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    current_player = 'X'
    while True:
        board_game(board)
        position = int(input('بازیکن ' + current_player + ' از 1 تا 9 انتخاب کن: ')) - 1
        if board[position] == 'X' or board[position] == 'O': # اطمینان از خالی بودن خونه انتخابی
            print('این خونه قبلا پر شده... لطفا یک خونه دیگه انتخاب کن!')
            continue # ادامه ندادن در صورت پر بودن خانه مورد نظر
        board[position] = current_player
        if check_winner(board, current_player): # چک کردن شرط برنده با تابع برنده
            board_game(board)
            print('بازیکن ' + current_player + ' برنده شد!')
            break
        if current_player == 'X': # تغییر نوبت بازیکن
            current_player = 'O'
        else:
            current_player = 'X'

tic_tac_toe() # دوز استارت بازی 
