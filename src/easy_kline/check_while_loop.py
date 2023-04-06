import inspect
import linecache
import re


import sys
def while_loop_checker_and_arg_var_giver():
    # 1. Get the current frame
    current_frame = inspect.currentframe()
    outer_frames = inspect.getouterframes(current_frame)[1:]
    num_lines = sum(frame[2] for frame in outer_frames)

    # 2. Get the previous frame (which should be the frame of the calling function)
    previous_frame = current_frame.f_back

    # 3. Get the line number of the previous frame
    
    for i in range(1 ,num_lines,1):
        previous_lineno = previous_frame.f_lineno - i

    # 4. Get the filename of the previous frame
        previous_filename = previous_frame.f_globals["__file__"]

    # 5. Get the previous line of code
        previous_line = linecache.getline(previous_filename, previous_lineno).strip()
        # if 'while' in previous_line:
        #     sys.stdout.write("\033[K")
        #     sys.stdout.write('\r')

        if 'easy_klinee.bybit' in previous_line :

            
            arg = re.findall( r"'(.*?)'" , previous_line)
            match = re.search(r'.*(?=\=)', previous_line)
            if match :
                var_name = match.group(0).strip()
            

            break
    return arg 


# h=5

# while True :
#     break


# g=54
# c = 33
# while_loop_and_arg_checker()
