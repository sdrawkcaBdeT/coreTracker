import cv2 as cv2
import numpy as np

haystack = cv2.imread('omega_strikers/find_the_core.jpg')
grayhaystack = cv2.cvtColor(haystack, cv2.COLOR_BGR2GRAY)

needle = cv2.imread('omega_strikers/os_core.jpg')
grayneedle =cv2.cvtColor(needle, cv2.COLOR_BGR2GRAY)

cv2.imshow('Needle', needle)
cv2.imshow('Haystack', haystack)

#methods available :[cv2.TM_CCOEFF, cv2.TM_CCOEFF_NORMED, cv2.TM_CCORR, cv2.TMO_CCORR_NORMED, cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]
result = cv2.matchTemplate(grayhaystack, grayneedle, cv2.TM_CCOEFF_NORMED)

min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
needle_w = needle.shape[1]
needle_h = needle.shape[0]
top_left = max_loc
bottom_right = (top_left[0] + needle_w, top_left[1] + needle_h)
output = cv2.rectangle(haystack, top_left, bottom_right, (0, 0, 255), 3)

cv2.imshow('Haystack', grayhaystack)
cv2.imshow('Result', result)
cv2.imshow('output', output)
cv2.waitKey(0)

cv2.imwrite('haystack_needle.png', output)