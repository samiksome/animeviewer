import QtQuick 1.0

Rectangle {
	width:500
	height:200
	color:"lightgray"

	Rectangle {
		anchors.left:parent.left
		anchors.right:parent.right
		anchors.verticalCenter:parent.verticalCenter
		anchors.leftMargin:parent.width*0.2
		anchors.rightMargin:parent.width*0.2
		height:parent.height*0.25
		color:"white"
	}

	Text {
		text:"Hello World!"
		font.family:"Arial"
		font.pointSize:parent.width*0.03
		anchors.centerIn:parent
	}
}
