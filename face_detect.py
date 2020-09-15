# /usr/bin/python3
import numpy as np
import cv2


def detect(img, cascade):
    rects = cascade.detectMultiScale(img, scaleFactor=1.1, minNeighbors=3, minSize=(80, 80),
                                     flags=cv2.CASCADE_SCALE_IMAGE)
    if len(rects) == 0:
        return []
    rects[:, 2:] += rects[:, :2]
    return rects


def draw_rects(img, rects, color):
    for x1, y1, x2, y2 in rects:
        cv2.rectangle(img, (x1, y1), (x2, y2), color, 2)


def mask_overlay(background, x, y):
    overlay_img = cv2.imread('smile.png')
    overlay_gray = cv2.cvtColor(overlay_img, cv2.COLOR_BGR2GRAY)

    contours, hierarchy = cv2.findContours(overlay_gray, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    overlay_img_mask = np.zeros_like(overlay_img)
    cv2.drawContours(overlay_img_mask, contours, -1, (255, 255, 255), -1)
    idx = np.where(overlay_img_mask == 255)
    background[y + idx[0], x + idx[1], idx[2]] = overlay_img[idx[0], idx[1], idx[2]]
    return background


if __name__ == '__main__':
    cascade_fn = "haarcascade_frontalface_alt.xml"
    nested_fn = "haarcascade_eye.xml"

    cascade = cv2.CascadeClassifier(cascade_fn)
    nested = cv2.CascadeClassifier(nested_fn)

    cam = cv2.VideoCapture(0)
    cam.set(cv2.CAP_PROP_FRAME_WIDTH, 960)
    cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

    while True:
        ret, img = cam.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        gray = cv2.equalizeHist(gray)
        rects = detect(gray, cascade)
        vis = img.copy()
        draw_rects(vis, rects, (0, 255, 0))
        for x1, y1, x2, y2 in rects:
            roi = gray[y1:y2, x1:x2]
            vis_roi = vis[y1:y2, x1:x2]
            subrects = detect(roi.copy(), nested)
            draw_rects(vis_roi, subrects, (255, 0, 0))
            #mask_overlay(vis, x1 - 65, y1 + 65)
            mask_overlay(vis, x1, y1)
        cv2.imshow('facedetect', vis)
        if 0xFF & cv2.waitKey(5) == 27:
            break
    cv2.destroyAllWindows()
