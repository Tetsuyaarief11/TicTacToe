class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]  # Papan permainan
        self.current_player = 'X'  # Pemain awal

    def display_board(self):
        """Menampilkan papan permainan."""
        print("\n")
        print("  0 | 1 | 2 ")
        print(" ----------- ")
        print("  {} | {} | {} ".format(self.board[0], self.board[1], self.board[2]))
        print(" ----------- ")
        print("  {} | {} | {} ".format(self.board[3], self.board[4], self.board[5]))
        print(" ----------- ")
        print("  {} | {} | {} ".format(self.board[6], self.board[7], self.board[8]))
        print("\n")

    def check_winner(self):
        """Memeriksa apakah ada pemenang."""
        winning_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Baris
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Kolom
            [0, 4, 8], [2, 4, 6]               # Diagonal
        ]
        for combo in winning_combinations:
            if self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]] != ' ':
                return self.board[combo[0]]
        return None

    def is_board_full(self):
        """Memeriksa apakah papan sudah penuh."""
        return ' ' not in self.board

    def play_game(self):
        """Fungsi utama untuk memainkan game."""
        print("Selamat datang di Tic-Tac-Toe!")
        self.display_board()

        while True:
            # Meminta input dari pemain
            try:
                move = int(input(f"Pemain {self.current_player}, masukkan posisi (0-8): "))
                if self.board[move] != ' ':
                    print("Posisi sudah terisi! Silakan pilih posisi lain.")
                    continue
            except (ValueError, IndexError):
                print("Input tidak valid! Silakan masukkan angka antara 0 dan 8.")
                continue

            # Memperbarui papan
            self.board[move] = self.current_player
            self.display_board()

            # Memeriksa pemenang
            winner = self.check_winner()
            if winner:
                print(f"Pemain {winner} menang!")
                break

            if self.is_board_full():
                print("Permainan berakhir seri!")
                break

            # Berganti pemain
            self.current_player = 'O' if self.current_player == 'X' else 'X'


if __name__ == "__main__":
    game = TicTacToe()
    game.play_game()
