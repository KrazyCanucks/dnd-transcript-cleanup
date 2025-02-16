# config.py

import os

# Configurable parameters

# Session name and part are folder names for storing your recordings
SESSION_NAME = "Recordings" # This is the main folder name for the session
PART = ' ' # If your recordings are split into different folder parts, change this to the appropriate part


# Base path configuration for the file directory
if PART != ' ':
    BASE_PATH = os.path.join('C:\\', 'Recordings', SESSION_NAME, PART)
else:
    BASE_PATH = os.path.join('C:\\', 'Recordings', SESSION_NAME)


# Name mappings - change these to your player's craig discord names 
# and map them to their character names
NAME_MAPPINGS = {
    'KrazyCanucks': 'DM(Scott)',    

    'Shedneck': 'Eolas', 
    'Reail8': 'Graye', 
    'CmnderThrawn': 'Naldon', 
    'Draglock': 'Lars',    
    'theFlash8Six': 'Lysikor',
    'xxxOMGxxx': 'Ragnarock',        
    'Warchydle73': 'Skullgrin',

    'Spectator01': 'Mike',
    'Spectator02': 'Toby',    
}

# Overlap Splitting
MAX_LENGTH = 50000 # Maximum length of one part of the transcript in characters
OVERLAP = 3000 # Number of characters to overlap between parts

# Text length settings
DUPLICATE_TEXT_LENGTH = 4  # Maximum text length for duplicates to be considered
MERGE_THRESHOLD = 0.01     # Threshold for merging text based on 'end' and 'start'
SHORT_TEXT_LENGTH = 1      # Maximum text length to be removed

# CSV output filenames
PROCESSED_CSV_SUFFIX = '_processed.csv'
COMBINED_CSV_FILENAME = f'{SESSION_NAME}_{PART}_processed.csv'
MERGED_CSV_FILENAME = f'{SESSION_NAME}_{PART}_merged.csv'
FINAL_TXT_FILENAME = f'{SESSION_NAME}_{PART}_final.txt'
REPLACEMENTS_FILE = 'merge_replacements.json'  # Path to replacements JSON file

