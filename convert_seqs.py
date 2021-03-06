import os
import cv2
from glob import glob

def save_img(frame, out_dir, file_name, frame_num):
    full_file_name = os.path.join(out_dir, file_name + '_' + \
                                  str(frame_num).zfill(6) + ".jpg")
    cv2.imwrite(full_file_name, frame)

def convert_seqs(dataset, config):
    config = config[dataset]
    seq_dir = config["seq_dir"]
    img_dir = config["img_dir"]

    img_cnt = 1
    for dname in sorted(glob(os.path.join(seq_dir, "set*"))):
        set_name = dname.split("/")[-1]
        out_dir = os.path.join(img_dir, set_name)
        os.makedirs(out_dir, exist_ok=True)

        for fn in sorted(glob('{}/*.seq'.format(dname))):
            file_name = fn.split('/')[-1].split(".")[0]
            cap = cv2.VideoCapture(fn)
            frame_num = 0
            while True:
                ret, frame = cap.read()
                if not ret:
                    break
                save_img(frame, out_dir, file_name, frame_num)
                frame_num += 1
            print(fn)
