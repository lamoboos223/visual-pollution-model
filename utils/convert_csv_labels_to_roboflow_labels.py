import pybboxes as pbx

W, H = 1920, 1080  # WxH of the image
def convert_to_yolo_format(x_min, y_min, x_max, y_max):
    yolo_bbox = (x_min, y_min, x_max, y_max)
    r = pbx.convert_bbox(yolo_bbox, from_type="coco", to_type="yolo", image_size=(W, H))
    r = ' '.join(map(str,r))

    return r
    
# TODO: read CSV as data frame
'''
in the df you get the class number, image_path, class name, xmax, xmin, ymax, ymin
- you will use the image path to name the new file
- you will pass xmax, xmin, ymax, ymin to the below method to convert for you the format
- you will use the class number with newly converted format of xmax, xmin, ymax, ymin to write in
- the file you created with the image path.
- the class name field will not be used for now.
'''

# example
x_max, x_min, y_max, y_min = 736.0,657.0,275.0,229.0
print(convert_to_yolo_format(x_min, y_min, x_max, y_max))
# you don't to change the W and H


# TODO: create file <name of the image>.txt and dump the class number and the result in the variable r e.g.
''' before --> train.csv

class,image_path,name,xmax,xmin,ymax,ymin
3.0,4a48c42c9579ec0399e6c5a3e825e765.jpg,GARBAGE,797.0,701.0,262.0,211.0
3.0,4a48c42c9579ec0399e6c5a3e825e765.jpg,GARBAGE,932.0,786.0,329.0,238.0
3.0,4a48c42c9579ec0399e6c5a3e825e765.jpg,GARBAGE,736.0,657.0,275.0,229.0
'''

''' after --> 4a48c42c9579ec0399e6c5a3e825e765.jpg.txt  and the content like below

0 0.59765625 0.3402777777777778 0.3651041666666667 0.19537037037037036
0 0.6901041666666666 0.4148148148148148 0.409375 0.22037037037037038
0 0.5544270833333333 0.36064814814814816 0.3421875 0.21203703703703702
'''
