#indexscanner.py
import requests, urllib.request, time

address = input("Please input an URL:")
max = int(input("Please input max index:"))
print("Starting Script")
active = []

def scan():
    """
    Scans Website Index
    Inputs:
        Website URL        - Required  : URL To Scan, E.g. https://www.hants.gov.uk/cctv/WCAM1 but without the index number (1)  (Str)
        MAX Index          - Optional  : MAX Index Number To Reach (Int)
    Options: 
        Download?          - Optional  : Download Active List Items (Str)
    Input:    
        File Path          - Required  : File Path To Downlaod To (Str)
    """
    index = 0
    item = list(range(index, max))
    for item in progressBar(item, prefix = 'Progress:', suffix = 'Complete', length = 50):
                response = requests.get(str(address) + str(index) + ".jpg")
                code = response.status_code
                index += 1
                if code == 200:
                    active.append(index)
            # else:
                # time.sleep(0.1)
    print("\n Max reached")
    print(str(len(active)) + " active indexs found")
    download = input("Downlaod? y/n: ")
    if download == "y":
            folder = input("Please input a file Directory: ")
            for i in active: 
                imgURL = str(address) + str(i) + ".jpg"
                urllib.request.urlretrieve(imgURL, folder + str(i) + ".jpg")
                print("Downloading " + folder + str(i) + ".jpg") 
            print("Downlaoded all " + str(len(active)) + "files")
    else:
        print("Active indexs found; " + str(active))

def progressBar(iterable, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█', printEnd = "\r"):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
        printEnd    - Optional  : end character (e.g. "\r", "\r\n") (Str)
    """
    total = len(iterable)
    # Progress Bar Printing Function
    def printProgressBar (iteration):
        percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
        filledLength = int(length * iteration // total)
        bar = fill * filledLength + '-' * (length - filledLength)
        print(f'\r{prefix} |{bar}| {percent}% {suffix}', end = printEnd)
    # Initial Call
    printProgressBar(0)
    # Update Progress Bar
    for i, item in enumerate(iterable):
        yield item
        printProgressBar(i + 1)
    # Print New Line on Complete
    print()

scan()