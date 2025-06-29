'''
Name: Rosa Pereira
Date: December 19, 2024

Description:
This program examines a wireShark.txt file in a line by line logic
with the purpose of extracting frame numbers, source (Src) and
destination (Dst) in MAC address format, and frame type. The output
results in the critical information displayed in an organized pattern.
This code can be used to extract the specified information from any 
WireShark capture in .txt format.
'''

def read_file(filename):
    '''
    Reads file, processes the entire file and returns each line as a list.
    Parameters:
    filename: str, file path.
    returns a list of strings.
    '''
    inputfile = open(filename, "r", encoding="utf-8") # open file
    lines = inputfile.readlines() # read lines into a list
    inputfile.close()
    return lines

def find_frame(line):
    '''
    Finds the frame number data.
    Parameters:
    line: str, line of text from the txt file.
    returns the frame number or none if the string is not found.
    '''
    if line.startswith("Frame"): # checks for "Frame"
        parts = line.split() # splits line to get the frame number
        return parts[1].strip(":") # remove :
    return None

def find_addresses(line):
    '''
    Finds Src and Dst MAC addresses.
    Parameters:
    line: str, line of text from the txt file.
    returns Src and Dst MAC addresses through the use of a tuple.
    '''
    def find_mac(substring):
        '''
        Extracts MAC found inside a parenthesis
        Parameters:
        substring: str, part of a line that contains a MAC address
        returns the MAC address if it is within the parameters, otherwise None.
        '''
        start = substring.find("(") + 1 # finds MAC within ()
        end = substring.find(")", start)
        if start > 0 and end > start: # checks valid MAC format and ()
            mac_address = substring[start:end]
            if mac_address.count(":") == 5: # checks for 5 :'s for MAC
                return mac_address
        return None
    if "Src:" in line: # checks for Src MAC
        return find_mac(line), None
    if "Dst:" in line or "Destination:" in line: # checks for Dst MAC
        return None, find_mac(line)
    return None, None

def find_type(line):
    '''
    Finds the type
    Parameters:
    line: str, line of text from the txt file.
    returns the frame type in the required format, otherwise None.
    '''
    if "Type:" in line: # checks for "Type:"
        type_info = line.split("Type: ")[1].strip()
        hex_type = type_info.split(" ")[-1] # gets hexadecimal type
        return hex_type.replace("(", "").replace(")", "") # takes () out
    return None

def parsing_each_frame(lines):
    '''
    Examines the lines of the txt file to find the specified details
    Parameters:
    lines: list, lists lines from the file as strings.
    returns list of dictionaries (frames) with keys ("number", "src", "dst", and "type")
    '''
    frames = [] # empty list to place frame details
    frame_info = {"number": None, "src": None, "dst": None, "type": None}
    for line in lines: # loop through lines
        frame_number = find_frame(line) # get frames from line
        if frame_number: # when a new frame is found save it and start new
            if frame_info["number"]: # save if frame is NOT empty
                frames.append(frame_info)
            frame_info = {"number": frame_number, "src": None, "dst": None, "type": None} # start new frame
        src, dst = find_addresses(line) # find Src and Dst MAC
        if src:
            frame_info["src"] = src
        if dst:
            frame_info["dst"] = dst
        frame_type = find_type(line) # find frame type
        if frame_type:
            frame_info["type"] = frame_type
    if frame_info["number"]: # after loop ends, append frame
        frames.append(frame_info)
    return frames

def frame_output(frames):
    '''
    Outputs the desired string format
    Parameters:
    frames: list, list of dictionaries
    '''
    for frame in frames: # loop through the frames and print out the required details in the specified format
        print("Frame " + frame['number'] + ", Src:" + str(frame['src']) + ", Des:" + str(frame['dst']) + ", Type:" + str(frame['type']))

#===================================================================================================================

def main():
    '''
    This is where we read, parse, and output the specified data from
    the wireShark.txt file.
    '''
    lines = read_file("wireShark.txt") # type your file name here
    frames = parsing_each_frame(lines) # parse frames
    frame_output(frames) # output
if __name__ == "__main__":
    main()
