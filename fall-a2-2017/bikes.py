""" CSC108 Assignment 2 Starter code """

from typing import List, TextIO

# A set of constants, each representing a list index for station information.
ID = 0
NAME = 1
LATITUDE = 2
LONGITUDE = 3
CAPACITY = 4
BIKES_AVAILABLE = 5
DOCKS_AVAILABLE = 6
IS_RENTING = 7
IS_RETURNING = 8

####### BEGIN HELPER FUNCTIONS ####################

def is_number(value: str) -> bool:
    """Return True if and only if value represents a decimal number.

    >>> is_number('csc108')
    False
    >>> is_number('  108 ')
    True
    >>> is_number('+3.14159')
    True
    """

    return value.strip().lstrip('-+').replace('.', '', 1).isnumeric()


# It isn't necessary to call this function to implement your bikes.py
# functions, but you can use it to create larger lists for testing.
# See the main block below for an example of how to do that.
def csv_to_list(csv_file: TextIO) -> List[List[str]]:
    """Read and return the contents of the open CSV file csv_file as a list of
    lists, where each inner list contains the values from one line of csv_file.

    Docstring examples not given since results depend on data to be input.
    """

    # Read and discard header.
    csv_file.readline()

    data = []
    for line in csv_file:
        data.append(line.strip().split(','))
    return data


####### END HELPER FUNCTIONS ####################

### SAMPLE DATA TO USE IN DOCSTRING EXAMPLES ####

SAMPLE_STATIONS = [
    [7087, 'Danforth/Aldridge', 43.684371, -79.316756, 23, 9, 14, True, True],
    [7088, 'Danforth/Coxwell', 43.683378, -79.322961, 15, 13, 2, False, False]]

HANDOUT_STATIONS = [
    [7000, 'Ft. York / Capreol Crt.', 43.639832, -79.395954, 31, 20, 11, True, True],
    [7001, 'Lower Jarvis St / The Esplanade', 43.647992, -79.370907,
     15, 5, 10, True, True]]

#########################################

def clean_data(data: List[list]) -> None:
    """Convert each string in data to an int if and only if it represents a
    whole number, a float if and only if it represents a number that is not a
    whole number, True if and only if it is 'True', False if and only if it is
    'False', and None if and only if it is either 'null' or the empty string.

    >>> d = [['abc', '123', '45.6', 'True', 'False']]
    >>> clean_data(d)
    >>> d
    [['abc', 123, 45.6, True, False]]
    >>> d = [['ab2'], ['-123'], ['False', '3.2']]
    >>> clean_data(d)
    >>> d
    [['ab2'], [-123], [False, 3.2]]
    """
    for d in data:
        for i, x in enumerate(d):
            if is_number(x):
                if '.' not in x:
                    d[i] = int(x)
                else:
                    d[i] = float(x)
            elif x == 'True':
                d[i] = True
            elif x == 'False':
                d[i] = False


def get_station_info(station_id: int, stations: List[list]) -> list:
    """Return a list containing the following information from stations
    about the station with id number station_id:
        - station name
        - number of bikes available
        - number of docks available
    (in this order)

    Precondition: station_id will appear in stations.

    >>> get_station_info(7087, SAMPLE_STATIONS)
    ['Danforth/Aldridge', 9, 14]
    >>> get_station_info(7088, SAMPLE_STATIONS) 
    ['Danforth/Coxwell', 13, 2]
    """
    #采用线性搜索方式进行搜索
    
    #遍历列表
    for station in stations:
        #若寻找到相应的station_id
        if station[ID] == station_id:
            #则按要求返回station_id对应列表元素，提取其中的数据
            return [station[NAME], station[BIKES_AVAILABLE], station[DOCKS_AVAILABLE]]


def get_total(index: int, stations: List[list]) -> int:
    """Return the sum of the column in stations given by index.

    Precondition: the items in stations at the position
                  that index refers to are ints.

    >>> get_total(BIKES_AVAILABLE, SAMPLE_STATIONS)
    22
    >>> get_total(DOCKS_AVAILABLE, SAMPLE_STATIONS)
    16
    """
    #累加
    x = 0
    #遍历列表
    for station in stations:
        x = x + station[index]
    return x 
        
        


def get_station_with_max_bikes(stations: List[list]) -> int:
    """Return the station ID of the station that has the most bikes available.
    If there is a tie for the most available, return the station ID that appears
    first in stations.

    Precondition: len(stations) > 0

    >>> get_station_with_max_bikes(SAMPLE_STATIONS)
    7088
    """
    #比较最大值
    x = 0
    y = 0
    for station in stations:
        if station[BIKES_AVAILABLE] > x:
            x = station[BIKES_AVAILABLE]
            y = station[ID]
    
    return y 
        

