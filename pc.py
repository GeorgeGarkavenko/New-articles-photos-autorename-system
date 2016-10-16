import csv
from glob import glob
from os import rename
from sys import argv

def main(main_file="info.csv", errors_report="pc_errors.txt"):
    
    """
    pc for Alicja v1.3
    Rename to add new photos for positions
    """
    present_articles = glob("8383*.jpg")
    present_photos = []
    with open(main_file, 'rb') as main_f:
        all_records = csv.reader(main_f, delimiter=";")
        absent_numbers = []
        for row in all_records:
            counter = 0
            for number in row[1:]:
                if number:
                    counter += 1
                    #print('DSC_{0:0>4}.JPG'.format(number))
                    new_picture_name = '{0}({1}).jpg'.format(row[0], counter)
                    if new_picture_name in present_articles:
                        present_photos.append(new_picture_name)
                    else:
                        try:
                            rename('DSC_{0:0>4}.JPG'.format(number), new_picture_name)
                        except WindowsError:
                            absent_numbers.append(number)

        if(absent_numbers or present_photos):
            with open(errors_report, 'w') as errors_f:
                if absent_numbers: errors_f.write("Absent numbers:\n")
                for number in absent_numbers:
                    errors_f.write('DSC_{0:0>4}.JPG\n'.format(number))
                
                if present_photos: errors_f.write("\nPresent photos:\n")
                for photo in present_photos:
                    errors_f.write('{0}\n'.format(photo))

        
if __name__ == "__main__":
    main(*argv[1:])