#this is how free code academy
def arithmetic_arranger(problems, show_answers=False):
    if len(problems) > 5:
        return "Error: Too many problems."

    top_row = []
    bottom_row = []
    dashes = []
    answers = []

    for problem in problems:
        parts = problem.split()
        if len(parts) != 3:
            return "Error: Invalid problem format."

        first, operator, second = parts

        if operator not in ['+', '-']:
            return "Error: Operator must be '+' or '-'."

        if not first.isdigit() or not second.isdigit():
            return "Error: Numbers must only contain digits."

        if len(first) > 4 or len(second) > 4:
            return "Error: Numbers cannot be more than four digits."

        width = max(len(first), len(second)) + 2
        top_row.append(first.rjust(width))
        bottom_row.append(operator + second.rjust(width - 1))
        dashes.append('-' * width)

        if show_answers:
            if operator == '+':
                result = str(int(first) + int(second))
            else:
                result = str(int(first) - int(second))
            answers.append(result.rjust(width))

    arranged_problems = '    '.join(top_row) + '\n' + \
                        '    '.join(bottom_row) + '\n' + \
                        '    '.join(dashes)

    if show_answers:
        arranged_problems += '\n' + '    '.join(answers)

    return arranged_problems

#this is why it took 2 days because I broke it into differen func for scalibility and free code did not like it
# def clean_up(list):
#     top_row =[]
#     mid_row =[]
#     operator =[]
#     counter =0
#     if len(list) <5:
#         while counter < len(list):
#             for operations in list:
#                 counter +=1
#                 clean_up =operations.split(' ')

#                 if len(clean_up[0]) and len(clean_up[2]) <4:
#                     try:
#                         top_row.append(clean_up[0])
#                         mid_row.append(clean_up[2])
#                         operator.append(clean_up[1])
#                     except ValueError:
#                         return 'Error: Numbers must only contain digits.'
#             else:
#                 'Error: Numbers cannot be more than four digits.'
#     return top_row,mid_row,operator


# def structure(fun_clean_data):
#     clean_data =clean_up(fun_clean_data)
#     top_row_num =clean_data[0]
#     bottom_row_num =clean_data[1]
#     operator =clean_data[2]
#     equal ='_'
#     join_bottom_row_num_wth_opeator =[op +' '  + num for op,num in zip(operator,bottom_row_num)]
#     colums_witdths =[max(len(top),len(bottom)) for top,bottom in zip(top_row_num,join_bottom_row_num_wth_opeator)]
#     top_line ='    '.join(top.rjust(width) for top,width in zip(top_row_num,colums_witdths))
#     bottom_line ='    '.join(bottom.rjust(width) for bottom,width in zip(join_bottom_row_num_wth_opeator,colums_witdths))
#     equal_line =equal_line = '    '.join(equal * width for width in colums_witdths)
#     return top_line,bottom_line,equal_line,colums_witdths


# def promblem_solver(problems):
#     probs =clean_up(problems)
#     answers =[]
#     for top,bottom,op in zip(probs[0],probs[1],probs[2]):
#         if op =='+':
#             answer =int(top) + int(bottom)
#             answers.append(answer)
#         elif op =='-':
#             answer =int(top) - int(bottom)
#             answers.append(answer)
#         else:
#             return "Error: Operator must be '+' or '-'."
#     return answers


# def arithmetic_arranger(problems, show_answers=False):
#     top_line,bottom_line,equal_line,column_widths=structure(problems)
#     answers =promblem_solver(problems)
#     if show_answers == True:
#         answer_line = '    '.join(str(ans).rjust(width) for ans, width in zip(answers, column_widths))
#         vetical_format =f'{top_line}\n{bottom_line}\n{equal_line}\n{answer_line}'
#         return vetical_format
#     else:
#         vetical_format =f'{top_line}\n{bottom_line}\n{equal_line}'
#         return vetical_format
# print(f'\n{arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])}')