def get_stations_with_n_docks(n: int, stations: List[list]) -> List[int]:
    """Return a list containing the station IDs for the stations in stations
    that have at least n docks available, in the same order as they appear
    in stations.

    Precondition: n >= 0

    >>> get_stations_with_n_docks(2, SAMPLE_STATIONS)
    [7087, 7088]
    >>> get_stations_with_n_docks(5, SAMPLE_STATIONS)
    [7087]
    """

    y = []
    for station in stations:
        if station[DOCKS_AVAILABLE] >= n:
            y.append(station[ID])
    return y


def get_direction(start_id: int, end_id: int, stations: List[list]) -> str:
    """ Return a string that contains the direction to travel to get from
    station start_id to station end_id according to data in stations.

    Precondition: start_id and end_id will appear in stations.

    >>> get_direction(7087, 7088, SAMPLE_STATIONS)
    'SOUTHWEST'
    """
    
    #多伦多是位于北纬、西经 43°40'N，79°25'W 。位于西、北半球

    # 同在北半球的，纬度高的点在纬度低点的正北。同在南半球的，纬度低的点在纬度高点的正北。

    # 根据两地经度数判读其东西方向
    #   1．两个相比较的地点同是东经，则经度数值大的在东面，经度数值小的在西面。
    #   2．两个相比较的地点同是西经，则经度数值小的在东面，经度数值大的在西面。
    #   3．两个相比较的地点分别为东经和西经时，要用两地经度之和来辨认东西方位：
    #       (1)若两地经度和小于180，则东经度的地点在东面。西经度的地点在西面；
    #       (2)若两地经度和大于180，则西经度的地点在东面．东经度的地点在西面；
    #       (3)若两地经度之和等于180，则两地分别位于两条正相对的经线上，
    #          说哪—点在东，哪—点在西均可，此种情况比不出东西方向。

    #取出两个点
    for station in stations:
        if station[ID] == start_id:
            p1 = (station[LATITUDE], station[LONGITUDE])
        if station[ID] == end_id:
            p2 = (station[LATITUDE], station[LONGITUDE])
    
    #比较两个点经纬度大小
    #先比较纬度, 以end_id, p2为基准来判定方向
    if p2[0] < p1[0]:
        #p2在p1的正南
        d1 = 'SOUTH'
    else:
        #p2在p1的正北
        d1 = 'NORTH'

    #比较两个点的经度    
    if abs(p2[1]) < abs(p1[1]):
        #p2在p1的东面
        d2 = 'EAST'
    else:
        d2 = 'WEST'

    return d1 + d2 


def rent_bike(station_id: int, stations: List[list]) -> bool:
    """Update the available bike count and the docks available count
    for the station in stations with id station_id as if a single bike was
    removed, leaving an additional dock available. Return True if and only
    if the rental was successful.

    Precondition: station_id will appear in stations.

    >>> station_id = SAMPLE_STATIONS[0][ID]
    >>> original_bikes_available = SAMPLE_STATIONS[0][BIKES_AVAILABLE]
    >>> original_docks_available = SAMPLE_STATIONS[0][DOCKS_AVAILABLE]
    >>> rent_bike(station_id, SAMPLE_STATIONS)
    True
    >>> original_bikes_available - 1 == SAMPLE_STATIONS[0][BIKES_AVAILABLE]
    True
    >>> original_docks_available + 1 == SAMPLE_STATIONS[0][DOCKS_AVAILABLE]
    True
    >>> station_id = SAMPLE_STATIONS[1][ID]
    >>> original_bikes_available = SAMPLE_STATIONS[1][BIKES_AVAILABLE]
    >>> original_docks_available = SAMPLE_STATIONS[1][DOCKS_AVAILABLE]
    >>> rent_bike(station_id, SAMPLE_STATIONS)
    False
    >>> original_bikes_available == SAMPLE_STATIONS[1][BIKES_AVAILABLE]
    True
    >>> original_docks_available == SAMPLE_STATIONS[1][DOCKS_AVAILABLE]
    True
    """
    #遍历
    for station in stations:
        #找到ID
        if station[ID] == station_id:
            if station[BIKES_AVAILABLE] >= 1 and station[IS_RENTING]:
                station[BIKES_AVAILABLE] -= 1
                station[DOCKS_AVAILABLE] += 1
                return True
    return False 
                




