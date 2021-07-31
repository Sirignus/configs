from libqtile.widget.battery import Battery, BatteryStatus

class CustomBattery(Battery):

    def build_string(self, status: BatteryStatus) -> str:
        percent = status.percent * 100

        icon = ''
        if percent < 5:
            icon =  '  '
        elif percent < 30:
            icon = '  '
        elif percent < 60:
            icon =  '  '
        elif percent < 90:
            icon =  '  '
        else:
            icon =  '  '
        
        return icon + f'{percent:.0f}' + '%'
