import cv2 as cv2
import numpy as np
import pandas as pd
import time as time

# Goal here is to support the awakening draft phase of the game by displaying what awakening are available in the pool still.

# To do this, the program will need to understand which of the 34 currently draftable awakenings are available.

# There's a choice between two awakenings during character selection - after this selection these awakenings
# are removed from the awakening pool (AP) and will not be available again this game.
# After a set is completed, characters draft awakenings according to their performance.
# In each Awakenings Draft, there are 8 Awakenings available for selection.
# All awakenings in the draft will not show up again, regardless of if they were selected or not.
# In the first Awakenings draft, the 8 Awakenings drawn will be drawn from a pool of 32 (34 less the 2 character selection awkns)
# In the second draft, the awakenings will be drawn from a pool of 24.
# If there's a third draft, the awakenings will be drawn from a pool of 16.
# If there's a fourth draft, the awakenings will be the remaining 8.

# Here's a list of the currently in-play awakenings:

LIST_AWAKENINGS = list((
    'SPECIALIZED TRAINING',
    'RAPID FIRE',
    'MISSILE PROPULSION',
    'TWIN DRIVE',
    'SUPER SURGE',
    'CAST TO LAST',
    'MONUMENTALIST',
    'PRIMETIME',
    'HOTSHOT',
    'BUILT DIFFERENT',
    'EXTRA SPECIAL',
    'TIMELESS CREATOR',
    'TEMPO SWING',
    'CHRONOBOOST',
    'BIG FISH',
    'HEAVY IMPACT',
    'PEAK PERFORMANCE',
    'BULK UP',
    'AERIALS',
    'QUICK STRIKE',
    'REVERBERATION',
    'GLASS CANNON',
    'STACKS ON STACKS',
    'DEADEYE',
    'ORB DANCER',
    'ORB PONDERER',
    'ORB REPLICATOR',
    'EGOIST',
    'CATALYST',
    'FIRE UP!',
    'STAGGER SWAGGER',
    'ONE-TWO PUNCH',
    'PRIZE FIGHTER',
    'PERFECT FORM',)
)


# I'm thinking about it like this-- let's ignore the 2 awakenings that go away at the start of the game, then
# awk1-available
# awk2-available
# awk3-available
# awk..n-available

# All awakenings are set to 'available' at the start of a match.
# The program runs during the first draft, it searches from the top of the list down- so specialized training is searched for first
# If it's found, update SPECIALIZED TRAININGS 'AVAILABLE' to 'UNAVAILABLE'
# If not found, do not change status of awakening and continue to next awakening.

# SET AWAKENINGS TO AVAILABLE
df_awakening_status = pd.DataFrame({'AWAKENING':LIST_AWAKENINGS})
df_awakening_status['STATUS'] = 'AVAILABLE'
awakenings_found = 0

# this must run continuously, so I'm putting it in a while loop that causes the code to run until at least the
# first two awakenings drafts have been completed.
while awakenings_found >= 18:    
    time.sleep(15) # sleep for fifteen seconds before re-running    
    for awakening in LIST_AWAKENINGS:
    
        haystack_filename="draft00"
        haystack_filetype='.png'
        haystack_filepath='omega_strikers/awakeningPool/img/haystacks/'

        # Define haystack (image to find the needle in)
        haystack = cv2.imread(haystack_filepath+haystack_filename+haystack_filetype)
        # grayscale transformation
        grayhaystack = cv2.cvtColor(haystack, cv2.COLOR_BGR2GRAY)
        
        # Define the needle 
        needle = cv2.imread('omega_strikers/awakeningPool/img/needle/{}.png'.format(awakening))
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
        
        # # Show haystack gray
        # cv2.imshow('Haystack', grayhaystack)

        # # Show transformed image
        # cv2.imshow('Result', result)

        # Show image with 'needle' found (if not found there will be no bounding box)
        # cv2.imshow('output', output)
        # cv2.waitKey(0)



            
        if max_val >= .8:
            print('found.')
            awakenings_found = awakenings_found + 1
            df_awakening_status.loc[df_awakening_status['AWAKENING']==awakening,"STATUS"]="NOT AVAILABLE"        
            # Write output image
            cv2.imwrite('omega_strikers/awakeningPool/img/searched/found/{}.png'.format(awakening), output)
            
        else:
            print('not found')
        

awakenings_found
df_awakening_status        

