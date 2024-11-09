# dnd-transcript-cleanup
A few cleanup scripts for processing Whisper .tsv files (generated from Craig Discord recordings)

## Setup

1. **Directory Structure**: Place the Whisper-generated transcripts in a directory named after the session (e.g., `SESSION_NAME`). If the session has multiple parts, create subdirectories (e.g., `SESSION_NAME/PART`). For example, sometimes I have 5 hour sessions - I stop and start Craig halfway through the session, so I have two "parts" to process separately.

**Note:** This script does not combine session parts. This is purely organizational. The script will treat "parts" of a session as completely independent, by design.
    
2. **Transcript Files**: Each file should be a TSV file (tab-separated values) with the following columns:
    
    - `start`: Start timestamp of the dialogue line.
    - `end`: End timestamp of the dialogue line.
    - `text`: The transcribed dialogue.
    - `speaker`: The speaker's identifier.
    
    Ensure one file per speaker, containing their respective dialogue lines.
    
3. **Replacement File**: Create a JSON file (`merge_replacements.json`) for any custom word replacements you want. This file will help correct common misinterpretations by Whisper. An example format:
    
    json
    
    Copy code
    
    `{     "Valtor": ["volatore", "walter"],     "Orla": ["ola"] }`
    
**Note:** The script will look for config.py and merge_replacements.json in the same directory as the script. If they aren't found on the first run, they will be copied from the defaults with default values.

## Usage

1. **Remove Short Form Duplicates**: Lines of dialogue that are identical and shorter than `DUPLICATE_TEXT_LENGTH` are removed, except for the first occurrence. These duplicates typically include fillers like “yeah” or “okay” and other artifacts.
    
2. **Merge Close Lines**: Consecutive dialogue lines by the same speaker with less than 0.01 seconds between them are merged, creating a more cohesive dialogue flow.
    
3. **Remove Short Lines**: Lines shorter than `SHORT_TEXT_LENGTH` (like “uh huh” or “oh”) are removed if they don’t add value. Adjust this threshold if you wish.
    
4. **Secondary Duplicate Check**: A second duplicate check is performed on the cleaned dialogue to catch additional redundancies, especially longer, repetitive phrases.
    
5. **Compile All Speakers**: The individual cleaned transcripts are then merged into a single file, sorted by timestamp, ensuring the conversational flow reflects all participants in proper order.
    
6. **Final Merge for Consecutive Lines**: Consecutive lines from the same speaker are combined to further condense the dialogue, making it easier to follow.
    
7. **Word Replacement Pass**: Using the provided replacement file (`merge_replacements.json`), the tool corrects common misinterpretations of specific words or names. This can be useful for unique terms or proper nouns often misinterpreted by Whisper.
    
8. **Splitting the Transcript**: If the final transcript is too large, it can be divided into parts for ease of processing in models with input limitations. (This step is optional if not needed).
    

## Running the Script

1. Ensure you have the necessary files in place:
    
    - Whisper-generated TSV transcripts for each speaker.
    - A `merge_replacements.json` file with any required word replacements.
2. Run the script with the relevant configuration parameters (e.g., `DUPLICATE_TEXT_LENGTH`, `SHORT_TEXT_LENGTH`). Console output will display details of the cleanup process, including which duplicates and lines were removed or merged.
    
3. The output will be a final, cleaned transcript file, ready for review or input into other tools.