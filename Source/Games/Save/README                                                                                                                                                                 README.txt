These two programs are used as a 'saver' and 'receiver' for opening 2.7 games from a 3.5 program, while this is not the best solution
at all, it is the most efficient given the time frame and size of the games in question. The '27save' program saves the game data in 
the format 'score, game', while this is then stored line by line in a file named 'username_game.esp'. For example if the game was pacman, 
and the player scored 10 the format would be '10, pacman' inside a file with the name 'burnm035.318_pacman.esp'. The receiver program then
receives the file on the other end, using the username got from the getpass module. 
