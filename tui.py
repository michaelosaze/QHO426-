def get_selected_make(allmakes):
    make =""
    while make.upper()  not in allmakes:
        print("please enter a valid make")
        make = input()
    return make
def get_selected_state(allstates):
    state =""
    while state.upper() not in allstates:
        print("please enter a valid state")
        state = input()