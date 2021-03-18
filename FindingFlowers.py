# code that finds number of non-consecutive occurances of flower names in a given sentence. 

flowerList = ["rose", "lily", "jasmine", "sunflower", "tulip", "orchid"]
og_userInput = "For those who work hard, should triumph finally. Roses and Tulips are red but rose is more red"

userInput =  og_userInput.lower()
userInput_list = list(userInput)

flower_count_indx = 0
flowerCount = [0, 0, 0, 0, 0, 0]

for flower in flowerList:
    # flower character index
    fl_ch_indx = 0
    word_len = 0
    current_inp_indx = 0

    while (fl_ch_indx < len(flower)):
        # getting character from flower
        ch_fl = flower[fl_ch_indx]

        inp_indx = current_inp_indx

        while inp_indx < len(userInput_list):
            ch_in = userInput_list[inp_indx]
            current_inp_indx += 1

            if ch_fl == ch_in:
                word_len += 1
                userInput_list.pop(inp_indx)
                current_inp_indx -= 1

                if word_len == len(flower):
                    word_len = 0
                    flowerCount[flower_count_indx] += 1
                    fl_ch_indx = -1
                    current_inp_indx = 0
                break

            inp_indx += 1

        fl_ch_indx += 1

    userInput_list = list(userInput)
    flower_count_indx += 1

print("User Input : ", og_userInput)
i = 0
for flower in flowerList:
    print(flower, ":", flowerCount[i])
    i += 1
