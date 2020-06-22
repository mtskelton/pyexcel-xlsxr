import os
from unittest.mock import MagicMock

from nose.tools import eq_

from pyexcel_xlsxr import get_data


def test_issue_1():
    test_file = get_fixture("issue_1.xlsx")
    data = get_data(test_file)
    eq_(
        data["dataSheet1"],
        [
            ["", "D0"],
            ["Pads", "PADA"],
            ["Timestamp", "13:26:26.375087"],
            ["I", "V"],
            ["0.0", "0.7830809999999999"],
            ["1.0", "1.11145"],
            ["2.0", "1.176147"],
            ["3.0", "1.222229"],
            ["4.0", "1.25946"],
            ["5.0", "1.293334"],
            ["6.0", "1.323852"],
            ["7.0", "1.351623"],
            ["8.0", "1.3778679999999999"],
            ["9.0", "1.402893"],
            ["10.0", "1.427001"],
            ["11.0", "1.449279"],
            ["12.0", "1.471252"],
            ["13.0", "1.4923089999999999"],
            ["14.0", "1.512451"],
            ["15.0", "1.531982"],
            ["16.0", "1.551513"],
            ["17.0", "1.5701289999999999"],
            ["18.0", "1.588134"],
            ["19.0", "1.606445"],
            ["20.0", "1.623535"],
            ["21.0", "1.64093"],
            ["22.0", "1.657714"],
            ["23.0", "1.674804"],
            ["24.0", "1.6906729999999999"],
            ["25.0", "1.707153"],
            ["26.0", "1.7233269999999998"],
            ["27.0", "1.738586"],
            ["28.0", "1.7544549999999999"],
            ["29.0", "1.769104"],
            ["30.0", "1.784667"],
            ["31.0", "1.799316"],
            ["32.0", "1.8148799999999998"],
            ["33.0", "1.8286129999999998"],
            ["34.0", "1.8432609999999998"],
            ["35.0", "1.85791"],
            ["36.0", "1.871948"],
            ["37.0", "1.885986"],
            ["38.0", "1.900329"],
            ["39.0", "1.913452"],
            ["40.0", "1.92749"],
            ["41.0", "1.941223"],
            ["42.0", "1.954345"],
            ["43.0", "1.967773"],
            ["44.0", "1.9808949999999999"],
            ["45.0", "1.9940179999999998"],
            ["46.0", "2.007446"],
            ["47.0", "2.019958"],
            ["48.0", "2.03247"],
            ["49.0", "2.0455929999999998"],
            ["50.0", "2.05841"],
            ["51.0", "2.071228"],
            ["52.0", "2.083129"],
            ["53.0", "2.095336"],
            ["54.0", "2.1072379999999997"],
            ["55.0", "2.120056"],
            ["56.0", "2.131652"],
            ["57.0", "2.143859"],
            ["58.0", "2.156066"],
            ["59.0", "2.167663"],
            ["60.0", "2.1795649999999998"],
            ["61.0", "2.191162"],
            ["62.0", "2.2021479999999998"],
            ["63.0", "2.214355"],
            ["64.0", "2.225646"],
            ["65.0", "2.236633"],
            ["66.0", "2.247009"],
            ["67.0", "2.258911"],
            ["68.0", "2.269897"],
            ["69.0", "2.2808829999999998"],
            ["70.0", "2.2915639999999997"],
            ["71.0", "2.302246"],
            ["72.0", "2.3138419999999997"],
            ["73.0", "2.3245229999999997"],
            ["74.0", "2.334899"],
            ["75.0", "2.3455809999999997"],
            ["76.0", "2.356262"],
            ["77.0", "2.366333"],
            ["78.0", "2.376708"],
            ["79.0", "2.3864739999999998"],
            ["80.0", "2.3971549999999997"],
            ["81.0", "2.407531"],
            ["82.0", "2.417602"],
            ["83.0", "2.427673"],
            ["84.0", "2.438354"],
            ["85.0", "2.4472039999999997"],
            ["86.0", "2.457885"],
            ["87.0", "2.467956"],
            ["88.0", "2.477722"],
            ["89.0", "2.487487"],
            ["90.0", "2.4978629999999997"],
            ["91.0", "2.506408"],
            ["92.0", "2.515869"],
            ["93.0", "2.5256339999999997"],
            ["94.0", "2.535095"],
            ["95.0", "2.54425"],
            ["96.0", "2.5537099999999997"],
            ["97.0", "2.562866"],
            ["98.0", "2.572021"],
            ["99.0", "2.5805659999999997"],
            ["100.0", "2.589721"],
        ],
    )


def test_issue_5():
    native_sheet = MagicMock(
        name="test", raw=MagicMock(return_value=[[None, 11, "11"]])
    )
    from pyexcel_xlsxr.xlsxr import XLSXSheet

    sheet = XLSXSheet(native_sheet)
    data = sheet.to_array()
    eq_(list(data), [[None, 11, 11]])


def get_fixture(file_name):
    return os.path.join("tests", "fixtures", file_name)
