import tkinter as tk
import turtle
import time


class PushdownAutomaton:
    def __init__(self):
        self.stack = []

    def push(self, symbol, turtle):
        self.stack.append(symbol)
        self.display_push(turtle, symbol)

    def pop(self, turtle):
        if len(self.stack) > 0:
            popped_symbol = self.stack.pop()
            self.display_pop(turtle, popped_symbol)
            return popped_symbol
        else:
            return None

    def is_empty(self):
        return len(self.stack) == 0

    def validate_parentheses(self, input_string, turtle):
        self.push("Zo", turtle)  # Push "Zo" initially
        for symbol in input_string:

            if symbol == "(" or symbol == "{" or symbol == "[":
                self.push(symbol, turtle)
            elif symbol == ")" and self.stack[-1] == "(":
                if self.pop(turtle) is None:
                    return False
            elif symbol == "}" and self.stack[-1] == "{":
                if self.pop(turtle) is None:
                    return False
            elif symbol == "]" and self.stack[-1] == "[":
                if self.pop(turtle) is None:
                    return False

            elif symbol == ")" and self.stack[-1] == "Zo":
                return False
            elif symbol == "}" and self.stack[-1] == "Zo":
                return False
            elif symbol == "]" and self.stack[-1] == "Zo":
                return False

        return self.stack[-1] == "Zo"  # Check if top is "Zo"

    def display_push(self, turtle, symbol):
        turtle.penup()
        turtle.goto(-200, 0)
        turtle.pendown()
        turtle.write("Push: " + symbol, font=("Arial", 12, "normal"))
        turtle.penup()
        turtle.goto(-200, -20)
        turtle.pendown()
        turtle.write("Stack: " + "".join(self.stack), font=("Arial", 12, "normal"))
        turtle.penup()
        turtle.goto(-200, -40)
        turtle.pendown()
        turtle.write(
            "------------------------------------", font=("Arial", 12, "normal")
        )
        time.sleep(1)
        turtle.clear()

    def display_pop(self, turtle, symbol):
        turtle.penup()
        turtle.goto(-200, 0)
        turtle.pendown()
        turtle.write("Pop: " + symbol, font=("Arial", 12, "normal"))
        turtle.penup()
        turtle.goto(-200, -20)
        turtle.pendown()
        turtle.write("Stack: " + "".join(self.stack), font=("Arial", 12, "normal"))
        turtle.penup()
        turtle.goto(-200, -40)
        turtle.pendown()
        turtle.write(
            "------------------------------------", font=("Arial", 12, "normal")
        )
        time.sleep(1)
        turtle.clear()


class GUIPushdownAutomaton:
    def __init__(self, master):
        self.master = master
        self.master.title("Pushdown Automaton for Valid Parentheses")
        self.master.geometry("400x200")  # Set window size

        self.input_label = tk.Label(
            master, text="Enter Parentheses String:", font=("Helvetica", 12)
        )
        self.input_label.pack()

        self.input_entry = tk.Entry(
            master, font=("Helvetica", 12), width=30
        )  # Increase width
        self.input_entry.pack()

        self.validate_button = tk.Button(
            master, text="Validate", font=("Helvetica", 12), command=self.validate
        )
        self.validate_button.pack()

        self.result_label = tk.Label(
            master, text="", font=("Helvetica", 14, "bold")
        )  # Increase font size and make bold
        self.result_label.pack()

    def validate(self):
        input_string = self.input_entry.get()
        pda = PushdownAutomaton()
        screen = turtle.Screen()
        screen.setup(width=800, height=400)
        screen.tracer(0)
        turtle.penup()
        turtle.hideturtle()
        if pda.validate_parentheses(input_string, turtle):
            self.result_label.config(
                text="Valid Parentheses", fg="green"
            )  # Set text color to green for valid
        else:
            self.result_label.config(
                text="Invalid Parentheses", fg="red"
            )  # Set text color to red for invalid
        screen.update()
        tk.mainloop()


def main():
    root = tk.Tk()
    gui = GUIPushdownAutomaton(root)


if __name__ == "__main__":
    main()
    tk.mainloop()



