from sentence_extractor import extract_category_items
# Lists storing fitness data
workouts = {'asd': 5}  # To store workout types and durations in minutes
calories = [50]  # To store calorie intake

# Variables for daily goals
workout_goal = 0  # Daily workout goal in minutes
calorie_goal = 0  # Daily calorie intake goal


def log_workout(workout_type, duration):
    """
    - Adding workout and duration in minutes inside the dictionary
    - Confirmation message
    """
    if workout_type not in workouts:
        workouts[workout_type] = duration
        return f'Your workout has been added.\nExercise: {workout_type}; Duration: {duration}'

    workouts[workout_type] += duration
    return f'Exercise: {workout_type} Added duration: {duration}"min"'


def log_calorie_intake(calories_consumed):
    calories.append(calories_consumed)
    """
    - Calories added to list
    - Confirmation message
    """
    return f'Calories added {calories_consumed}'


def view_progress():
    """
    - Calculate the total workout time and total calories.
    - Print feedback
    """
    all_workout_sum = len(workouts)
    all_workout_duration = sum(workouts.values())
    daily_calories = sum(calories)
    workout_display = f'You have done {all_workout_sum} exercises and {all_workout_duration} min of working out.'
    calories_display = f'You have consumed {daily_calories} calories today.'

    return workout_display, calories_display


def reset_progress(clear_input):
    """
    - Clear input 1 clears workouts. Clear input 2 clears calories. Clear input 3 clears everything.
    - Clear date input and return message
    """
    if clear_input == 1:
        workouts.clear()
        return f'Workouts have been cleared!'
    elif clear_input == 2:
        calories.clear()
        return f'Calories have been cleared!'
    elif clear_input == 3:
        workouts.clear()
        calories.clear()
        return f'Both workouts and calories have been cleared!'


def set_daily_goals(workout_minutes_goal=None, calorie_limit_goal=None):
    if workout_minutes_goal is not None:
        workout_goal = workout_minutes_goal
    elif calorie_limit_goal is not None:
        calorie_goal = calorie_limit_goal
    """
    Set daily goals for workout time and calorie intake.
    - Update the global variables workout_goal and calorie_goal.
    - Print a confirmation message.
    """
    return f'Your goals have been set. Workout goal {workout_goal} minutes/ Calorie goal {calorie_goal}'


def calculate_goal_completion():
    """
    Comparing workout done to goals and setting a variable(goal_completion)
    which will be used to find the correct inspirational message from the Word file
    """
    goal_completion = ''
    workout_duration_completed = sum(workouts.values())
    if workout_duration_completed < (workout_goal / 2):
        goal_completion = 'Beginning'
    elif workout_duration_completed >= (workout_goal / 2) and workout_duration_completed < workout_goal:
        goal_completion = 'Half-done'
    elif workout_duration_completed >= workout_goal:
        goal_completion = 'Finished'
    return goal_completion


def encouragement_system():
    """
    -Calling function from (file.name) that extracts inspirational message from the Word file database.
    -Returning the sentence as a string
    """
    goal_completion = calculate_goal_completion()
    encouragement_sentence = extract_category_items('encouragment_database.docx', goal_completion)
    return encouragement_sentence


