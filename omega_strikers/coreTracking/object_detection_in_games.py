import cv2 as cv2
import numpy as np
import pandas as pd

# name of the file for the image to act as the haystack (img with desired object to find)

# Object for storing the top left and bottom right location of the core in each frame
core_location = list()
core_center = list()

for x in range(5388):
    current_iter = str(x)
    
    haystack_filename="video-frame"+current_iter.rjust(5,"0")
    haystack_filetype='.png'
    haystack_filepath='omega_strikers/coreTracking/img/haystacks/onivillage fullgoal/'

    # Define haystack (image to find the needle in)
    haystack = cv2.imread(haystack_filepath+haystack_filename+haystack_filetype)
    # grayscale transformation
    grayhaystack = cv2.cvtColor(haystack, cv2.COLOR_BGR2GRAY)

    # Define the needle (image of os core in this case)
    needle = cv2.imread('omega_strikers/coreTracking/img/needle/os_core.jpg')
    # grayscale transformation
    grayneedle =cv2.cvtColor(needle, cv2.COLOR_BGR2GRAY)

    # # Uncomment to show image
    # cv2.imshow('Needle', needle)
    # cv2.waitKey(0)

    # # Uncomment to show image
    # cv2.imshow('Haystack', haystack)
    # cv2.waitKey(0)

    #methods available :[cv2.TM_CCOEFF, cv2.TM_CCOEFF_NORMED, cv2.TM_CCORR, cv2.TMO_CCORR_NORMED, cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]
    result = cv2.matchTemplate(grayhaystack, grayneedle, cv2.TM_CCOEFF_NORMED)

    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    needle_w = needle.shape[1]
    needle_h = needle.shape[0]
    top_left = max_loc
    bottom_right = (top_left[0] + needle_w, top_left[1] + needle_h)
    output = cv2.rectangle(haystack, top_left, bottom_right, (0, 0, 255), 3)

    core_location.append([top_left,bottom_right])
    
    core_center.append(
        (
            np.mean((core_location[x][0][0], core_location[x][1][0])),
            np.mean((core_location[x][0][1], core_location[x][1][1]))
            )
        )

    # # Show haystack gray
    # cv2.imshow('Haystack', grayhaystack)

    # # Show transformed image
    # cv2.imshow('Result', result)

    # Show image with 'needle' found (if not found there will be no bounding box)
    # cv2.imshow('output', output)
    # cv2.waitKey(0)



    # Write output image
    cv2.imwrite('omega_strikers/coreTracking/img/searched/searched_{}.png'.format(haystack_filename), output)
    


df_core_loc = pd.DataFrame(core_center, columns=['xdim','ydim'])

df_core_loc.to_csv("core_location onivillage.csv")
    
    

    # Might need different core for when it turns red
    # How to note when goal is scored
    # How to feed continuous streams of image for core tracking
    # How to mark events (saves, shots (crossing defined line))
    # How to deal with different maps
    # Initially - goal is to watch omega strikers game and tally proper score for each team - left and right.
    # Then layer in core location, user strikes, goals, and eventually ability usuage
    # How to build this into a system...
    # One though already is to have have same video processed with different 'needle' images (needles=All Strikers, to track striker location and sense who was in game. To do so would require a separate needle image of the striker to process the video, unless there's a way to sense mutiple objects in frame and denote they are different through the current framework)

    # Need to fix code from other repo that attempted continuous stream stuff - need working continous stream of images to process. Need to demark events. Need whole data processing structure for an os game tbh
    
    # How to deal with time? If extracting video frames, the data will need to eventually be put on a timeline to make sense -- how can that be done with numbered images?
    
    # Image of soccer shots and conversion: https://soccerlogic.com/2017/04/18/conversion-rates-sg-by-shot-location/ one goal is to recreate this (shot tracking is a later feature)
    # Here's the same for baskeball: https://www.hoopcoach.org/advanced-field-goal-percentage-analysis-for-basketball-players/
    # Hockey's is fantastic: http://apps.chicagotribune.com/sports/hockey/shot_charts/?eventId=1542407
    # soccer pass map: https://madaboutsports.in/how-to-analyse-pass-maps-in-football/
    
    # for oni village, the goal happens in frame 05191. Going to have to come up with a way to trim these, then.
    # for aimis app, goal is frame 00796??