def return_bike(station_id: int, stations: List[list]) -> bool:
    """Update the available bike count and the docks available count
    for station in stations with id station_id as if a single bike was added,
    making an additional dock unavailable. Return True if and only if the
    return was successful.

    Precondition: station_id will appear in stations.

    >>> station_id = SAMPLE_STATIONS[0][ID]
    >>> original_bikes_available = SAMPLE_STATIONS[0][BIKES_AVAILABLE]
    >>> original_docks_available = SAMPLE_STATIONS[0][DOCKS_AVAILABLE]
    >>> return_bike(station_id, SAMPLE_STATIONS)
    True
    >>> original_bikes_available + 1 == SAMPLE_STATIONS[0][BIKES_AVAILABLE]
    True
    >>> original_docks_available - 1 == SAMPLE_STATIONS[0][DOCKS_AVAILABLE]
    True
    >>> station_id = SAMPLE_STATIONS[1][ID]
    >>> original_bikes_available = SAMPLE_STATIONS[1][BIKES_AVAILABLE]
    >>> original_docks_available = SAMPLE_STATIONS[1][DOCKS_AVAILABLE]
    >>> return_bike(station_id, SAMPLE_STATIONS)
    False
    >>> original_bikes_available == SAMPLE_STATIONS[1][BIKES_AVAILABLE]
    True
    >>> original_docks_available == SAMPLE_STATIONS[1][DOCKS_AVAILABLE]
    True
    """
    for station in stations:
        if station[ID] == station_id:
            if station[DOCKS_AVAILABLE] >= 1 and station[IS_RETURNING]:
                station[BIKES_AVAILABLE] += 1
                station[DOCKS_AVAILABLE] -= 1
                return True 
    return False 


def balance_all_bikes(stations: List[list]) -> int:
    """Calculate the percentage of bikes available across all stations
    and evenly distribute the bikes so that each station has as close to the
    overall percentage of bikes available as possible. Remove bikes from a
    station if and only if the station is renting and there is a bike
    available to rent, and return a bike if and only if the station is
    allowing returns and there is a dock available. Return the difference
    between the number of bikes rented and the number of bikes returned.

    >>> balance_all_bikes(HANDOUT_STATIONS)
    0
    >>> HANDOUT_STATIONS == [\
     [7000, 'Ft. York / Capreol Crt.', 43.639832, -79.395954, 31, 17, 14, True, True], \
     [7001, 'Lower Jarvis St / The Esplanade', 43.647992, -79.370907, \
     15, 8, 7, True, True]]
    True
    """

    x = 0
    y = 0
    for station in stations:
        x = x + station[CAPACITY]
        y = y + station[BIKES_AVAILABLE]

    #根据所有站点的自行车总量，和容量，计算出目标百分比
    goal_percent = round(y*1.0 / x, 2)

    rented_total, returned_total = 0, 0
    #遍历
    for station in stations:
        #记录原来的自行车数量
        original_bikes_available = station[BIKES_AVAILABLE]
        #将要改变的自行车数量
        result = round(goal_percent * station[CAPACITY])

        #将要改变的量 和 原来自行车的数量 两者的差值
        bikes_diff = result - original_bikes_available

        #若差值 < 0, 则说明自行车出租出去
        if bikes_diff <= 0 and \
            station[IS_RENTING] and station[BIKES_AVAILABLE] >= abs(bikes_diff):

            #赋给了新值
            station[BIKES_AVAILABLE] = result
            station[DOCKS_AVAILABLE] = station[CAPACITY] - station[BIKES_AVAILABLE]

            #累加出租自行车的数量
            rented_total = rented_total + abs(bikes_diff)

        #若差值 > 0， 则说明自行车返还回来
        if bikes_diff > 0 and \
            station[IS_RETURNING] and station[DOCKS_AVAILABLE] >= abs(bikes_diff):

            station[BIKES_AVAILABLE] = result
            station[DOCKS_AVAILABLE] = station[CAPACITY] - station[BIKES_AVAILABLE]

            #累加返还自行车的数量
            returned_total = returned_total + bikes_diff
    
    return rented_total - returned_total




        
      


      



if __name__ == '__main__':
    #import doctest
    #doctest.testmod()  

    # # To test your code with larger lists, you can uncomment the code below to
    # # read data from the provided CSV file.
    stations_file = open('stations.csv')
    bike_stations = csv_to_list(stations_file)
    clean_data(bike_stations)

    # # For example,
    print('Testing get_station_with_max_bikes: ', \
         get_station_with_max_bikes(bike_stations) == 7033)