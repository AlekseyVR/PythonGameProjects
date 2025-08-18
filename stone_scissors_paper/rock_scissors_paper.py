import tkinter as tk
import random
from pathlib import Path
from typing import Tuple

from stone_scissors_paper.enums.Items import Items
from stone_scissors_paper.enums.result_colors import ResultColors
from stone_scissors_paper.l10n import en


HORIZONTAL: int = 800
VERTICAL: int = 400
BG_COLOR: str = "lightblue"


class RockPaperScissorsApp(tk.Tk):
    """Application "Rock-scissors-Paper" on Tkinter in OOP style."""

    def __init__(self) -> None:
        super().__init__()
        self._configure_window()
        self._load_assets()
        self._resolve_enum_members()
        self._build_ui()

    def _configure_window(self) -> None:
        self.geometry(f"{HORIZONTAL}x{VERTICAL}")
        self.title(en["title"])

    def _load_assets(self) -> None:
        base_dir: Path = Path(__file__).resolve().parent
        img_dir: Path = base_dir / "img"
        self.rock_img = tk.PhotoImage(file=str(img_dir / "stone.png"))
        self.paper_img = tk.PhotoImage(file=str(img_dir / "paper.png"))
        self.scissors_img = tk.PhotoImage(file=str(img_dir / "cut.png"))

    def _resolve_enum_members(self) -> None:
        self.enum_rock: Items = getattr(Items, "ROCK")
        self.enum_paper: Items = getattr(Items, "PAPER")
        self.enum_scissors: Items = getattr(Items, "SCISSORS")

    def _build_ui(self) -> None:
        self.main_frame = tk.Frame(self, bg=BG_COLOR)
        self.main_frame.place(relx=0.01, rely=0.01, relwidth=0.98, relheight=0.98)

        self.header_label = tk.Label(self.main_frame, text=en["header_pl_vs_pc"], font="100", bg=BG_COLOR)
        self.header_label.place(x=298, y=20)

        self.label_player = tk.Label(self.main_frame, text=en["player"], font="normal 15", bg=BG_COLOR)
        self.label_vs = tk.Label(self.main_frame, text=en["vs"], font="normal 15", bg=BG_COLOR)
        self.label_computer = tk.Label(self.main_frame, text=en["computer"], font="normal 15", bg=BG_COLOR)

        self.label_player.place(x=80, y=50, width=100)
        self.label_vs.place(x=350, y=50, width=100)
        self.label_computer.place(x=550, y=50, width=150)

        self.user_image_label = tk.Label(self.main_frame, image="", bg=BG_COLOR)
        self.user_image_label.place(x=80, y=100)

        self.computer_image_label = tk.Label(self.main_frame, image="", bg=BG_COLOR)
        self.computer_image_label.place(x=550, y=100)

        self.result_label = tk.Label(self.main_frame, text="", font="normal 10", width=15,
                                     borderwidth=2,relief="solid", bg=BG_COLOR)
        self.result_label.place(x=350, y=250)

        self.button_rock = tk.Button(self.main_frame, text=en["rock"], font=10, width=20, command=self.on_click_rock)
        self.button_scissors = tk.Button(self.main_frame, text=en["scissors"], font=10, width=20, command=self.on_click_scissors)
        self.button_paper = tk.Button(self.main_frame, text=en["paper"], font=10, width=20, command=self.on_click_paper)

        self.button_rock.place(x=100, y=300)
        self.button_scissors.place(x=300, y=300)
        self.button_paper.place(x=500, y=300)

    def on_click_rock(self) -> None:
        self._play_round(self.enum_rock)

    def on_click_scissors(self) -> None:
        self._play_round(self.enum_scissors)

    def on_click_paper(self) -> None:
        self._play_round(self.enum_paper)

    def _play_round(self, user_choice: Items) -> None:
        computer_choice: Items = random.choice(list(Items))
        self._update_user_image(user_choice)
        result_text, computer_image, color = self._decide_outcome(user_choice, computer_choice)
        self.result_label.config(text=result_text, bg=color)
        self.computer_image_label.config(image=computer_image)

    def _decide_outcome(self, user_choice: Items, computer_choice: Items) -> Tuple[str, tk.PhotoImage, ResultColors]:
        if user_choice == computer_choice:
            return en["tie"], self._image_for_choice(computer_choice), ResultColors.YELLOW

        if user_choice == self.enum_rock:
            if computer_choice == self.enum_paper:
                return en["computer_win"], self.paper_img, ResultColors.RED
            return en["human_win"], self.scissors_img, ResultColors.GREEN

        if user_choice == self.enum_scissors:
            if computer_choice == self.enum_rock:
                return en["computer_win"], self.rock_img, ResultColors.RED
            return en["human_win"], self.paper_img, ResultColors.GREEN

        if user_choice == self.enum_paper:
            if computer_choice == self.enum_scissors:
                return en["computer_win"], self.scissors_img, ResultColors.RED
            return en["human_win"], self.rock_img, ResultColors.GREEN

        return "", self._image_for_choice(computer_choice)

    def _image_for_choice(self, choice: Items) -> tk.PhotoImage:
        if choice == self.enum_rock:
            return self.rock_img
        if choice == self.enum_paper:
            return self.paper_img
        return self.scissors_img

    def _update_user_image(self, user_choice: Items) -> None:
        if user_choice == self.enum_rock:
            self.user_image_label.config(image=self.rock_img)
        elif user_choice == self.enum_paper:
            self.user_image_label.config(image=self.paper_img)
        else:
            self.user_image_label.config(image=self.scissors_img)


if __name__ == "__main__":
    app = RockPaperScissorsApp()
    app.mainloop()