def check_if_string(menu_choice=None, wor_cal_check=None, res_progress_input=None, goal_choice_input=None, goal_input=None):
    """
    - Checks if the input is a string
    - Return the number if it is int
    """
    if menu_choice is not None:  # Main menu
        while True:
            try:
                menu_choice = int(menu_choice)
                if menu_choice not in (1, 2, 3, 4, 5, 6, 7):
                    menu_choice = input('Invalid number. Available choices:')
                else:
                    return menu_choice

            except ValueError:
                menu_choice = input('Invalid input. Please choose a number:')
    elif wor_cal_check is not None:  # View progress
        while True:
            try:
                wor_cal_check = int(wor_cal_check)
                if wor_cal_check not in (1, 2, 3):
                    wor_cal_check = input('Invalid number!\nEnter your choice:')
                else:
                    return wor_cal_check

            except ValueError:
                wor_cal_check = input('Please choose a number:')
    elif res_progress_input is not None:  # Reset progress
        while True:
            try:
                res_progress_input = int(res_progress_input)
                if res_progress_input not in (1, 2, 3):
                    res_progress_input = input('Please choose between 1, 2, 3.\nYour choice:')
                else:
                    return res_progress_input

            except ValueError:
                print('Please write a number')
                res_progress_input = input('Your choice:')
    elif goal_choice_input is not None:  # Goal choice
        while True:
            try:
                goal_choice_input = int(goal_choice_input)
                if goal_choice_input not in (1, 2):
                    goal_choice_input = input('Invalid number.\nYour Choice:')
                else:
                    return goal_choice_input

            except ValueError:
                goal_choice_input = input('Invalid input. Please choose a number:')
    elif goal_input is not None:  # Goal input
        while True:
            try:
                goal_input = int(goal_input)
                return goal_input
            except ValueError:
                goal_input = input('Please enter a number:')


def main():
    """
    Main function to interact with the user.
    """
    print("Welcome to the Personal Fitness Tracker System 🏋️‍♂️\n")

    while True:
        # Display menu
        print("1. Log Workout")
        print("2. Log Calorie Intake")
        print("3. View Progress")
        print("4. Reset Progress")
        print("5. Set Daily Goals")
        print("6. Compare Workout To Goals")
        print("7. Exit")

        # Prompt user for their choice
        choice = input("\nEnter your choice:")
        choice = check_if_string(menu_choice=choice)

        if choice == 1:  # Log Workout
            print('Input type and duration of exercise in min:')
            workout = input('Exercise:')
            duration = int(input('Duration:'))
            print(log_workout(workout, duration))

        elif choice == 2:  # Log Calorie Intake
            calories_taken = input('Add amount of calories taken:')
            log_calorie_intake(calories_taken)

        elif choice == 3:
            # View progress
            workout_encouragement, calories_encouragement = view_progress()
            print('1. Workouts\n2. Calories\n3. Both')
            stats_choice = input('Enter your choice:')
            show_stats = check_if_string(wor_cal_check=stats_choice)

            if show_stats == 1:
                if workouts:
                    for exercise, time in workouts.items():
                        print(f'{exercise} : {time} min')
                    print(workout_encouragement)
                else:
                    print('There are no workouts done for today')

            elif show_stats == 2:
                if calories:
                    print(calories_encouragement)
                else:
                    print('There are no calories added yet.')

            elif show_stats == 3:
                if workouts and calories:
                    for exercise, time in workouts.items():
                        print(f'{exercise} : {time} min')
                    print(workout_encouragement)
                    print(calories_encouragement)

                else:
                    print('There are either no workouts or calories added.')

        elif choice == 4:
            # Call reset_progress function
            print('Reset Progress:')
            clear_progress_input = input('1. Clear Workouts\n2. Clear Calories\n3. Clear Both\nYour choice:')
            clear_progress_input = check_if_string(res_progress_input=clear_progress_input)
            print(reset_progress(clear_progress_input))

        elif choice == 5:
            # Set daily goals
            work_cal_choice = input('Set daily goals:\n1. Workouts\n2. Calories\nYour Choice:')
            work_cal_choice = check_if_string(goal_choice_input=work_cal_choice)
            if work_cal_choice == 1:
                workout_goal_new = input('Workout goal:')
                check_if_string(goal_input=workout_goal_new)
                print(f'You workout goal has been set to {workout_goal} min.')
            elif work_cal_choice == 2:
                calorie_goal_new = input('Calories goal:')
                check_if_string(goal_input=calorie_goal_new)
                print(f'Your calorie goal has bene set to {calorie_goal}.')

        elif choice == 6:
            # Compare workout to goals
            workouts_sum = sum(workouts.values())
            print(f'Your current workout is: {workouts_sum}min and your goal is {workout_goal} min')
            print(encouragement_system())

        elif choice == 7:
            # Goodbye message and breaking loop
            print("Thank you for using the Fitness Tracker. Stay healthy! 💪")
            break
        else:
            print("Invalid choice, please try again.")


if __name__ == "__main__":
    main()
