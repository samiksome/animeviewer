import QtQuick 1.0

Rectangle {
    id:"app_window"

	width:500
	height:200
	color:"#eeeeee"

	signal exit_gui()
	signal search_start(string param)
	
	function clearSearchInput() {
	    search_input.text=""
	}

	Rectangle {
		id:"top_bar"
		anchors.top:parent.top
		anchors.left:parent.left
		anchors.right:parent.right
		height:parent.height*0.05
		color:"#0d47a1"
	}
	Text {
	    id:"top_bar_text"
		anchors.top:parent.top
		anchors.left:parent.left
		height:parent.height*0.05
		anchors.leftMargin:parent.height*0.0125
		verticalAlignment:Text.AlignVCenter
		text:"Search Anime"
		font.bold:false
		font.family:"Roboto"
		font.pointSize:parent.height*0.015
		color:"#ffffff"
	}
	Rectangle {
	    id:"top_bar_shadow"
		anchors.top:top_bar.bottom
		anchors.left:parent.left
		anchors.right:parent.right
		height:2
		color:"#444444"
	}

    Rectangle {
	    id:"search_bar_shadow"
	    anchors.left:search_bar.left
		anchors.right:search_bar.right
		anchors.top:search_bar.top
		anchors.topMargin:2
		height:search_bar.height
		radius:search_bar.radius
		color:"#444444"
	}
	Rectangle {
	    id:"search_bar"
		anchors.top:top_bar_shadow.bottom
		anchors.left:parent.left
		anchors.right:parent.right
		height:parent.height*0.1
		anchors.topMargin:parent.height*0.05
		anchors.leftMargin:parent.height*0.05
		anchors.rightMargin:parent.height*0.05
		radius:height*0.1
		color:"#ffffff"
	}
	TextInput {
	    id:"search_input"
		anchors.left:search_bar.left
		anchors.right:search_button.left
		anchors.verticalCenter:search_bar.verticalCenter
		font.family:"Roboto"
		font.pointSize:parent.height*0.03
		anchors.leftMargin:parent.height*0.03
		anchors.rightMargin:parent.height*0.03
		color:"#000000"
		
		onAccepted:parent.search_start(text)
	}
	Text {
	    id:"search_button"
	    anchors.right:search_bar.right
	    anchors.top:search_bar.top
	    anchors.bottom:search_bar.bottom
	    verticalAlignment:Text.AlignVCenter
	    font.family:"Roboto"
	    font.pointSize:parent.height*0.06
	    anchors.rightMargin:parent.height*0.03
	    text:"\u2794"
	    color:"#000000"
	}
	MouseArea {
	    id:"search_button_mouse_area"
	    anchors.right:search_bar.right
	    anchors.top:search_bar.top
	    anchors.bottom:search_bar.bottom
	    anchors.left:search_input.right
	    
	    onClicked:parent.search_start(search_input.text)
	}

	Rectangle {
	    id:"close_button"
		anchors.top:parent.top
		anchors.right:parent.right
		width:parent.height*0.025
		height:parent.height*0.025
		radius:width*0.5
		anchors.topMargin:width*0.5
		anchors.rightMargin:width*0.5
		color:"#ffffff"
	}
	MouseArea {
	    id:"close_button_mouse_area"
		anchors.top:parent.top 
                anchors.right:parent.right
                width:parent.height*0.025
                height:parent.height*0.025
		anchors.topMargin:width*0.5
		anchors.rightMargin:width*0.5

		onClicked:parent.exit_gui()
	}
}
