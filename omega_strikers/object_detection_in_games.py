import cv2 as cv2
import numpy as np

haystack = cv2.imread('omega_strikers/sc_02_img_02.jpg')
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

cv2.imwrite('haystack_needle_scen_02_02.png', output)

# Might need different core for when it turns red
# How to note when goal is scored
# How to feed continuous streams of image for core tracking
# How to mark events (saves, shots (crossing defined line))
# How to deal with different maps
# Initially - goal is to watch omega strikers game and tally proper score for each team - left and right.
# Then layer in core location, user strikes, goals, and eventually ability usuage
# How to build this into a system...
# One though already is to have have same video processed with different 'needle' images (needles=All Strikers, to track striker location and sense who was in game. To do so would require a separate needle image of the striker to process the video, unless there's a way to sense mutiple objects in frame and denote they are different through the current framework)
# 