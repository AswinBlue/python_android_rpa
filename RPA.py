from ppadb.client import Client


class AndroidController:
    def __init__(self):
        print('[AndroidController] init AndroidController')
        self.device = None

    def get_first_device(self, host='127.0.0.1', port=5037):
        # load adb
        adb = Client(host=host, port =port)
        # get device lists
        devices = adb.devices()

        if len(devices) == 0:
            print('[AndroidController] no devices attached')
            return False
        else:
            # get first device connected
            self.device = devices[0]
        return True

    def take_screenshot(self, fname='screen.png'):
        if self.device is None:
            print('[AndroidController] no devices selected')
            return False

        image = self.device.screencap()
        print('[AndroidController] take_screenshot:: ', fname)
        with open(fname, 'wb') as f:
            f.write(image)
        return True

    def make_position_to_string(self, pos):
        result = ' ' + str(pos[0]) + ' ' + str(pos[1]) + ' '
        print(result)
        return result

    def touch_screen(self, pos1):
        if self.device is None:
            print('[AndroidController] no devices selected')
            return False
        self.device.shell('input touchscreen tap'
                          + self.make_position_to_string(pos1))
        return True

    def drag_screen(self, pos1, pos2):
        if self.device is None:
            print('[AndroidController] no devices selected')
            return False
        self.device.shell('input touchscreen swipe'
                          + self.make_position_to_string(pos1)
                          + self.make_position_to_string(pos2)
                          + '100')

    def test1(self):
        # self.device.shell('input touchscreen swipe 500 500 1500 1000 2000')
        for i in range(4):
            for j in range(4):
                self.drag_screen(self.bench[0], self.myPosition[i][j])
                self.drag_screen(self.myPosition[i][j], self.bench[0])

