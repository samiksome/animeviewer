import QtQuick 1.0

Rectangle {
    id:"app_window"

	width:500
	height:200
	color:"#eeeeee"

	signal exit_gui()
	signal search_start(string param)
	signal browse_back()
	signal browse_forward()
	
	function setInfoAreaVisibility(val) {
	    info_area.visible=val
	    info_area_shadow.visible=val
	    browse_bar.visible=val
	    browse_back_button.visible=val
	    browse_forward_button.visible=val
	    browse_back_button.visible=val
	    browse_forward_button.visible=val
	    browse_back_button_mouse_area.visible=val
	    browse_forward_button_mouse_area.visible=val
	    anime_title.visible=val
	    anime_picture.visible=val
	}
	
	function setAnimeInfo(dispname,picture) {
	    anime_title.text=dispname
	    anime_picture.source=picture
	}
	
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
		text:"Anime Viewer"
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
	
	Rectangle {
	    id:"info_area_shadow"
	    anchors.top:info_area.top
	    anchors.left:info_area.left
	    anchors.right:info_area.right
	    height:info_area.height
	    anchors.topMargin:2
	    radius:search_bar.height*0.1
	    color:"#444444"
	    visible:false
	}
	Rectangle {
	    id:"info_area"
	    anchors.top:search_bar_shadow.bottom
	    anchors.left:parent.left
	    anchors.right:parent.right
	    anchors.bottom:parent.bottom
	    anchors.topMargin:parent.height*0.05
	    anchors.bottomMargin:parent.height*0.05
	    anchors.leftMargin:parent.height*0.05
	    anchors.rightMargin:parent.height*0.05
	    radius:search_bar.height*0.1
	    color:"#ffffff"
	    visible:false
	}
	
	Rectangle {
	    id:"browse_bar"
	    anchors.top:info_area.top
	    anchors.left:info_area.left
	    anchors.right:info_area.right
	    height:search_bar.height*1.5
	    radius:search_bar.height*0.1
	    color:"#0d47a1"
	    visible:false
	}
	Text {
	    id:"browse_back_button"
	    anchors.left:info_area.left
	    anchors.verticalCenter:browse_bar.verticalCenter
	    font.family:"Roboto"
	    font.pointSize:search_button.font.pointSize
	    anchors.leftMargin:search_button.anchors.rightMargin
	    text:"\u2190"
	    color:"#ffffff"
	    visible:false
	}
	MouseArea {
	    id:"browse_back_button_mouse_area"
	    anchors.left:info_area.left
	    anchors.right:anime_title.left
	    anchors.top:info_area.top
	    anchors.bottom:browse_bar.bottom
	    visible:false
	    
	    onClicked:parent.browse_back()
	}
	Text {
	    id:"browse_forward_button"
	    anchors.right:info_area.right
	    anchors.verticalCenter:browse_bar.verticalCenter
	    font.family:"Roboto"
	    font.pointSize:search_button.font.pointSize
	    anchors.rightMargin:search_button.anchors.rightMargin
	    text:"\u2192"
	    color:"#ffffff"
	    visible:false
	}
	MouseArea {
	    id:"browse_forward_button_mouse_area"
	    anchors.left:anime_title.right
	    anchors.right:info_area.right
	    anchors.top:info_area.top
	    anchors.bottom:browse_bar.bottom
	    visible:false
	    
	    onClicked:parent.browse_forward()
	}
	Text {
	    id:"anime_title"
	    anchors.verticalCenter:browse_bar.verticalCenter
	    anchors.left:browse_back_button.right
	    anchors.right:browse_forward_button.left
	    anchors.leftMargin:parent.height*0.03
	    anchors.rightMargin:parent.height*0.03
	    font.family:"Roboto"
	    font.pointSize:parent.height*0.03
	    wrapMode:Text.WordWrap
	    text:"Anime Title\nJapanese Name"
	    color:"#ffffff"
	    visible:false
	}
	
	Image {
	    id:"anime_picture"
	    anchors.top:browse_bar.bottom
	    anchors.left:info_area.left
	    anchors.bottom:info_area.bottom
	    anchors.topMargin:parent.height*0.03
	    anchors.bottomMargin:parent.height*0.03
	    anchors.leftMargin:parent.height*0.03
	    anchors.rightMargin:parent.height*0.03
	    smooth:true
	    fillMode:Image.PreserveAspectFit
	    visible:false
	}
}
