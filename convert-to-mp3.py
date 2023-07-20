import subprocess, os



FIND_EXTENSIONS = ['.webm', '.m4a']
DIR_SAVE = './converted'
DELETE_OLD_FILES = True

if not os.path.exists(DIR_SAVE):
    os.makedirs(DIR_SAVE, exist_ok=True)



files = [
    filename
    for filename in os.listdir()
    if os.path.isfile(filename) and
    ('.' + filename.split('.')[-1]) in FIND_EXTENSIONS
]


print('Total files: ', len(files))
for file in files:
    new_filename = '-'.join(file.split('.')[:-1])

    print('Converting file: ', file)
    convert_result = subprocess.run(
        [
            'ffmpeg',
            '-i',
            file,
            '-vn',
            '-ab',
            '128k',
            '-ar',
            '44100',
            '-y',
            (f'{DIR_SAVE}/' + new_filename + '.mp3')
        ],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
        )
    
    if convert_result.returncode != 0:
        print('Error converting file: ', file)
    else:
        if DELETE_OLD_FILES:
            os.remove(file)

        print('Successfully file converted: ', file)
    



print('All files converted!')

