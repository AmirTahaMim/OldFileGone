import os
import time

def main():

    dir_path = r"YourDirPath"
    hour = 3 #int
    loop_sleep_time = 1 #int

    delete_file(dir_path, hour)
    time.sleep(hour_to_Second(loop_sleep_time))

def delete_file(dir_path, hour):
    for file_name in os.listdir(dir_path):

        file_path = os.path.join(dir_path, file_name)

        if os.path.isfile(file_path):

            # get the current time ==> time.time() & creation_time ==> os.path.getctime(file_path)

            time_difference = time.time() - os.path.getctime(file_path)

            if time_difference > hour_to_Second(hour):
                os.remove(file_path)
                print(f"File {file_name} deleted.")
            else:
                print(f"File {file_name} is not older than 1 hour.")

def hour_to_Second(hour):
    return hour * 3600

main()
