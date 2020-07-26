from types import SimpleNamespace
from typing import Union

def antigcp() -> bool : ...
def bitmap_to_backbuffer(bmp_id:int, operation:int, x:Optional[int] = 0, y:Optional[int] = 0) -> bool : ...
def bitmap_to_string(bmp_id: int) -> str : ...
def calculate_minimap_alignment(map_center_x:int, map_center_y:int, radius:int, wall_color:int, color_tolerance:int, deformation_tolerance:int) -> SimpleNamespace: ...
def calculate_minimap_movement(map_center_x:int, map_center_y:int, radius:int, point_count:int, rotation_tolerance:int, color_tolerance:int, deformation_tolerance:int, max_distance:int) -> SimpleNamespace: ...
def click_mouse(x:int, y:int, button:int) -> None: ...
def click_mouse_random_area(left:int, top:int, right:int, bottom:int, button:int) -> None: ...
def create_rotated_bitmap(bmp_id:int, rotation_float:float) -> int: ...
def destroy_bitmap(bmp_id:int) -> None: ...
def distance(left:int, top:int, right:int, bottom:int) -> int: ...
def double_click_mouse(x:int, y:int, button:int) -> None: ...
def dump_backbuffer() -> None: ...
def dump_backbuffer_to_bitmap_string() -> str: ...
def dump_backbuffer_to_bitmap_string_rect(left:int, top:int, right:int, bottom:int) -> str: ...
def dump_window_structure() -> None: ...
def erase_backbuffer() -> None: ...
def erase_backbuffer_rect(left:int, top:int, right:int, bottom:int) -> None: ...
def find_bitmap(bmp_id:int, left:Optional[int] = 0, top:Optional[int] = 0, right:Optional[int] = -1, bottom:Optional[int] = -1, color_tolerance:Optional[int] = 0, deformation_tolerance:Optional[int] = 0, percent_match:Optional[int] = 99, closest:Optional[bool] = False, x:Optional[int] = 0, y:Optional[int] = 0) -> Union[bool, SimpleNamespace]: ...
def find_bitmap_spiral(bmp_id:int, left:Optional[int] = 0, top:Optional[int] = 0, right:Optional[int] = -1, bottom:Optional[int] = -1, color_tolerance:Optional[int] = 0, deformation_tolerance:Optional[int] = 0, x:Optional[int] = 0, y:Optional[int] = 0) -> Union[bool, SimpleNamespace]: ...
def find_color( color:int, left:Optional[int] = 0, top:Optional[int] = 0, right:Optional[int] = -1, bottom:Optional[int] = -1, color_tolerance:Optional[int] = 0) -> Union[bool, SimpleNamespace]: ...
def find_color_spiral(color:int, left:Optional[int] = 0, top:Optional[int] = 0, right:Optional[int] = -1, bottom:Optional[int] = -1, color_tolerance:Optional[int] = 0, exclude_radius:Optional[int] = 0,  x:Optional[int] = 0, y:Optional[int] = 0) -> Union[bool, SimpleNamespace]: ...
def find_text_using_font(font_id:int, text:str, left:Optional[int] = 0, top:Optional[int] = 0, right:Optional[int] = -1, bottom:Optional[int] = -1, minimum_spacing:Optional[int] = 0, maximum_spacing:Optional[int] = 30, color_tolerance:Optional[int] = 0, deformation_tolerance:Optional[int] = 0) -> Union[bool, SimpleNamespace]: ...
def create_encrypted(script:str, unique_code:str) -> str: ...
def run_encrypted(script:str) -> None: ...
def unique_code() -> str: ...
def focus_game_window() -> None: ...
def unfocus_game_window() -> None: ...
def force_oversized_backbuffer(width:int, height:int) -> bool: ...
def get_ancestor_window_hwnd() -> int: ...
def get_async_key_state(virtual_key:int) -> int: ...
def get_backbuffer_height() -> int: ...
def get_backbuffer_width() -> int: ...
def get_bitmap_height(bmp_id:int) -> int: ...
def get_bitmap_width(bmp_id:int) -> int: ...
def get_color(x:int, y:int) -> int: ...
def get_font_height(bmp_id:int) -> int: ...
def get_game_dims() -> SimpleNamespace: ...
def get_game_rect() -> SimpleNamespace: ...
def get_game_title() -> str: ...
def get_height() -> int: ...
def get_inner_window_class_name_by_hwnd(hwnd:int) -> Union[bool, str]: ...
def get_inner_window_dims(hwnd:int) ->  Union[bool, SimpleNamespace]: ...
def get_inner_window_from_ancestor_point(x:int, y:int) -> int: ...
def get_inner_window_from_point(x:int, y:int) -> int: ...
def get_inner_window_text_by_hwnd(hwnd:int) -> int: ...
def get_last_mouse_x() -> int: ...
def get_last_mouse_y() -> int: ...
def get_modules() -> dict: ...
def get_poly_point(color:int, left:Optional[int]=0, top:Optional[int]=0, right:Optional[int]=-1, bottom:Optional[int]=-1, color_tolerance:Optional[int]=30, gap_tolerance:Optional[int]=10, margin:Optional[int]=0) -> Union[bool,SimpleNamespace]: ...
def get_width() -> int: ...
def get_window_hwnd() -> int: ...
def is_color(color_a:int, color_b:int, color_tolerance:int) -> bool: ...
def is_inner_window(hwnd:int) -> bool: ...
def key_down(scan_code:int) -> None: ...
def key_up(scan_code:int) -> None: ...
def load_bitmap_from_backbuffer(left:Optional[int]=0, top:Optional[int]=0, right:Optional[int]=-1, bottom:Optional[int]=-1, transparent_color:Optional[int]=0, is_mask:Optional[bool]=False, override_bmp_id:Optional[int]=0) -> int: ...
def load_bitmap_from_bytes(byte_array:bytes, transparent_color:Optional[int]=0, is_mask:Optional[bool]=False, strip_alpha:Optional[bool]=False) -> int: ...
def load_bitmap_from_file(file_name:str, transparent_color:Optional[int]=0, is_mask:Optional[bool]=False) -> : ...
def load_bitmap_from_string(bmp_string:str, transparent_color:Optional[int]=0, is_mask:Optional[bool]=False) -> : ...
def load_font_from_bitmap(bmp_id:int, characters:str, transparent_color:Optional[int]=0) -> int: ...
def load_mask_from_bytes(byte_array:bytes, transparent_color:Optional[int]=0, is_mask:Optional[bool]=0, strip_alpha:Optional[bool]=False) -> : ...
def load_mask_from_file(file_name:str, transparent_color:Optional[int]=0xff00ff, is_mask:Optional[bool]=True) -> int: ...
def load_mask_from_string(bmp_string:str, transparent_color:Optional[int]=0xff00ff, is_mask:Optional[bool]=True) -> int: ...
def mouse_button_down(x:int, y:int, button:int) -> None: ...
def mouse_button_up(x:int, y:int, button:int) -> None: ...
def move_mouse(x:int, y:int) -> bool: ...
def next_inner_windows_iterator() -> int: ...
def ocr_using_font(font_id:int, left:Optional[int]=0, top:Optional[int]=0, right:Optional[int]=-1, bottom:Optional[int]=-1, minimum_spacing:Optional[int]=0, maximum_spacing:Optional[int]=30, color_tolerance:Optional[int]=50, deformation_tolerance:Optional[int]=0) -> Union[bool,SimpleNamespace]: ...
def ready() -> bool: ...
def reset_inner_windows_iterator() -> None: ...
def save_bitmap_to_file(bmp_id:int, file_name:str) -> bool: ...
def scrape() -> None: ...
def scrape_rect(left:int, top:int, width:int, height:int) -> None: ...
def select_inner_window_by_hwnd(hwnd:int) -> bool: ...
def select_inner_window(class_name:str) -> bool: ...
def select_inner_window_exact(class_name:str) -> bool: ...
def select_inner_window_from_ancestor_point(x:int, y:int) -> bool: ...
def select_inner_window_from_point(x:int, y:int) -> bool: ...
def select_inner_window_regex(class_name_regex:str) -> bool: ...
def send_alt_key(key:int) -> None: ...
def send_keys(keys:str) -> None: ...
def set_color(x:int, y:int, color:int) -> None: ...
def set_gdi_capture_off() -> None: ...
def set_gdi_capture_on() -> None: ...
def set_human_mouse_mode_off() -> None: ...
def set_human_mouse_mode_on() -> None: ...
def set_mouse_delay(us_delay:int, us_delay_random:Optional[int]) -> None: ...
def set_virtual_inputs_off() -> None: ...
def set_virtual_inputs_on() -> None: ...
def set_virtual_mouse_java_mode_off() -> None: ...
def set_virtual_mouse_java_mode_on() -> None: ...
def set_virtual_mouse_wfp_mode_off() -> None: ...
def set_virtual_mouse_wfp_mode_on() -> None: ...
def set_window_by_hwnd(hwnd:int) -> Union[bool,str]: ...
def set_window_by_title_and_class_regex(title_regex:str, class_regex:str) -> Union[bool,str]: ...
def set_window_by_title(title:str) -> Union[bool,str]: ...
def set_window_by_title_regex(title_regex:str) -> Union[bool,str]: ...
def set_window(title:str) -> Union[bool,str]: ...
def set_wmprint_off() -> None: ...
def set_wmprint_on() -> None: ...
def show_bitmap_picker() -> SimpleNamespace: ...
def show_color_picker() -> SimpleNamespace: ...
def show_game_window(maximize_window:bool) -> None: ...
def show_inner_window_picker() -> None: ...
def sleep(milliseconds:int) -> None: ...
def unselect_inner_window() -> None: ...
