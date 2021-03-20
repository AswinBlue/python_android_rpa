import RPA
import ImageParser


class Coordinate:
        myPosition = [[(470, 360), (650, 360), (815, 360), (980, 360)],
                           [(420, 460), (610, 460), (790, 460), (980, 460)],
                           [(360, 560), (570, 560), (770, 560), (960, 560)],
                           [(290, 700), (550, 700), (730, 700), (930, 700)]]

        enemyPosition = [[(1330, 370), (1510, 370), (1680, 370), (1850, 370)],
                              [(1350, 460), (1530, 460), (1720, 460), (1890, 460)],
                              [(1370, 590), (1550, 590), (1770, 590), (1960, 590)],
                              [(1390, 720), (1600, 720), (1820, 720), (2030, 720)]]
        bench = [(500, 930), (700, 930), (840, 930), (1030, 930), (1190, 930),
                      (1360, 930), (1530, 930), (1700, 930), (1870, 930)]
        item = (330, 930)
        store = (2060, 930)
        buy = [(550, 680), (880, 680), (1220, 680), (1530, 680), (1840, 680)]
        gemstone = (140, 340)
        resetStore = (2260, 580)
        cube = (140, 590)
        start = (1210, 160)
        info_need = [(1700, 420), (1880, 420), (2040, 420), (2210, 420)]
        info_assemble = [(1700, 670), (1880, 670), (2040, 670), (2210, 670)]
        info_name = [(1850, 130), (1920, 170)]
        info_need_name = [[(1640, 470), (1780, 500)], [(1810, 470), (1940, 500)],
                          [(1970, 470), (2110, 500)], [(2150, 470), (2280, 500)]]
        info_assemble_name = [[(1640, 700), (1780, 740)], [(1810, 700), (1940, 740)],
                                   [(1970, 700), (2110, 740)], [(2150, 700), (2280, 740)]]


if __name__ == '__main__':
    # create instances
    ac = RPA.AndroidController()
    te = ImageParser.TextExtractor(r'C:\Users\jepil\AppData\Local\Programs\Tesseract-OCR\tesseract.exe')

    # set android device
    #ac.get_first_device()
    # ac.test1()

    # take image and extract text
    image = None
    image_name = 'test.png'

    #if ac.take_screenshot(image_name) is True:
        # te.parse_image(te.load_image(image_name, Coordinate.info_name[0], Coordinate.info_name[1]))
    te.compare_image('sample1.png', 'sample2.png')

