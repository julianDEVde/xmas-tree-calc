import math



def calc_cutting_length(thickness, beta):
    cutting_length = (thickness / math.sin(math.radians(beta))) * math.sin(math.radians(90))
    return cutting_length

def calc_base_width(height, beta, gamma, step_amount, thickness):
    base_width = 2 * (((height / math.sin(math.radians(beta))) * math.sin((math.radians(gamma) / 2))) - step_amount * calc_cutting_length(thickness, beta))
    return base_width

def calc_step_lengths(height, beta, overlap, step_amount, thickness):
    site = (height / math.sin(math.radians(beta))) * math.sin(math.radians(90))
    # Step a is the top step which overlaps the other top step

    # overlap * (step_amount - 1) #? is calculating the entire overlap
    # - calc_cutting_length(thickness, beta) / step_amount #? is there because the top step is alwas for the cutting_lenght longer
    #* Later you can choose between: For cutting_lenght longer / For % longer than the ground steps

    length_top_step_A = (site / 3) + ((((overlap * (step_amount - 1)) - calc_cutting_length(thickness, beta)) / 3) + calc_cutting_length(thickness, beta))
    length_top_step_B = (site / 3) + ((((overlap * (step_amount - 1)) - calc_cutting_length(thickness, beta)) / 3))
    ground_step_length = (site / 3) + (((overlap * (step_amount - 1)) - calc_cutting_length(thickness, beta)) / 3)
    return [length_top_step_A, length_top_step_B, ground_step_length]

# First calc test script with height, step_amount, overlap and thickness input
# The other parameters will be hard coded for this test script
beta = 60
gamma = 60

while True:
    try:
        height = int(input("Please insert the height of your tree in mm: "))
        step_amount = int(input("Please enter your amount of steps on one site as an integer: "))
        overlap = int(input("Please enter the length of your overlap in mm: "))
        thickness = int(input("Please enter the thickness of your wood in mm: "))
        step_lengths = [round(i, 2) for i in calc_step_lengths(height, beta, overlap, step_amount, thickness)]
        print(f"Base width: {round(calc_base_width(height, beta, gamma, step_amount, thickness), 2)} mm")
        print(f"Top step A length: {step_lengths[0]} mm")
        print(f"Top step B length: {step_lengths[1]} mm")
        print(f"Ground steps length: {step_lengths[2]} mm")
        break
    except ValueError:
        continue