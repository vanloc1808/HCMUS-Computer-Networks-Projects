import tkinter as tk
import tkinter.ttk as ttk
from functools import partial

# RGB link: https://htmlcolorcodes.com/

# FUNCTIONS FOR RECEVING DATA FROM SERVER

"""
    function for receving data (ID, Name) about all places from server
    @return: a list of dictionaries, one dictionary for each place
"""
def query_all_places():
    pass

"""
    function for receiving data (ID, Name, Coordinate, Description) about one place from server
    @param:
        id: the id of the place
    @return: a dictionary of the place
"""
def query_one_place(id):
    pass

"""
    function for downloading all avatars of all places from server
    @return: list of directory to avatars (?)
"""
def download_all_avatars():
    pass

"""
    function for downloading all images of one place from server
    @param:
        id: the id of the place
    @return: list of directory to images
"""
def download_images_one_place(id):
    pass

# FUNCTIONS FOR HANDLING MOUSE CLICK EVENTS
def query_one_place_clicked(id, name):
    w = tk.Toplevel()
    w.title("Chi tiết về " + name)
    w['bg'] = '#EAF40D'

    # details = query_one_place(id)
    details = {"ID": "TRV", 
    "Name": "Trà Vinh", 
    "Coordinate": [9.94719, 106.34225], 
    "Description": "Trà Vinh là một tỉnh ven biển thuộc vùng Đồng bằng sông Cửu Long, Việt Nam. Trà Vinh cách Thành phố Hồ Chí Minh 200km đi bằng quốc lộ 53 qua tỉnh Vĩnh Long, khoảng cách rút ngắn thời gian chỉ còn 130km nếu đi bằng quốc lộ 60 qua tỉnh Bến Tre, cách thành phố Cần Thơ 50km. Được bao bọc bởi sông Tiền, sông Hậu với 02 cửa Cung Hầu và Định An nên giao thông đường thủy có điều kiện phát triển."}

    place_id = details['ID']
    place_name = details['Name']
    place_coordinate = details['Coordinate']
    place_description = details['Description']

    # frames and labels
    frm_id = tk.Frame(master=w, bg='#45F40D')
    frm_id.pack(side='top', fill='x', padx=10, pady=10)
    lbl_id = tk.Label(master=frm_id, text='ID: ' + place_id, bg='#45F40D', fg='red')
    lbl_id.pack(side='left', fill='x', padx=10, pady=10)

    frm_name = tk.Frame(master=w, bg='#0DE2F4')
    frm_name.pack(side='top', fill='x', padx=10, pady=10)
    lbl_name = tk.Label(master=frm_name, text='Tên địa điểm: ' + place_name, bg='#0DE2F4', fg='red')
    lbl_name.pack(side='left', fill='x', padx=10, pady=10)

    frm_coordinate = tk.Frame(master=w, bg='#0DC0F4')
    frm_coordinate.pack(side='top', fill='x', padx=10, pady=10)
    str_coordinate = '(' + str(place_coordinate[0]) + ', ' + str(place_coordinate[1]) + ')'
    lbl_coordinate = tk.Label(master=frm_coordinate, text='Tọa độ: ' + str_coordinate, bg='#0DC0F4', fg='red')
    lbl_coordinate.pack(side='left', fill='x', padx=10, pady=10)

    frm_description = tk.Frame(master=w, bg='#0DF468')
    frm_description.pack(side='top', fill='x', padx=10, pady=10)
    lbl_description = tk.Label(master=frm_description, text='Mô tả: ' + place_description, bg='#0DF468', fg='red')
    lbl_description.pack(side='left', fill='x', padx=10, pady=10)


    w.mainloop()