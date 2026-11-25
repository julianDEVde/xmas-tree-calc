import math



def calc_cutting_length(thickness, beta):
    # The length of the side where the cut was made
    cutting_length = (thickness / math.sin(math.radians(beta))) * math.sin(math.radians(90))
    return cutting_length

def calc_base_width(height, beta, gamma, step_amount, thickness):
    # The base width, messured on the longest side
    base_width = 2 * (((height / math.sin(math.radians(beta))) * math.sin((math.radians(gamma) / 2))) - step_amount * calc_cutting_length(thickness, beta))
    return base_width

def calc_step_lengths(height, beta, overlap, step_amount, thickness, percent):
    # The complete length of on side on the tree 
    site = (height / math.sin(math.radians(beta))) * math.sin(math.radians(90))

    if percent == 0:
        # overlap * (step_amount - 1) #? is calculating the entire overlap length
        # - calc_cutting_length(thickness, beta) / step_amount #? is there because the top step is alwas for the cutting_lenght longer

        longer_top_step = (site / step_amount) + ((((overlap * (step_amount - 1)) - calc_cutting_length(thickness, beta)) / step_amount) + calc_cutting_length(thickness, beta))
        other_steps = (site / step_amount) + (((overlap * (step_amount - 1)) - calc_cutting_length(thickness, beta)) / step_amount)
        return [longer_top_step, other_steps]
    else:
        top_step_a = (site / ((step_amount - 1) * (1 - percent / 100) + 1))
        top_step_b = top_step_a + calc_cutting_length(thickness, beta)
        bottom_steps = top_step_a * (1 - percent / 100)
        return [top_step_a, top_step_b, bottom_steps]

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
        percent = int(input("Please enter the percentage by how much the top steps should be bigger as the bottom steps\n(leave empty for standart): ") or 0)
        step_lengths = [round(i, 2) for i in calc_step_lengths(height, beta, overlap, step_amount, thickness, percent)]
        print(f"Base width: {round(calc_base_width(height, beta, gamma, step_amount, thickness), 2)} mm")
        if percent == 0:
            print(f"Longer top step: {step_lengths[0]} mm")
            print(f"All other steps: {step_lengths[1]} mm")
        else:
            print(f"Top step A: {step_lengths[0]} mm")
            print(f"Top step B: {step_lengths[1]} mm")
            print(f"Bottom steps: {step_lengths[2]} mm")
        break
    except ValueError:
        continue