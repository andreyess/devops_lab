# Module logger
import psutil
import json
import datetime
import time
import threading
import argparse
from os.path import isdir


class SystemStateLogger:
    ''' This class is used to make system-state snapshots.
    The main two functions are: start_threading_task and stop_threading_task.

    All main things happens in function __start_making_snapshots.
    This function is protected and can be called only by start_threading_task function.
    It runs in the other thread (not in main), what allows us to execute some other code
    in the main thread, when the logger-thread is sleeping.
    stop_threading_task method sends the "request" to logging thread,
    and waits to end of it (it needs to end sleeping-process to close the thread correctly).
    After stop_threading_task execution we can start one another thread.
    At the time, we can run only one logging-thread.

    Here are the command-line arguments:
        -p - period between system-state logging in seconds. Default - 300 seconds.
        -t - type of output. Allowed values are: JSON and text. Default - JSON.
        -m - path to the directory, which will be used to describe memory-parameter. Default -"/".

    All output will be stored in snapsht.log file in your current directory.
    '''

    __DEFAULT_PERIOD = 300
    __DEFAULT_PATH = "snapshot.log"

    def __init__(self):
        self.__is_thread_working = False
        self.__thread_stop_it_please = False

    def __get_cpu_load(self):
        return psutil.cpu_percent()

    def __get_memory_usage(self, memory_usage_path):
        return psutil.disk_usage(memory_usage_path)

    def __get_virtual_memory_usage(self):
        return psutil.virtual_memory()

    def __get_io_information(self):
        return psutil.disk_io_counters()

    def __get_network_information(self):
        return psutil.net_io_counters()

    def get_current_info(self, memory_usage_path, is_json_format):
        if is_json_format:
            snapshot_dict = {
                'CPU': self.__get_cpu_load(),
                'MEM': self.__get_memory_usage(memory_usage_path),
                'VMEM': self.__get_virtual_memory_usage(),
                'IO': self.__get_io_information(),
                'NET': self.__get_network_information()
            }
            return json.dumps(snapshot_dict)
        else:
            return "{},{},{},{},{}".format(
                self.__get_cpu_load(), self.__get_memory_usage(memory_usage_path),
                self.__get_virtual_memory_usage(), self.__get_io_information(),
                self.__get_network_information())

    def __start_making_snapshots(
            self, sleep_period, is_json_format,
            path_to_store, memory_usage_path):

        writes_counter = 1

        while not self.__thread_stop_it_please:
            with open(path_to_store, 'a') as file:
                file.write("SNAPSHOT {}: {}: {}\n".format(
                    writes_counter, datetime.datetime.now(),
                    self.get_current_info(memory_usage_path, is_json_format)))

            writes_counter += 1
            time.sleep(sleep_period)

        self.__is_thread_working = self.__thread_stop_it_please = False

    def start_threading_task(
            self, sleep_period=__DEFAULT_PERIOD, is_json_format=False,
            path_to_store=__DEFAULT_PATH, memory_usage_path="/"):

        if not self.__is_thread_working:
            self.__snapshot_thread = threading.Thread(
                target=self.__start_making_snapshots,
                args=[sleep_period, is_json_format, path_to_store, memory_usage_path])
            self.__snapshot_thread.start()

            self.__is_thread_working = True
            return True
        else:
            return False

    def stop_threading_task(self):
        if self.__is_thread_working:
            self.__thread_stop_it_please = True
            self.__snapshot_thread.join()

            return True
        else:
            return False


def snapshoot():
    parser = argparse.ArgumentParser(description='Arguments for sys-snapshooter')

    parser.add_argument(
        '-p', default=300, type=int,
        help="Input here a priod between the snapshots. Default value is 300s")
    parser.add_argument(
        '-t', default='JSON', type=str,
        help="Input here an output-type. Possible values are: JSON and text")
    parser.add_argument(
        '-m', type=str, default='/',
        help='Input here directory, which will be checked and displayed by snapshooter')

    cmd_args = parser.parse_args()
    if cmd_args.p <= 0 or cmd_args.t not in ('JSON', 'text') or not isdir(cmd_args.m):
        print('Bad input of command-line arguments. Try to tap --help to see the script-interface.')
    else:
        logger = SystemStateLogger()
        logger.start_threading_task(
            cmd_args.p, True if cmd_args.t == 'JSON' else False,
            memory_usage_path=cmd_args.m)


if __name__ == "__main__":
    snapshoot()
