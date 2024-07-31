import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States game")
img = "blank_states_img.gif"
screen.addshape(img)
turtle.shape(img)

data = pandas.read_csv("50_states.csv")

guessed_state = []

while len(guessed_state) < 50:  # Changed to '<' to properly count states
    answer_state = turtle.textinput(f"{len(guessed_state)}/50 States Correct", "What's next state?").title()
    states = data.state.to_list()

    if answer_state == "Exit":
        break
    if answer_state in states:
        t = turtle.Turtle()
        t.hideturtle()
        t.up()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x.iloc[0]), int(state_data.y.iloc[0]))
        t.write(state_data.state.item())
        guessed_state.append(answer_state)

missed_states = []

for state in data.state:
    if state not in guessed_state:
        missed_states.append(state)

missed_states_dic = {
    "state": missed_states
}

new_data = pandas.DataFrame(missed_states)
new_data.to_csv("missed.csv")
