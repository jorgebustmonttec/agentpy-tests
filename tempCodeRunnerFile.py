parameters={
    'dimensions': 16,  # Dimensions of the grid, minimum 4
    'steps': 20,  # Number of steps to run the model
    'max_cars': 3, # Maximum number of cars
    'spawn_rate': 1, # Rate of car spawn, chance of car spawn per step 
    'chance_run_yellow_light': 0.5, # Chance of running a yellow light
    'chance_run_red_light': 0.5, # Chance of running a red light
}

print(run_intersection_model(parameters))