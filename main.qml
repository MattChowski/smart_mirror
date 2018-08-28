import QtQuick 2.11
import QtQuick.Controls 1.4
import QtQuick.Layouts 1.2

ApplicationWindow {
    Item {
        id: variables
        property var bgColor: "#1e1e1e"
        property var textColor: "#ffffff"
    }

    id: mainWindow

    visible: true
    width: 640
    height: 480
    title: "Smart Mirror 1.0"
    color: variables.bgColor

    //Temp and status
    Rectangle {
        id: mainArea
        color: "transparent"
        opacity: 0
        
        anchors.left: parent.left
        anchors.top: parent.top
        anchors.right: parent.right
        anchors.bottom: parent.bottom
        
        anchors.margins: (mainWindow.height / 10) / 2
        
        //Date
        Rectangle {
            id: mainDate
            width: childrenRect.width
            height: childrenRect.height
            color: "transparent"

            Text {
                text: {window.mainWeatherDate()}
                font.pixelSize: (mainWindow.width / 10) / 4
                font.family: "Montserrat"
                color: variables.textColor
            }
        }

        //Temp
        Rectangle {
            id: mainTemp
            width: childrenRect.width
            height: childrenRect.height
            anchors.top: mainDate.bottom
            color: "transparent"
            Text {
                id: mainTempText
                text: {window.mainWeatherTemp()}
                font.pixelSize: mainWindow.width / 10
                font.family: "Montserrat"
                color: variables.textColor
            }
        }

        //Date
        Rectangle {
            id: mainStatus
            anchors.top: mainTemp.bottom
            width: childrenRect.width
            height: childrenRect.height
            color: "transparent"
            Text {
                text: {window.mainWeatherStatus()}
                font.pixelSize: (mainWindow.width / 10) / 4
                font.family: "Montserrat"
                color: variables.textColor
            }
        }

        //opacity animation
        SequentialAnimation {
            running: true
            PauseAnimation {duration: 500}
            NumberAnimation {target: mainArea; property: "opacity"; from: 0; to: 1; duration: 2000}
        }
    }
}