import number_program_input

def split_and_convert(input_string):
	split_string = list(input_string)
	for i in range(len(split_string)):
		split_string[i] = number_program_input.chinese_character_to_arabic_number(split_string[i])
	return split_string

def multiply(list):
	output = [list]
	hold_variable = None
	output_try = 1
	while output_try >= 1:
		output.append([])
		for num in output[output_try-1]:
			if hold_variable == None:
				if num < 10000:
					hold_variable = num
				else:
					output[output_try].append(num)
			else:
				if num < 10000:
					if hold_variable < num:
						output[output_try].append(hold_variable*num)
						hold_variable = None
					else:
						output[output_try].append(hold_variable)
						output[output_try].append(num)
						hold_variable = None
				else:
					output[output_try].append(hold_variable)
					output[output_try].append(num)
					hold_variable = None
		if hold_variable != None:
			output[output_try].append(hold_variable)
			hold_variable = None
		if output_try > 1:
			if output[output_try] == output[output_try-1]:
				output_try = 0
			else:
				output_try += 1
		else:
			output_try += 1
	return output[-1]

def add(list):
	output = [list]
	hold_variable = None
	output_try = 1
	while output_try >= 1:
		output.append([])
		for num in output[output_try-1]:
			if hold_variable == None:
				if num < 10000:
					hold_variable = num
				else:
					output[output_try].append(num)
			else:
				if num < 10000:
					if hold_variable > num and hold_variable < 10000:
						output[output_try].append(hold_variable+num)
						hold_variable = None
					else:
						output[output_try].append(hold_variable)
						output[output_try].append(num)
						hold_variable = None
				else:
					output[output_try].append(hold_variable)
					output[output_try].append(num)
					hold_variable = None
		if hold_variable != None:
			output[output_try].append(hold_variable)
			hold_variable = None
		if output_try > 1:
			if output[output_try] == output[(output_try-1)]:
				output_try = 0
			else:
				output_try += 1
		else:
			output_try += 1
	return output[-1]

def multiply_big(list):
	output = []
	i = 0
	while i < len(list):
		if i != (len(list)-1):
			output.append(list[i]*list[i+1])
			i += 2
		else:
			output.append(list[i])
			i += 1
	return output

def add_big(list):
	output = 0
	i = 0
	while i < len(list):
		output += list[i]
		i += 1
	return output

def main(input_string):
	split_string = split_and_convert(input_string)
	output1 = multiply(split_string)
	output2 = add(output1)
	output3 = multiply_big(output2)
	output4 = add_big(output3)
	print(output4)

main(number_program_input.sample_chinese_number_strings[0])
